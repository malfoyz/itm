from fastapi import Depends, UploadFile, status
from fastapi.responses import Response, JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.routing import APIRouter

from src.documents.dependencies import (
    get_document_file_manager,
    get_document_repository,
    validate_image,
)
from src.documents.exceptions import DocumentNotFoundException, DocumentTextNotFoundException
from src.documents.repositories import DocumentRepository
from src.documents.services import DocumentFileManager
from src.documents.tasks import analyse_image_task

router = APIRouter(
    prefix='/documents',
    tags=['Documents'],
)


@router.post('/images', status_code=status.HTTP_201_CREATED, summary="Загрузить изображение")
async def upload_image(
        file: UploadFile = Depends(validate_image),
        file_manager: DocumentFileManager = Depends(get_document_file_manager),
        repo: DocumentRepository = Depends(get_document_repository),
) -> JSONResponse:
    """
    Загружает изображение, сохраняет на диск в папку documents,
    и добавляет в базу запись в таблицу Documents.

    - **file**: изображение для загрузки

    Возвращает ответ с информацией о загруженном изображении.
    """

    try:
        path = file_manager.save_file(file)
        document = await repo.add_one(path)

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


@router.delete('/images/{id}', status_code=status.HTTP_204_NO_CONTENT, summary='Удалить изображение')
async def delete_image(
        id: int,
        file_manager: DocumentFileManager = Depends(get_document_file_manager),
        repo: DocumentRepository = Depends(get_document_repository),
):
    """
    Удаляет документ в базе данных и на диске с помощью его идентификатора.

    - **id**: идентификатор документа

    Возвращает ответ с информацией о загруженном изображении.
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


@router.post('/images/analyse/{id}', status_code=status.HTTP_202_ACCEPTED, summary='Обработать изображение')
async def analyse_image(
        id: int,
        file_manager: DocumentFileManager = Depends(get_document_file_manager),
        repo: DocumentRepository = Depends(get_document_repository),
) -> JSONResponse:
    """
    Анализирует текст в изображении в фоновом режиме,
    затем сохраняет этот текст в базу данных.

    - **id**: идентификатор изображения (документа)

    Возвращает идентификатор задачи и статус выполнения.
    """
    try:
        filename = await repo.get_filename_by_id(id)
        path = str(file_manager.MEDIA_PATH / filename)

        task = analyse_image_task.delay(path)
        text = task.get(timeout=10)

        await repo.add_text_to_document(id, text)

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
    except DocumentNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                'status': 'error',
                'data': None,
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


@router.get('/texts/{document_id}', summary='Получить текст изображения')
async def get_text(
        document_id: int,
        repo: DocumentRepository = Depends(get_document_repository),
):
    """
    Возвращает текст из базы данных по идентификатору изображения (документа).

    - **document_id**: идентификатор документа, которому приндлежит текст
    """
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
    except DocumentTextNotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                'status': 'error',
                'data': None,
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