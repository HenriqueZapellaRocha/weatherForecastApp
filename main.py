import requests
import ApiException
from database import DataBase

db = DataBase.getInstance()

print(db)
db.updateToken("32156")