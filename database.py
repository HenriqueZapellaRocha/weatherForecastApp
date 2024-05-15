import sqlite3
from sqlite3 import Cursor
from typing import Tuple

class DataBase:
    __instance = None
    
    #get a instance of the class(singleton pattern)
    @staticmethod
    def getInstance():
        if DataBase.__instance == None:
            DataBase.__instance = DataBase()
           
        return DataBase.__instance
    
    #constructor from the class
    def __init__(self):
            self.connection = sqlite3.connect("data.db")
            self.pointer = self.connection.cursor()
            self.__createTables(self.pointer)
 
    #if the db does not exist, creates the tables
    def __createTables(self,pointer: Cursor) -> bool:
        pointer.execute("CREATE TABLE IF NOT EXISTS TOKENS(token TEXT)")
        pointer.execute("CREATE TABLE IF NOT EXISTS CITIES(name TEXT, id INTEGER)")
        return True
    
    #insert the toke in db
    def insterToken(self, tokens: str):
        self.pointer.execute("INSERT INTO TOKENS VALUES (?)",(tokens,))
        self.connection.commit()
        
    #update toke in db
    def updateToken(self, newToken: str):
        for row in self.pointer.execute("SELECT token FROM TOKENS"):
            self.pointer.execute("UPDATE TOKENS SET token = ? WHERE token = ? ", (newToken, row[0]))
        self.connection.commit()
        
    #get the api token from db 
    def getToken(self) -> str:
        response = self.pointer.execute("SELECT token FROM TOKENS")
        result = response.fetchone()
        if result is not None:
            return result[0]
        else:
            return None
    
    #insert a new city in db
    def instertCity(self, cityName:str, cityId: int):
        self.pointer.execute("INSERT INTO CITIES VALUES (?, ?)", (cityName, cityId))
        self.connection.commit()
    
    #get the id of a city by the city name
    def getCityId(self,cityName: str) -> int:
        response = self.pointer.execute("SELECT id FROM CITIES WHERE name = ?", (cityName,))
        result = response.fetchone()
        if result is not None:
            return result
        else:
            return None
        
    def getCityName(self,cityId: int) -> str:
        response = self.pointer.execute("SELECT id FROM CITIES WHERE id = ?", (cityId,))
        result = response.fetchone()
        if result is not None:
            return result[0]
        else:
            return None        
    
    def getCities(self) -> Tuple:
        response = self.pointer.execute("SELECT name FROM CITIES")
        result = response.fetchone()
        if result is not None:
            return result
        else:
            return None
        
    def isTheCityOnDb(self, cityName: str) -> bool:
        response = self.pointer.execute("SELECT name FROM CITIES WHERE name = ", (cityName,))
        result = response.fetchone()
        if result is not None:
            return True
        else:
            return False
        
        