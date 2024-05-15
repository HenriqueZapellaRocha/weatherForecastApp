from tkinter import *
from customtkinter import *
from PIL import Image
from Facade import *


def updateInformations(textImage,mainScreen, cityComboBox, frameWeather):
    #update the text in the label 
    result = currentWeatherr(cityComboBox.get())
    
    if result != None:
        image =CTkImage(light_image=Image.open("Icons/"+str(result['icon'])+".png"),
                dark_image=Image.open("Icons/"+str(result['icon'])+".png"),
                size=(50,50))
        print(result)
        textImage.configure(text=str(result['temperature'])+"c°")
        textImage.configure(image=image)
        frameWeather.place(x=53, y=120)
        textImage.place(x=215, y =0)
        #update the GUI
        mainScreen.update()
        print("passed")

def mainScreenGUI():
    mainScreen = CTk()

    mainScreen.title("weather app")
    larguraDaTela= mainScreen.winfo_screenwidth()
    alturaDaTela= mainScreen.winfo_screenheight()
    x = (larguraDaTela - 700) // 2
    y = (alturaDaTela - 700) // 3
    mainScreen.geometry(f"{700}x{700}+{x}+{y}")
    mainScreen.resizable(width=False, height=False)


    cititesText = CTkLabel(mainScreen, 
                        font=("San Francisco", 15),
                        text="Chossen the city")
    cititesText.pack()
    cities = getAllCtitiesInDb() 
    cityComboBox = CTkComboBox(mainScreen, 
                            values=cities)


    cityComboBox.set("")
    cityComboBox.pack(pady=5)

    citieChoiceConfButton = CTkButton(mainScreen, 
                                    text="send",
                                    command=lambda: updateInformations(textImage, mainScreen, cityComboBox, frameWeather)) 
    citieChoiceConfButton.pack()


    frameWeather = CTkFrame(mainScreen, width=600, height= 550)
    
    frameWeather.place_forget()

    textImage = CTkLabel(frameWeather, 
                    text=" -0c°",
                    font=("San Francisco", 70),
                    image=None,
                    compound="bottom",
                    padx=4
                    )
    textImage.place_forget()

    mainScreen.mainloop()
