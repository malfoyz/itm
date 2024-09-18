from typing import Annotated

from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from config import settings


engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True,
    # pool_size = 5
)

session_factory = sessionmaker(bind=engine)


str_address = Annotated[str | None, 256]
str_phone = Annotated[str | None, 12]
str_name = Annotated[str, 256]


class Base(DeclarativeBase):
    type_annotation_map = {
        str_address: String(256),
        str_phone: String(12),
        str_name: String(256),
    }

    repr_cols_num = 3
    repr_cols = tuple()

    def __repr__(self):
        """Relationships не используются в repr(), т.к. могут вести к неожиданным подгрузкам"""
        cols = []
        for idx, col in enumerate(self.__table__.columns.keys()):
            if col in self.repr_cols or idx < self.repr_cols_num:
                cols.append(f"{col}={getattr(self, col)}")

        return f"<{self.__class__.__name__} {', '.join(cols)}>"