import json
from typing import List
from fastapi import FastAPI
from fastapi.param_functions import Depends
from sqlalchemy.orm import load_only
from sqlalchemy.orm.session import Session
from src import database, models, schemas
from fastapi.middleware.cors import CORSMiddleware

# Create all required table if needed
database.Base.metadata.create_all(bind=database.engine)

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

@app.get("/products", response_model=List[schemas.Product])
def getAllProducts(db: Session = Depends(get_db)):
    products = db.query(models.Product).all()
    return products

@app.get("/products/{id}", response_model=schemas.Product)
def getAProduct(id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).get(id)
    return product

@app.get("/load")
async def loadData(db: Session = Depends(get_db)):
    with open("data_source.json") as json_file:
        data = json.load(json_file)
        for p in data:
            product = models.Product(id=p['Product ID'], name=p['Name'], image_url=p["Thumbnail URL"], price=p["Price"], description=p["Description"])
            db.add(product)
        db.commit()



