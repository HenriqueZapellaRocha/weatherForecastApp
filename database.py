import sqlite3
from sqlite3 import Cursor
class DataBase:
    __instance = None
    
    
    @staticmethod
    def getInstance():
        if DataBase.__instance == None:
            DataBase.__instance = DataBase()
           
        return DataBase.__instance
       
    def __init__(self):
            self.connection = sqlite3.connect("data.db")
            self.pointer = self.connection.cursor()
            self.createTables(self.pointer)
 
        
    def createTables(self,pointer: Cursor) -> bool:
        
        pointer.execute("CREATE TABLE IF NOT EXISTS TOKENS(token TEXT)")
        pointer.execute("CREATE TABLE IF NOT EXISTS CITIES(name TEXT, id INTEGER)")

        return True
    
    def insterToken(self, tokens: str):
        self.pointer.execute("INSERT INTO TOKENS VALUES (?)",(tokens,))
        self.connection.commit()

    def updateToken(self, newToken: str):
        for row in self.pointer.execute("SELECT token FROM TOKENS"):
            self.pointer.execute("UPDATE TOKENS SET token = ? WHERE token = ? ", (newToken, row[0]))
        self.connection.commit()