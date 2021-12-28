import sys
import json
from src import database, models

# Drop all tables
for t in database.Base.metadata.sorted_tables:
    t.drop(database.engine, checkfirst=True)
# Create all needed tables
database.Base.metadata.create_all(bind=database.engine)

db = database.SessionLocal()

with open(sys.argv[1]) as json_file:
    data = json.load(json_file)
    for p in data["Products"]:
        product = models.Product(id=int(p['Id']), name=p['Title'], image_url=p["ImageUrl"], price=p["Price"], description=p["Description"])
        db.add(product)
    db.commit()
    print("Database initialization done")