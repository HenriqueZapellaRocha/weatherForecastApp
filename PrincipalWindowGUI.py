from tkinter import *
from customtkinter import *
from PIL import Image

def mainScreenGUI():
    mainScreen = CTk()

    mainScreen.title("weather app")
    larguraDaTela= mainScreen.winfo_screenwidth()
    alturaDaTela= mainScreen.winfo_screenheight()
    x = (larguraDaTela - 700) // 2
    y = (alturaDaTela - 700) // 3
    mainScreen.geometry(f"{700}x{700}+{x}+{y}")
    mainScreen.resizable(width=False, height=False)


    #AQUI TORNA VISIVEL O FRAME 
    def mostrar_selecao():
        print(cityComboBox.get())


    cititesText = CTkLabel(mainScreen, 
                        font=("San Francisco", 15),
                        text="Chossen the city")
    cititesText.pack()
    cities = ["Porto Alegre", "Sao Paulo"] # MUDAR PARA RESULTADO DE CONSULTA AO BANCO DE DADOS
    cityComboBox = CTkComboBox(mainScreen, 
                            values=cities)


    cityComboBox.set("")
    cityComboBox.pack(pady=5)

    citieChoiceConfButton = CTkButton(mainScreen, 
                                    text="send",
                                    command=mostrar_selecao) 
    citieChoiceConfButton.pack()


    frameWeather = CTkFrame(mainScreen, width=600, height= 550)
    frameWeather.place(x=53, y=120)
    citieChoiceConfButton2 = CTkButton(frameWeather, 
                                    text="send",
                                    command=mostrar_selecao) 

    image =CTkImage(light_image=Image.open("/Users/henriquezapellarocha/Downloads/realistic/200px/1.png"),
                    dark_image=Image.open("/Users/henriquezapellarocha/Downloads/realistic/200px/1.png"),
                    size=(50,50))

    textImage = CTkLabel(frameWeather, 
                    text=" -0 C°",
                    font=("San Francisco", 70),
                    image=image,
                    compound="bottom",
                    padx=4
                    )
    textImage.place(x=215, y =0)

    mainScreen.mainloop()
