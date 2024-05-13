import requests
import ApiException
from database import DataBase

db = DataBase.getInstance()

print(db)
db.insterToken( "1234")
db.updateToken("32156")
db.getToken()
db.instertCity("porto alegre", 2540)