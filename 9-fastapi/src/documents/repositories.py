from sqlalchemy.ext.asyncio import AsyncSession

from src.documents.exceptions import DocumentNotFoundException, DocumentTextNotFoundException
from src.documents.models import Document, DocumentText


class DocumentRepository:
    """
    Репозиторий для работы с документами в базе данных, в том числе CRUD-операций.

    :param session: Асинхронная сессия для работы с базой данных.
    :type session: AsyncSession
    """

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, path: str) -> Document:
        """
        Создает документ в базе данных.

        :param path: Путь к файлу.
        :type path: str

        :return: Объект модели документа.
        :rtype: Document
        """
        document = Document(path=path)
        self.session.add(document)
        await self.session.commit()
        await self.session.refresh(document)
        return document

    async def get_filename_by_id(self, id: int) -> str:
        """
        Возвращает имя файла по его идентификатору.

        :param id: Идентификатор файла.
        :type id: int

        :return: Имя файла.
        :rtype: str

        :raises DocumentNotFoundException: если такого документа нет в базе данных
        """
        document = await self.session.get(Document, id)
        if document is None:
            raise DocumentNotFoundException("Document not found")
        filename = document.path.split('/')[-1]
        return filename

    async def delete_one(self, id: int) -> None:
        """
        Удаляет документ из базы данных.

        :param id: Идентификатор удаляемого документа
        :rtype id: int

        :return: None
        :rtype: None

        :raises DocumentNotFoundException: если такого документа нет в базе данных
        """
        document = await self.session.get(Document, id)
        if document is None:
            raise DocumentNotFoundException("Document not found")
        await self.session.delete(document)
        await self.session.commit()

    async def add_text_to_document(self, document_id: int, text: str) -> None:
        """
        Добавляет текст в базу данных.

        :param document_id: идентификатор документа, которому принадлежит текст
        :type document_id: int

        :param text: текст, который нужно добавить
        :type text: str

        :return: None
        :rtype: None

        :raises DocumentNotFoundException: если такого документа нет в базе данных
        """
        document = await self.session.get(Document, id)
        if document is None:
            raise DocumentNotFoundException("Document not found")
        document_text = DocumentText(text=text)
        document_text.document = document
        await self.session.commit()

    async def get_document_text(self, document_id: int) -> str:
        """
        Возвращает текст документа по идентификатору документа.

        :param document_id: идентификатор документа, которому принадлежит текст
        :type document_id: int

        :return: текст документа
        :rtype: str

        :raises DocumentNotFoundException: если такого документа нет в базе данных
        """

        document = await self.session.get(Document, id)
        if document is None:
            raise DocumentNotFoundException("Document not found")
        try:
            document_text = document.document_texts[0]
        except Exception as e:
            print(e)
        else:
            text = document_text.text
            return text