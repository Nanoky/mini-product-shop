from sqlalchemy import Column, Integer, String
from .database import Base

class Product(Base):
    __tablename__ = "product_table"

    id = Column("product_id", Integer(), autoincrement=False, nullable=False, primary_key=True)
    name = Column("product_name", String(100), nullable=False)
    price = Column("product_price", Integer(), nullable=False, default=0)
    image_url = Column("product_image_url", String(1000), nullable=False)
    description = Column("product_description", String(500), nullable=False)