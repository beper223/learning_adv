# Задача 1. Создание модели Mineral
# Создать таблицу минералов с полями:
#
# id: PK
# name: уникальное имя (строка, макс. 50)
# color: строка
# hardness: значение по шкале Мооса, float
# pip install python-dotenv

from db_connector import engine, Base
from sqlalchemy import Integer, String, Float, UniqueConstraint, Index, DateTime, ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime


class Mineral(Base):
    __tablename__ = 'mineral'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255))
    color: Mapped[str] = mapped_column(String(255))
    hardness: Mapped[float] = mapped_column(Float)

    shipments_info: Mapped[list['Shipment']] = relationship('Shipment', back_populates='mineral_info')

# Задача 7. Связь Salon и Shipment через M2M
#
# Один Shipment может быть доставлен в несколько салонов
# Один Salon может принимать разные Shipment
# Настроить Many-to-Many через таблицу salon_shipment_association
salon_shipment_association = Table(
    "salon_shipments",
    Base.metadata,
    Column("salon_id", ForeignKey('salons.id'), primary_key=True),
    Column("shipment_id", ForeignKey('shipments.id'), primary_key=True)
)

# Задача 2. Создание модели Salon
# Создать модель элитного бутика. Поля:
#
# id: PK
# name: название
# location: строка
# Пара (name, location) должна быть уникальна.
class Salon(Base):
    __tablename__ = "salons"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    location: Mapped[str] = mapped_column(String(150))

    __table_args__ = (
        UniqueConstraint(
            'name',
            'location',
            name='unq_name_location'
        ),
        Index(
            'idx_name_location',
            'name',
            'location'
        )
    )

# Задача 3. Создание модели Shipment
# Модель поставки минерала. Поля:
#
# id: PK
# shipment_date: дата
# destination: строка
# mineral_id: FK - ForeignKey

class Shipment(Base):
    __tablename__ = "shipments"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    shipment_date: Mapped[datetime] = mapped_column(DateTime)
    destination: Mapped[str] = mapped_column(String(150))
    mineral_id: Mapped[int] = mapped_column(ForeignKey('mineral.id')) #ForeignKey (o2m - one to many)

    mineral_info: Mapped[list[Mineral]] = relationship('Mineral', back_populates='shipments_info')


