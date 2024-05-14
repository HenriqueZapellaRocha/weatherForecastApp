from Facade import *
from tkinter import *
from customtkinter import * 
import webbrowser
import TokenGUI
import PrincipalWindowGUI

DataBase.getInstance().instertCity("Sao Paulo", 3477)

def principalWindow():
    print("im in princioapl")
    PrincipalWindowGUI.mainScreenGUI()

#verify if exist any token in db, case not a window start to put this information
if verifyExistingToken() == False:
    TokenGUI.tokenGUI()


principalWindow()
    
