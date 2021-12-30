
from typing import List
from fastapi import FastAPI
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from src import database, models, schemas
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import Page, add_pagination, paginate

def get_db():
   db = database.SessionLocal()
   try:
       yield db
   finally:
       db.close()

app = FastAPI()

origins = [
    "http://127.0.0.1:4200",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/products", response_model=Page[schemas.Product])
def getAllProducts(db: Session = Depends(get_db)):
    products = db.query(models.Product).all()
    return paginate(products)

@app.get("/products/{id}", response_model=schemas.Product)
def getAProduct(id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).get(id)
    return product


add_pagination(app)

