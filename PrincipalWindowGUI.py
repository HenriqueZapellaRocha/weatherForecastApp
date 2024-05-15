from tkinter import *
from customtkinter import *
from PIL import Image
from Facade import *


def updateInformations(textImage,mainScreen, cityComboBox, frameWeather, condition, sensation):
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
        textImage.place(x=230, y =0)
        condition.configure(text=str(result['condition']))
        condition.place(x=140, y=130)
        sensation.configure(text="sensação: "+str(result['sensation'])+"c°")
        sensation.place(x=215, y=170)
        #update the GUI
        mainScreen.update()
        print("passed")

def mainScreenGUI():
    mainScreen = CTk()

    mainScreen.title("weather app")
    larguraDaTela= mainScreen.winfo_screenwidth()
    alturaDaTela= mainScreen.winfo_screenheight()
    x = (larguraDaTela - 700) // 2
    y = (alturaDaTela - 400) // 3
    mainScreen.geometry(f"{700}x{400}+{x}+{y}")
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
                                    command=lambda: updateInformations(textImage, mainScreen, cityComboBox, frameWeather, condition, sensation)) 
    citieChoiceConfButton.pack()


    frameWeather = CTkFrame(mainScreen, width=600, height= 230)
    
    frameWeather.place_forget()

    textImage = CTkLabel(frameWeather, 
                    text=" -0c°",
                    font=("San Francisco", 70),
                    image=None,
                    compound="bottom",
                    padx=4
                    )
    textImage.place_forget()
    
    condition = CTkLabel(frameWeather,
                         font=("San Francisco", 30))
    condition.place_forget()
    
    sensation= CTkLabel(frameWeather,
                         font=("San Francisco", 30))
    
    sensation.place_forget()
    
    mainScreen.mainloop()
