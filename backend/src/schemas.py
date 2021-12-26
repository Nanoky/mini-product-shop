
from pydantic import BaseModel

class Product (BaseModel):
    id: int
    name: str
    price: int
    image_url: str
    description: str

    class Config:
        orm_mode = True