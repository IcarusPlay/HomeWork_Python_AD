from sqlalchemy import create_engine, Column, Integer, String, Numeric, Boolean, ForeignKey
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

    # Задача 5: связь с Category
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship("Category", back_populates="products")


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


category1 = Category(name="Electronics", description="Electronic devices and gadgets")
category2 = Category(name="Food", description="Food and beverages")

product1 = Product(name="Laptop", price=999.99, in_stock=True, category=category1)
product2 = Product(name="Phone", price=499.99, in_stock=True, category=category1)
product3 = Product(name="Apple", price=0.99, in_stock=False, category=category2)

session.add(category1)
session.add(category2)
session.add(product1)
session.add(product2)
session.add(product3)

session.commit()


print(*[product.name for product in category1.products], sep='\n')
print(product3.category.name)

session.close()