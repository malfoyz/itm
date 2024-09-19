import os
import shutil
from pathlib import Path

from fastapi import UploadFile


class DocumentFileManager:
    """
    Менеджер для управления документами на жестком диске.

    :attr

    :param media_path: Путь для работы с файлами.
    :type
    """
    MEDIA_PATH: Path = Path(__file__).resolve().parent.parent / 'media'

    def __init__(self, media_path: Path | str = MEDIA_PATH):
        self.MEDIA_PATH.mkdir(parents=True, exist_ok=True)

    def save_file(self, file: UploadFile) -> str:
        """
        Сохраняет файл локально в директории.

        :param file: Файл, который нужно сохранить.
        :type file: UploadFile

        :return: Путь к файлу
        :rtype: str
        """

        path = self.MEDIA_PATH / file.filename
        with open(path, 'wb') as buffer:
            shutil.copyfileobj(file.file, buffer)
        return str(path)

    def delete_file(self, filename: str) -> None:
        """
        Удаляет файл локально из директории.

        :param filename: Имя файла, который нужно удалить.
        :type filename: str

        :return: None
        :rtype: None
        """
        try:
            path = self.MEDIA_PATH / filename
            if os.path.exists(path):
                os.remove(path)
        except Exception as e:
            print(f"Произошла ошибка при удалении файла {path}: {e}")
