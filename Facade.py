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

def currentWeatherr(cityName: str):
    
    token = DataBase.getInstance().getToken()
    cityId = DataBase.getInstance().getCityId(cityName)[0]
    
    if token and cityId != None:
        return currentWeather(token, cityId)
    else:
        None

def updateCitiesFromApiToDb():
    token = DataBase.getInstance().getToken()
    result = verifyCitiesAddedInApi(token)
    for id in result:
        DataBase.getInstance().instertCity(nameCityByiD(token, id), id)

def getAllCtitiesInDb():
    return DataBase.getInstance().getCities()