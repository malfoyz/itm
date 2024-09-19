import datetime
from sqlalchemy import ForeignKey, String, Text, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base


class Document(Base):
    """Модель документа"""
    __tablename__ = 'document'
    id: Mapped[int] = mapped_column(primary_key=True)
    path: Mapped[str] = mapped_column(String(length=1024))
    date: Mapped[datetime.date] = mapped_column(
        default=text("(CURRENT_TIMESTAMP AT TIME ZONE 'UTC')::DATE"),
    )

    document_texts: Mapped[list['DocumentText']] = relationship(
        back_populates='document'
    )


class DocumentText(Base):
    """Модель текста документа"""
    __tablename__ = 'document_text'
    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(Text, default='')
    document_id: Mapped[int] = mapped_column(ForeignKey('document.id'))

    document: Mapped['Document'] = relationship(
        back_populates='document_texts'
    )




