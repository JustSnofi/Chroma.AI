import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import numpy as np
import os
import detection as dt
from time import sleep
from requests import get
import threading

# Supported modes : Light, Dark, System
ctk.set_appearance_mode('dark')
# Supported themes : green, dark-blue, blue
ctk.set_default_color_theme("green")  

links = [
    'https://github.com/OlafenwaMoses/ImageAI/releases/download/3.0.0-pretrained/retinanet_resnet50_fpn_coco-eeacb38b.pth/',
    'https://github.com/OlafenwaMoses/ImageAI/releases/download/3.0.0-pretrained/yolov3.pt/',
    'https://github.com/OlafenwaMoses/ImageAI/releases/download/3.0.0-pretrained/tiny-yolov3.pt/'
]

destinations = [
    'models/RetinaNet.pth',
    'models/YoloV3.pt',
    'models/TinyYoloV3.pt'
]

objValues = ['None']

appName = 'Chroma.AI'

appLogoPath = r'img\app\icon.ico'

newFilePath = r'output\output.jpg'

modelsCount = 0

appWidth, appHeight = 1000, 1000

class Loading(ctk.CTk):
    def __init__(self, *args, **kwargs):
        global modelsCount
        super().__init__(*args, **kwargs)
        self.title(appName + "- Loading")
        self.iconbitmap(appLogoPath)
        self.resizable(False,False)
        self.geometry("700x680")
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)
        self.countingVar = ctk.StringVar()
        self.countingVar.set(f'{modelsCount} Models downloaded out of 3')
        # self.minsize(700, 680)
        font = ctk.CTkFont(family='arial', size=20)
        fontTitle = ctk.CTkFont(family='arial', size=65, slant='roman')

        self.appearanceLabel1 = ctk.CTkLabel(self,
                                    text="Loading...", font=fontTitle)
        
        self.appearanceLabel1.grid(row=0, column=0, 
                                        padx=5,
                                        pady=0, ipadx = 200, ipady = 35,
                                        sticky="nw")
        
        self.appearanceLabel2 = ctk.CTkLabel(self, text='Loading, we will finish shortly after...', font=font)
        self.appearanceLabel2.grid(row = 1, column = 0)

        self.modelCountingLabel = ctk.CTkLabel(self, text=self.countingVar.get(), font=font)
        self.modelCountingLabel.grid(row = 2, column = 0 , sticky = 's')
        
        # for path in os.listdir('models/'):
        #     if os.path.isfile(os.path.join('models/', path)):
        #         modelsCount += 1
        # while modelsCount != 4:
        #     thread1 = threading.Thread(target=downloadModels)
        #     thread1.start()
        # else:
        #     self.destroy
        #     Main.mainloop(self)

        def downloadModels():
            '''Downloads and Checks if models exist.'''
            global modelsCount

            for path in os.listdir('models/'):
            # check if current path is a file
                if os.path.isfile(os.path.join('models/', path)):
                    modelsCount += 1

            if modelsCount == 4:
                self.after(0, homeOpen)
            elif modelsCount != 4:
                for link, destination in zip(links, destinations):
                    print('downloading')
                    download_file(link, destination)
                    modelsCount += 1
                    print('downloaded')
                    if modelsCount == 4:
                        self.after(0, homeOpen)


        thread1 = threading.Thread(target=downloadModels)
        thread1.start()

            
            
        


    

class Home(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # !!!Tried to set background as an image - didnt work!!!
        # homeBG = ctk.CTkImage(Image.open('img\icon_bg.png'))
        # self.backgroundLabel = ctk.CTkLabel(self, image=homeBG)
        # self.backgroundLabel.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.title(appName + " - color blind helper")
        self.iconbitmap(appLogoPath)
        self.resizable(False,False)
        self.geometry("700x680")
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)
        # self.minsize(700, 680)
        font = ctk.CTkFont(family='arial', size=20)
        fontTitle = ctk.CTkFont(family='arial', size=65, slant='roman')

        # ChromaAi Title
        self.appearanceLabel = ctk.CTkLabel(self,
                                    text=appName, font=fontTitle)
        
        self.appearanceLabel.grid(row=0, column=0, 
                                        padx=5,
                                        pady=0, ipadx = 200, ipady = 35,
                                        sticky="nw")

        # Start Button
        self.startButton = ctk.CTkButton(self,
                                         text="Start", font=font, command=mainOpen)
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
                                        text="About us", font=font, width=50, height=20,command=about_usOpen)
        self.weButton.grid(row=0, column=0, 
                                        padx=5, 
                                        pady=15,
                                        sticky="sw")


#Settings page
class Settings(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title(appName + "- Settings")
        self.iconbitmap(appLogoPath)
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
class AboutUs(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("ChromAi - About us")
        self.iconbitmap(appLogoPath)
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

# Main Window Class
class Main(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title(appName)
        self.iconbitmap(appLogoPath)
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
                                        values=objValues, font=font,)
        self.objOptionMenu.grid(row=0, column=0, columnspan=3, 
                                        padx=50,
                                        pady=360,
                                        sticky="nw")
 
        # Generate Button
        self.generateResultsButton = ctk.CTkButton(self,
                                         text="Generate Results", font=font, command=self.renderImage)
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
        
        self.modelOptionMenu = ctk.CTkOptionMenu(self,
                                        values=["RetinaNet", "YOLOv3", "TinyYOLOv3"], font=font, variable = self.modelVar, command=self.modelSelect) 
        
        self.modelOptionMenu.grid(row=0, column=0, columnspan=3, 
                                        padx=50,
                                        pady=860,
                                        sticky="nw")
 
    def modelSelect(self, modelVar):
        if modelVar == 'RetinaNet':
            return 'models\retinanet_resnet50_fpn_coco-eeacb38b.pth'
        if modelVar == 'YOLOv3':
            return 'models\yolov3.pt'
        if modelVar == 'TinyYOLOv3':
            return 'models\tiny-yolov3.pt'
    
    def selectAppearance(self, appearanceVar):
        ctk.set_appearance_mode(appearanceVar)

    def selectTheme(self, themeVar):
        ctk.set_default_color_theme(themeVar)

    def selectFile(self):
        global resX, resY, originalImage, filePath
        filePath = filedialog.askopenfilename(filetypes=[("PNG files", "*.png"), ('JPEG files', "*.jpg"), ('JPEG files', "*.jpeg")])
        img = Image.open(filePath)
        if filePath:
            if 1700 > img.size[0]:
                resX = img.size[0]
            elif 1700 <= img.size[0]:
                resX = 1700
            if 470 > img.size[1]:
                resY = img.size[1]
            elif 470 <= img.size[1]:
                resY = 470
            
        originalImage = ctk.CTkImage(img, size=(resX ,resY))
        self.originalImageLabel = ctk.CTkLabel(self, image=originalImage, height=10, width=10)
        self.originalImageLabel.grid(row=0, rowspan = 1,
                                     column=1, columnspan = 2,
                                     sticky='n')
        
    def renderImage(self):
        dt.RetinaNet(filePath)
        
        newImg = Image.open(newFilePath)    
        newImg = ctk.CTkImage(newImg, size=(resX ,resY))
        self.newImageLabel = ctk.CTkLabel(self, image=newImg, 
                                          height= 10, width= 10)

        self.newImageLabel.grid(row=0, rowspan = 1,
                                column=1, columnspan = 2,
                                padx = 0, 
                                pady = resY + 20,
                                sticky='n')

def download_file(url, destination):
    response = get(url)
    with open(destination, 'wb') as file:
        file.write(response.content)

def RetinaNet():
    thread2 = dt.RetinaNet(filePath)
    thread2.start()
    thread2.join()


def about_usOpen():
    about_us.mainloop()

def setting_open():
    home.destroy()
    settings.mainloop()

def mainOpen():
    home.destroy()
    main.mainloop()

def homeOpen():
    loading.destroy()
    home.mainloop()

if __name__ == "__main__":
    '''
    
    !!!README!!! : main = Main() needs to be always at the top or it will cause a bug
    
    '''
    main = Main()
    home = Home()
    loading = Loading()
    settings = Settings()
    about_us= AboutUs()

    loading.mainloop()



