from ApiCommunication import * 
from database import DataBase

def verifyExistingToken() -> bool:
    if DataBase.getInstance().getToken() == None:
        return False
    else: 
        return True

def insertTokenInDb(token: str):
    if verifyExistingToken() == False:
        DataBase.getInstance().insterToken(token)