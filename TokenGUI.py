from tkinter import *
from customtkinter import * 
import webbrowser
from Facade import insertTokenInDb

set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
set_appearance_mode("system")

#case click label 3 the link for the api token creation open
def open_link(event):
    webbrowser.open("https://advisor.climatempo.com.br")
    #insert the token in the db getitng the information in the entry 
def getToken(window, entry):
    insertTokenInDb(entry.get())
    window.destroy()
    return

def tokenGUI():
    # setting our window
    window = CTk()
    window.title("weather app")
    larguraDaTela= window.winfo_screenwidth()
    alturaDaTela= window.winfo_screenheight()
    x = (larguraDaTela - 400) // 2
    y = (alturaDaTela - 400) // 3
    window.geometry(f"{400}x{200}+{x}+{y}")
    window.resizable(width=False, height=False)

    #widgets creation
    label1 = CTkLabel(window,
                    font=("San Francisco", 15),
                    text="We did not find an API token, please enter one:").grid(row=0, column=0, columnspan=2, pady=10) 


    entry = CTkEntry(window,
                    font=("San Francisco", 15),
                    placeholder_text="Entry Token",
                    width=280)
    entry.grid(row=1, column=0)

    button = CTkButton(window, 
                    font=("San Francisco", 15),
                    text="submit",
                    width=120,
                    command=lambda: getToken(window, entry)).grid(row=1, column=1, pady=5)

    label2 = CTkLabel(window,
                    font=("San Francisco", 10),
                    text="Please check the link below if you don't have an API token.").grid(row=3, column=0, columnspan=2)

    label3 = CTkLabel(window,
                    font=("San Francisco", 10),
                    text="https://advisor.climatempo.com.br", cursor="hand2", text_color="blue")

    #bind to make the label 3 clickable, case the user fucntion open_link is called
    label3.bind("<Button-1>", lambda event: open_link(event))

    label3.place(relx=0.5, rely=0.6, anchor="center", y=10)
    
    window.mainloop()