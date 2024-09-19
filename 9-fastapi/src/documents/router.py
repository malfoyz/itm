from fastapi import Depends, UploadFile, status
from fastapi.responses import Response, JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.routing import APIRouter

from src.documents.dependencies import (
    get_document_file_manager,
    get_document_repository,
    validate_image,
)
from src.documents.exceptions import DocumentNotFoundException
from src.documents.repositories import DocumentRepository
from src.documents.services import DocumentFileManager
from src.documents.tasks import analyse_image_task


router = APIRouter(
    prefix='/documents',
    tags=['Documents'],
)


@router.post('/images')
async def upload_image(
        file: UploadFile = Depends(validate_image),
        file_manager: DocumentFileManager = Depends(get_document_file_manager),
        repo: DocumentRepository = Depends(get_document_repository),
) -> JSONResponse:
    """
    Загружает изображение, сохраняет на диск в папку documents,
    и добавляет в базу запись в таблицу Documents.

    :param file: Изображение для загрузки (проверяется через validate_image).
    :type file: UploadFile

    :param file_manager: Файловый менеджер для работы с файлами документов.
    :param file_manager: DocumentFileManager

    :param repo: Репозиторий для работы с документами в базе данных.
    :type repo: DocumentRepository

    :return: JSON-ответ с результатами загрузки и добавления в базу данных.
    :rtype: Response

    :raises HTTPException: при ошибках загрузки или записи в базу данных
    """

    try:
        path = file_manager.save_file(file)
        document = await repo.add_one(path)

        # return Response(                # решил сделать со схемой так вместо словаря, так как структура однотипная
        #     status='success',
        #     data={
        #         'filename': file.filename,
        #         'filepath': path,
        #         'document_id': document.id,
        #     },
        #     details=None,
        # )
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={
                'status': 'success',
                'data': {
                    'filename': file.filename,
                    'filepath': path,
                    'document_id': document.id,
                },
                'details': None,
            }
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                'status': 'error',
                'data': None,
                'details': None,
            }
        )


@router.delete('/images/{id}')
async def delete_image(
        id: int,
        file_manager: DocumentFileManager = Depends(get_document_file_manager),
        repo: DocumentRepository = Depends(get_document_repository),
):
    """
    Принимает id документа и удаляет его в базе данных и на диске.

    :param id: Идентификатор документа в таблице `Documents`.
    :type id: int

    :param file_manager: Файловый менеджер для работы с файлами документов.
    :param file_manager: DocumentFileManager

    :param repo: Репозиторий для работы с документами в базе данных.
    :type repo: DocumentRepository

    :return: JSON-ответ с результатами загрузки и добавления в базу данных.
    :rtype: Response

    :raises DocumentNotFoundException: если такого изображения нет
    :raises HTTPException: при ошибках загрузки или записи в базу данных
    """
    try:
        filename = await repo.get_filename_by_id(id)
        file_manager.delete_file(filename)
        await repo.delete_one(id)

        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except DocumentNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                'status': 'error',
                'data': None,
                'details': {'Document not found.'},
            }
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                'status': 'error',
                'data': None,
                'details': None,
            }
        )


@router.post('/images/analyse/{id}')
async def analyse_image(
        id: int,
        file_manager: DocumentFileManager = Depends(get_document_file_manager),
        repo: DocumentRepository = Depends(get_document_repository),
) -> JSONResponse:
    """
    Апи должна принимать id документа
    и вызывать функцию очереди задач celery для выполнения в фоновом режиме.
    В методе celery необходимо вызвать библиотеку tesseract
    для получения текста и записать результат в Documents_text.
    Вам здесь понадобиться брокер сообщений, например RabbitMQ.
    """
    try:
        filename = await repo.get_filename_by_id(id)
        path = file_manager.MEDIA_PATH / filename
        task = analyse_image_task.delay(id, path)

        return JSONResponse(
            status_code=status.HTTP_202_ACCEPTED,
            content={
                'status': 'accepted',
                'data': {
                    'task_id': task.id,
                },
                'details': 'Task has been accepted and is being processed.',
            }
        )
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                'status': 'error',
                'data': None,
                'details': None,
            }
        )


@router.get('/get_text/{document_id}')
async def get_text(
        document_id: int,
        repo: DocumentRepository = Depends(get_document_repository),
):
    """Апи должна принимать id документа и возвращать текст из БД."""
    try:
        text = await repo.get_document_text(document_id)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                'status': 'success',
                'data': {
                    'document_id': document_id,
                    'text': text,
                },
                'details': None,
            }
        )
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                'status': 'error',
                'data': None,
                'details': None,
            }
        )