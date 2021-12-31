import json
from fastapi import FastAPI
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from src import database, models, schemas
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import Page, add_pagination, paginate


# Drop all tables
for t in database.Base.metadata.sorted_tables:
    t.drop(database.engine, checkfirst=True)
# Create all needed tables
database.Base.metadata.create_all(bind=database.engine)

db = database.SessionLocal()

with open("products.json") as json_file:
    data = json.load(json_file)
    for p in data["Products"]:
        product = models.Product(id=int(p['Id']), name=p['Title'], image_url=p["ImageUrl"], price=p["Price"], description=p["Description"])
        db.add(product)
    db.commit()
    print("Database initialization done")



def get_db():
   db = database.SessionLocal()
   try:
       yield db
   finally:
       db.close()

app = FastAPI()

origins = [
    "http://127.0.0.1:8080",
    "http://localhost:8080",
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

