import customtkinter as ctk
import tkinter as tk
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import numpy as np
import os

# Supported modes : Light, Dark, System
ctk.set_appearance_mode('dark')
# Supported themes : green, dark-blue, blue
ctk.set_default_color_theme("green")   

appWidth, appHeight = 900, 880


# App Class
class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("GUI Application")
        self.geometry(f"{appWidth}x{appHeight}")
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)
        self.appearanceVar = tk.StringVar(self)
        self.themeVar = tk.StringVar(self)
        self.modelVar = tk.StringVar(self)
        self.minsize(840, 300)
        font = ctk.CTkFont(family='arial', size=18)
        fontTitle = ctk.CTkFont(family='arial', size=22, slant='roman')
        canvasScreen = ctk.CTkCanvas(self, width = 350, height = 350)
        canvasScreen.create_line(300,300,300,300)

        # File selection button
        self.fileButton = ctk.CTkButton(self,
                                        text = 'Choose Image', font=font, command=self.selectFile)
        self.fileButton.grid(row=0, rowspan=2, column=0, columnspan=2, 
                            padx=50, 
                            pady=30, ipady = 15,
                            sticky="nw")
 
        # Image Label
        # self.imageLabel = ctk.CTkLabel(self,
        #                             text="Chosen image")
        # self.imageLabel.grid(row=2, column=0,
        #                       padx=20, pady=0,
        #                       sticky="w")
 
        # Blindness Label
        self.blindnessLabel = ctk.CTkLabel(self,
                                    text="Blindness type", font=fontTitle)
        self.blindnessLabel.grid(row=0, column=0, columnspan = 1,
                                padx=50, 
                                pady=120,
                                sticky="nw")

 
        # Blindness Radio Buttons
        self.blindnessVar = tk.StringVar(value="Normal")
 
        self.deuRadioButton = ctk.CTkRadioButton(self,
                                  text="Deuteranopia", font=font,
                                  variable=self.blindnessVar,
                                            value="He is")
        self.deuRadioButton.grid(row=0, column=0, columnspan=3, 
                                padx=50, 
                                pady=160,
                                sticky="nw")
 
        self.triRadioButton = ctk.CTkRadioButton(self,
                                      text="Tritanopia", font=font,
                                      variable=self.blindnessVar,
                                      value="She is")
        self.triRadioButton.grid(row=0, column=0, columnspan=3, 
                                padx=50, 
                                pady=200,
                                sticky="nw")
         
        self.monRadioButton = ctk.CTkRadioButton(self,
                                    text="Monochromacy", font=font,
                                    variable=self.blindnessVar,
                                            value="They are")
        self.monRadioButton.grid(row=0, column=0, columnspan=3, 
                                padx=50, 
                                pady=240,
                                sticky="nw")
 
  
        # Occupation Label
        self.occupationLabel = ctk.CTkLabel(self,
                                            text="Object Selection", font=font,)
        self.occupationLabel.grid(row=0, column=0, columnspan=3, 
                                padx=50,
                                pady=320,
                                sticky="nw")
 
        # Obj drop box
        self.objOptionMenu = ctk.CTkOptionMenu(self,
                                        values=["None"], font=font,)
        self.objOptionMenu.grid(row=0, column=0, columnspan=3, 
                                        padx=50,
                                        pady=360,
                                        sticky="nw")
 
        # Generate Button
        self.generateResultsButton = ctk.CTkButton(self,
                                         text="Generate Results", font=font,)
        self.generateResultsButton.grid(row=0, column=0, columnspan=3, 
                                        padx=50, 
                                        pady=480, ipady = 15,
                                        sticky="nw")

 
        # Generate Button
        self.generateResultsButton = ctk.CTkButton(self,
                                         text="Generate Results", font=font,)
        self.generateResultsButton.grid(row=0, column=0, columnspan=3, 
                                        padx=50, 
                                        pady=480, ipady = 15,
                                        sticky="nw")    

        # Appearance
        self.appearanceLabel = ctk.CTkLabel(self,
                                    text="Appearance", font=font)
        
        self.appearanceLabel.grid(row=0, column=0, columnspan = 1,
                                padx=50, 
                                pady=580,
                                sticky="nw")
        
        self.appearanceOptionMenu = ctk.CTkOptionMenu(self,
                                        values=["System", "Light", "Dark"], 
                                        variable = self.appearanceVar, font=font,
                                        command=self.selectAppearance)

        self.appearanceOptionMenu.grid(row=0, column=0, columnspan=3, 
                                        padx=50,
                                        pady=620,
                                        sticky="nw")
        
        # Theme
        self.themeLabel = ctk.CTkLabel(self,
                                    text="Theme", font=font)
        
        self.themeLabel.grid(row=0, column=0, columnspan = 1,
                                padx=50, 
                                pady=660,
                                sticky="nw")
        
        self.themeOptionMenu = ctk.CTkOptionMenu(self,
                                        values=["green", "dark-blue", "blue"], 
                                        variable = self.themeVar, font=font,
                                        command=self.selectTheme)

        self.themeOptionMenu.grid(row=0, column=0, columnspan=3, 
                                        padx=50,
                                        pady=700,
                                        sticky="nw")
        
        # Model Select and install https://imageai.readthedocs.io/en/latest/detection/ https://github.com/OlafenwaMoses/ImageAI/releases
        
        self.themeLabel = ctk.CTkLabel(self,
                                    text="Model Settings", font=font)
        
        self.themeLabel.grid(row=0, column=0, columnspan = 1,
                                padx=50, 
                                pady=780,
                                sticky="nw")
        
        self.modelInstallButton = ctk.CTkButton(self, text="Download models",
                                                command=self.downloadModels)
        
        self.modelInstallButton.grid(row=0, column=0, columnspan=3, 
                                        padx=50,
                                        pady=820,
                                        sticky="nw")
        
        self.modelOptionMenu = ctk.CTkOptionMenu(self,
                                        values=["RetinaNet", "YOLOv3", "TinyYOLOv3"], font=font, variable = self.modelVar, command=self.modelSelect) 
        
        self.modelOptionMenu.grid(row=0, column=0, columnspan=3, 
                                        padx=50,
                                        pady=860,
                                        sticky="nw")
 
    def downloadModels(self):
        os.system('models\install.bat')
    
    def modelSelect(self, modelVar):
        if modelVar == 'RetinaNet':
            pass
    
    def selectAppearance(self, appearanceVar):
        ctk.set_appearance_mode(appearanceVar)

    def selectTheme(self, themeVar):
        ctk.set_default_color_theme(themeVar)

    def selectFile(self):
        global filePath
        filePath = filedialog.askopenfilename(filetypes=[("PNG files", "*.png"), ('JPEG files', "*.jpg"), ('JPEG files', "*.jpeg")])
        if filePath:
            img = Image.open(filePath)
            
            if 1700 > img.size[0]:
                resX = img.size[0]
            elif 1700 <= img.size[0]:
                resX = 1700
            if 500 > img.size[1]:
                resY = img.size[1]
            elif 500 <= img.size[1]:
                resY = 500
            
            originalImage = ctk.CTkImage(img, size=(resX ,resY))
            self.originalImageLabel = ctk.CTkLabel(self, image=originalImage, 
                                                   height= 10, width= 10)
            self.originalImageLabel.grid(row=0, column=1,
                                         padx = 0, 
                                         pady = 0, ipadx = 2/self.winfo_height(),
                                         sticky='n')
            return filePath

if __name__ == "__main__":
    app = App()
    app.mainloop()