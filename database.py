import sqlite3
from sqlite3 import Cursor

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
        return response.fetchone()[0]
    
    def instertCity(self, cityName:str, cityId: int):
        self.pointer.execute("INSERT INTO CITIES VALUES (?, ?)", (cityName, cityId))
        self.connection.commit()