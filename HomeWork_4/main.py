from sqlalchemy import create_engine, Column, Integer, String, Numeric, Boolean, ForeignKey, func
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm.decl_api import declarative_base

engine = create_engine('sqlite:///:memory:')

Base = declarative_base()


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String(255))
    products = relationship("Product", back_populates="category")


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    price = Column(Numeric(10, 2))
    in_stock = Column(Boolean)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship("Category", back_populates="products")


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


# задача 1
cat1 = Category(name="Электроника", description="Гаджеты и устройства.")
cat2 = Category(name="Книги", description="Печатные книги и электронные книги.")
cat3 = Category(name="Одежда", description="Одежда для мужчин и женщин.")

session.add(cat1)
session.add(cat2)
session.add(cat3)

p1 = Product(name="Смартфон", price=299.99, in_stock=True, category=cat1)
p2 = Product(name="Ноутбук", price=499.99, in_stock=True, category=cat1)
p3 = Product(name="Научно-фантастический роман", price=15.99, in_stock=True, category=cat2)
p4 = Product(name="Джинсы", price=40.50, in_stock=True, category=cat3)
p5 = Product(name="Футболка", price=20.00, in_stock=True, category=cat3)

session.add(p1)
session.add(p2)
session.add(p3)
session.add(p4)
session.add(p5)

session.commit()


# задача 2
print("=== категории и продукты ===")
cats = session.query(Category).all()
for cat in cats:
    print(f"категория: {cat.name}")
    for p in cat.products:
        print(f"  - {p.name}: {p.price}")


# задача 3
smartphone = session.query(Product).filter(Product.name == "Смартфон").first()
smartphone.price = 349.99
session.commit()
print(f"\nновая цена смартфона: {smartphone.price}")


# задача 4
print("\n=== кол-во продуктов в категории ===")
res = session.query(Category.name, func.count(Product.id)).join(Product, Category.id == Product.category_id).group_by(Category.id).all()
for cat_name, count in res:
    print(f"  {cat_name}: {count}")


# задача 5
print("\n=== категории где больше 1 продукта ===")
res2 = session.query(Category.name, func.count(Product.id)).join(Product, Category.id == Product.category_id).group_by(Category.id).having(func.count(Product.id) > 1).all()
for cat_name, count in res2:
    print(f"  {cat_name}: {count}")


session.close()