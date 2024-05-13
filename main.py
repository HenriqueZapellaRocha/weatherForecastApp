import requests
import ApiException
from database import DataBase 
from ApiCommunication import *
from Facade import *

db = DataBase.getInstance()

print(db)

if verifyExistingToken() == True:
    print("dint")
else:
    insertTokenInDb('1234')