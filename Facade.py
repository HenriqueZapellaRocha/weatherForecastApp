from ApiCommunication import * 
from database import DataBase

#verify the existence of token in db
def verifyExistingToken() -> bool:
    if DataBase.getInstance().getToken() == None:
        return False
    else: 
        return True

#insert a token in db
def insertTokenInDb(token: str):
    if verifyExistingToken() == False:
        DataBase.getInstance().insterToken(token)