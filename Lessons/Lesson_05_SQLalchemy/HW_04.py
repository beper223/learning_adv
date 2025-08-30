from sqlalchemy import create_engine, Column, Integer, String, Numeric, Boolean, ForeignKey, func
from pathlib import Path
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

proj_path = Path(__file__).parent #learning_adv
sqlite_engine = create_engine(url=f"sqlite:///{proj_path}/database.db")
# sqlite_engine = create_engine("sqlite:///:memory:") #echo=True

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    in_stock = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="products")

    def __repr__(self):
        return f"Продукт: {self.name}: {self.price}"

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255))
    products = relationship("Product", back_populates="category")

    def __repr__(self):
        return f"Категория: {self.name} ({self.description})"

SessionLocal = sessionmaker(bind=sqlite_engine)
session = SessionLocal()
Base.metadata.create_all(bind=sqlite_engine)

if __name__ == "__main__":
    # Очистка базы
    # session.query(Product).delete()
    # session.query(Category).delete()
    # session.commit()

    # 1. Наполнение данными
    cat_electronics = Category(name="Электроника", description="Гаджеты и устройства.")
    cat_books = Category(name="Книги", description="Печатные книги и электронные книги.")
    cat_clothes = Category(name="Одежда", description="Одежда для мужчин и женщин.")

    session.add_all([cat_electronics, cat_books, cat_clothes])
    session.flush()

    products = [
        Product(name="Смартфон", price=299.99, in_stock=True, category=cat_electronics),
        Product(name="Ноутбук", price=499.99, in_stock=True, category=cat_electronics),
        Product(name="Научно-фантастический роман", price=15.99, in_stock=True, category=cat_books),
        Product(name="Джинсы", price=40.50, in_stock=True, category=cat_clothes),
        Product(name="Футболка", price=20.00, in_stock=True, category=cat_clothes),
    ]
    session.add_all(products)
    session.commit()

    # 2. Чтение данных
    print("\n--- Категории и продукты ---")
    categories = session.query(Category).all()
    for c in categories:
        print(c)
        for p in c.products:
            print(f"   - {p}")

    # 3. Обновление данных
    print("\n--- Обновление цены смартфона ---")
    smartphone = session.query(Product).filter(Product.name == "Смартфон").first()
    if smartphone:
        smartphone.price = 349.99
        session.commit()
        print("Новая цена смартфона:", smartphone.price)

    # 4. Агрегация и группировка
    print("\n--- Количество продуктов в каждой категории ---")
    counts = (
        session.query(Category.name, func.count(Product.id))
        .join(Product, Category.id == Product.category_id)
        .group_by(Category.id)
        .all()
    )
    for name, cnt in counts:
        print(f"{name}: {cnt} продуктов")

    # 5. Группировка с фильтрацией
    print("\n--- Категории с более чем одним продуктом ---")
    multi_counts = (
        session.query(Category.name, func.count(Product.id).label("prod_count"))
        .join(Product, Category.id == Product.category_id)
        .group_by(Category.id)
        .having(func.count(Product.id) > 1)
        .all()
    )
    for name, cnt in multi_counts:
        print(f"{name}: {cnt} продуктов")

