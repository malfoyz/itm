import asyncio
from pathlib import Path

from celery import Celery
import pytesseract
from PIL import Image

from src.config import settings
from src.documents.dependencies import get_document_repository


celery = Celery(
    'tasks',
    broker=f'amqp://{settings.RABBITMQ_DEFAULT_USER}:{settings.RABBITMQ_DEFAULT_PASS}@{settings.RABBITMQ_HOST}:{settings.RABBITMQ_PORT}//',
    backend=settings.CELERY_RESULT_BACKEND,
)


@celery.task
def analyse_image_task(document_id: int, image_path: Path | str) -> str:
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
        repo = get_document_repository()

        loop = asyncio.get_event_loop()
        loop.run_until_complete(repo.add_text_to_document(document_id, text))
        return text
    except Exception as e:
        print(e)
