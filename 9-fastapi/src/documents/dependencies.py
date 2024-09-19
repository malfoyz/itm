from fastapi import Depends, UploadFile, status
from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.documents.repositories import DocumentRepository
from src.documents.services import DocumentFileManager


def get_document_repository(session: AsyncSession = Depends(get_async_session)) -> DocumentRepository:
    """
    Создает и возвращает экземпляр репозитория для работы с документами в БД.

    Эта функция используется для получения экземпляра `DocumentRepository`,
    настроенного с текущей асинхронной сессией базы данных.

    :param session: Асинхронная сессия для работы с базой данных.
    :type session: AsyncSession

    :return: Экземпляр `DocumentRepository`, настроенный с переданной сессией.
    :rtype: DocumentRepository
    """
    return DocumentRepository(session)


def get_document_file_manager() -> DocumentFileManager:
    """
    Создает и возвращает экземпляр файлового менеджера для работы с документами на жестком диске.

    Эта функция используется для получения экземпляра `DocumentRepository`,
    настроенного с текущей асинхронной сессией базы данных.

    :return: Экземпляр `DocumentFileManager`
    :rtype: DocumentFileManager
    """
    return DocumentFileManager()


async def validate_image(file: UploadFile) -> UploadFile:
    """
    Проверяет, что файл является изображением.

    :param file: Файл, который нужно проверить.
    :type file: fastapi.UploadFile

    :return: Файл, прошедший валидацию.
    :rtype: UploadFile
    """

    if file.content_type not in ['image/jpeg', 'image/png']:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                'status': 'error',
                'data': None,
                'details': 'File must be an image in JPEG or PNG format',
            }
        )
    return file