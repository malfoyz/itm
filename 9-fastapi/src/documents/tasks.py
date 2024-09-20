import asyncio
import logging
from pathlib import Path

from celery import Celery
import pytesseract
from PIL import Image

from src.config import settings
from src.database import get_async_session
from src.documents.dependencies import DocumentRepository, get_document_repository


logger_tasks = logging.getLogger(__name__)
logger_tasks.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
handler.setFormatter(formatter)
logger_tasks.addHandler(handler)


celery = Celery(
    'tasks',
    broker=f'amqp://{settings.RABBITMQ_DEFAULT_USER}:{settings.RABBITMQ_DEFAULT_PASS}@{settings.RABBITMQ_HOST}:{settings.RABBITMQ_PORT}//',
    backend=settings.CELERY_RESULT_BACKEND,
)


@celery.task
def analyse_image_task(document_id: int, image_path: str) -> str:
    """
    Анализирует изображение и возвращает текст.

    Данная функция переводит текст с изображения в строку.

    :param id:
    :type id: int

    :param image_path: Путь к изображению, которое нужно проанализировать.
    :type image_path: Path | str

    :return: Текст, полученный с изображения.
    :rtype: str
    """
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image, lang='rus')

        loop = asyncio.get_event_loop()
        session = loop.run_until_complete(get_async_session())
        repo = DocumentRepository(session)
        loop.run_until_complete(repo.add_text_to_document(document_id, text))

        return text
    except Exception as e:
        print(e)
