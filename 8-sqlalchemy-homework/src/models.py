import datetime
from typing import Annotated

from sqlalchemy import CheckConstraint, ForeignKey, Numeric, String, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base, str_address, str_phone, str_name


int_pk = Annotated[int, mapped_column(primary_key=True)]


class Clients(Base):
    """Модель клиента"""

    __tablename__ = 'clients'
    id: Mapped[int_pk]
    full_name: Mapped[str_name]
    address: Mapped[str_address]
    phone: Mapped[str_phone]

    orders: Mapped[list['Orders']] = relationship(
        back_populates='client',
    )


class Suppliers(Base):
    """Модель поставщика"""

    __tablename__ = 'suppliers'
    id: Mapped[int_pk]
    name: Mapped[str_name]
    representative: Mapped[str | None] = mapped_column(String(128))
    contact: Mapped[str | None] = mapped_column(String(128))
    phone: Mapped[str_phone]
    address: Mapped[str_address]

    supplies: Mapped[list['Supplies']] = relationship(
        back_populates='supplier',
    )


class Supplies(Base):
    """Модель поставки"""

    __tablename__ = 'supplies'
    id: Mapped[int_pk]
    supply_date: Mapped[datetime.date | None]
    supplier_id: Mapped[int | None] = mapped_column(ForeignKey('suppliers.id', ondelete='SET NULL'))

    supplier: Mapped['Suppliers'] = relationship(
        back_populates='supplies',
    )
    goods: Mapped[list['Goods']] = relationship(
        back_populates='supply',
    )


class Goods(Base):
    """Модель товара"""

    __tablename__ = 'goods'
    id: Mapped[int_pk]
    name: Mapped[str_name]
    technical_specifiactions: Mapped[str | None] = mapped_column(String(256))
    description: Mapped[str | None] = mapped_column(String(256))
    image: Mapped[str | None] = mapped_column(String(1024))
    purchase_cost: Mapped[float | None] = mapped_column(Numeric(12, 2))
    selling_cost: Mapped[float | None] = mapped_column(Numeric(12, 2))
    is_in_stock: Mapped[bool | None] = mapped_column(default=False)
    count: Mapped[int | None] = mapped_column(default=0)
    supply_id: Mapped[int | None] = mapped_column(ForeignKey('supplies.id', ondelete='SET NULL'))

    supply: Mapped['Supplies'] = relationship(
        back_populates='goods',
    )
    orders: Mapped[list['Orders']] = relationship(
        back_populates='good',
    )

    __table_args__ = (
        CheckConstraint(sqltext='purchase_cost >= 0', name='check_purchase_cost_positive'),
        CheckConstraint(sqltext='selling_cost >= 0', name='check_selling_cost_positive'),
        CheckConstraint(sqltext='count >= 0', name='check_count_positive'),
    )


class Employees(Base):
    """Модель сотрудника"""

    __tablename__ = 'employees'
    id: Mapped[int_pk]
    last_name: Mapped[str] = mapped_column(String(64))
    first_name: Mapped[str] = mapped_column(String(64))
    middle_name: Mapped[str | None] = mapped_column(String(64))
    position: Mapped[str | None] = mapped_column(String(64))
    address: Mapped[str_address]
    phone: Mapped[str_phone]
    birthday: Mapped[datetime.date | None]

    orders: Mapped[list['Orders']] = relationship(
        back_populates='employee',
    )


class Orders(Base):
    """Модель заказа"""

    __tablename__ = 'orders'
    id: Mapped[int_pk]
    posting_date: Mapped[datetime.date | None] = mapped_column(
        default=text("(CURRENT_TIMESTAMP AT TIME ZONE 'UTC')::DATE"),
    )
    execution_date: Mapped[datetime.date | None] = mapped_column(
        default=text("(CURRENT_TIMESTAMP AT TIME ZONE 'UTC')::DATE"),
    )
    employee_id: Mapped[int] = mapped_column(ForeignKey('employees.id'))
    good_id: Mapped[int] = mapped_column(ForeignKey('goods.id'))
    client_id: Mapped[int] = mapped_column(ForeignKey('clients.id'))

    employee: Mapped['Employees'] = relationship(
        back_populates='orders',
    )
    good: Mapped['Goods'] = relationship(
        back_populates='orders',
    )
    client: Mapped['Clients'] = relationship(
        back_populates='orders'
    )


