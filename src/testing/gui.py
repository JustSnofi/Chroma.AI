#imports
import tkinter as tk
import customtkinter as ctk

#window sets
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme("dark-blue")   

#window sizes
appWidth, appHeight = 700, 680

#Home page
class Home(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("ChromAi - color blind helper")
        self.resizable(False,False)
        self.geometry(f"{appWidth}x{appHeight}")
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)
        # self.minsize(700, 680)
        font = ctk.CTkFont(family='arial', size=20)
        fontTitle = ctk.CTkFont(family='arial', size=65, slant='roman')

        # ChromaAi Title
        self.appearanceLabel = ctk.CTkLabel(self,
                                    text="ChromAi", font=fontTitle)
        
        self.appearanceLabel.grid(row=0, column=0, 
                                        padx=5,
                                        pady=0, ipadx = 200, ipady = 35,
                                        sticky="nw")

        # Start Button
        self.startButton = ctk.CTkButton(self,
                                         text="Start", font=font)
        self.startButton.grid(row=0, column=0, columnspan=3, 
                                        padx=250, 
                                        pady=190, ipadx = 40, ipady = 30,
                                        sticky="nw")
        
        # settings Button
        self.settingsButton = ctk.CTkButton(self,
                                        text="Settings", font=font,command=setting_open)
        self.settingsButton.grid(row=0, column=0, columnspan=3, 
                                        padx=250, 
                                        pady=300, ipadx = 40, ipady = 30,
                                        sticky="nw")  

        # About us Button
        self.weButton = ctk.CTkButton(self, 
                                        text="About us", font=font, width=50, height=20,command=About_us_open)
        self.weButton.grid(row=0, column=0, 
                                        padx=5, 
                                        pady=15,
                                        sticky="sw")


#Settings page
class Settings(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("ChromAi - Settings")
        self.resizable(False,False)
        self.geometry(f"{appWidth}x{appHeight}")
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)
        # self.minsize(700, 680)
        font = ctk.CTkFont(family='arial', size=20)
        fontTitle = ctk.CTkFont(family='arial', size=65, slant='roman')

        # ChromaAi Title
        self.appearanceLabel = ctk.CTkLabel(self,
                                    text="Settings", font=fontTitle)
        
        self.appearanceLabel.grid(row=0, column=0, 
                                        padx=5,
                                        pady=0, ipadx = 200, ipady = 35,
                                        sticky="nw")

         
#About us page
class About_us(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("ChromAi - About us")
        self.resizable(False,False)
        self.geometry("400x400")
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)
        # self.minsize(700, 680)
        font = ctk.CTkFont(family='arial', size=20)
        fontTitle = ctk.CTkFont(family='arial', size=45, slant='roman')

        # ChromaAi Title
        self.appearanceLabel = ctk.CTkLabel(self,
                                    text="About us", font=fontTitle)
        
        self.appearanceLabel.grid(row=0, column=0, 
                                        padx=5,
                                        pady=0, ipadx = 20, ipady = 20,
                                        sticky="nw")

#runers
if __name__ == "__main__":
    settings = Settings()

if __name__ == "__main__":
    we = About_us()

def About_us_open():
    we.mainloop()

def setting_open():
    home.destroy()
    settings.mainloop()

if __name__ == "__main__":
    home = Home()
    home.mainloop()



