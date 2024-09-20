import asyncio
import logging
from pathlib import Path

from celery import Celery
import pytesseract
from PIL import Image

from src.config import settings


celery = Celery(
    'tasks',
    broker=f'amqp://{settings.RABBITMQ_DEFAULT_USER}:{settings.RABBITMQ_DEFAULT_PASS}@{settings.RABBITMQ_HOST}:{settings.RABBITMQ_PORT}//',
    backend=settings.CELERY_RESULT_BACKEND,
)

celery.conf.update(
    result_expires=3600,
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
)


@celery.task
def analyse_image_task(image_path: str) -> str:
    """
    Анализирует изображение и возвращает текст.

    Данная функция переводит текст с изображения в строку.

    :param id:
    :type id: int

    :param image_path: Путь к изображению, которое нужно проанализировать.
    :type image_path: str

    :return: Текст, полученный с изображения.
    :rtype: str
    """
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image, lang='rus')
        return text
    except Exception as e:
        print(e)
