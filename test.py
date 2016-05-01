import database
from app_init import app, api, db

try:
    db.drop_all()
    db.create_all()


except Exception as e:
    print(e)