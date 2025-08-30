from sqlalchemy import create_engine, Column, Integer, String, Numeric, Boolean, ForeignKey
from pathlib import Path
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

proj_path = Path(__file__).parent #learning_adv
sqlite_engine = create_engine(url=f"sqlite:///{proj_path}/database.db")
#sqlite_engine = create_engine("sqlite:///:memory:", echo=True)

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    price = Column(Numeric(10, 2), nullable=False)  # число с фиксированной точностью
    in_stock = Column(Boolean, default=True)

    # связь с категорией (многие-к-одному)
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="products")

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255))
    products = relationship("Product", back_populates="category")

SessionLocal = sessionmaker(bind=sqlite_engine)
session = SessionLocal()
Base.metadata.create_all(bind=sqlite_engine)

if __name__ == "__main__":

    cat1 = Category(name="Electronics", description="Electronic devices")
    cat2 = Category(name="Books", description="Printed and digital books")

    p1 = Product(name="Smartphone", price=699.99, in_stock=True, category=cat1)
    p2 = Product(name="Laptop", price=1200.00, in_stock=False, category=cat1)
    p3 = Product(name="Novel", price=15.50, in_stock=True, category=cat2)

    session.add_all([cat1, cat2, p1, p2, p3])
    session.commit()

    for product in session.query(Product).all():
        print(product.name, "-> category:", product.category.name)
