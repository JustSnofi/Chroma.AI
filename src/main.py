<<<<<<< Updated upstream
'''

Chroma.Ai 
v0.2.3

'''

import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import numpy as np
import os
import detection as dt
from requests import get
import threading
import json
import userdata
import imgColoring
import cv2
import webbrowser


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

appName = 'Chroma.AI'

appLogoPath = r'img\app\icon.ico'

newFilePath = r'output\output.jpg'

modelsCount = 0

weURL = r'https://github.com/JustSnofi/Chroma.AI#readme'

appWidth, appHeight = 780, 780




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


        def downloadModels():
            '''Downloads and Checks if models exist.'''
            global modelsCount

            for path in os.listdir('models/'):
            # check if current path is a file
                if os.path.isfile(os.path.join('models/', path)):
                    modelsCount += 1

            if modelsCount == 4:
                self.after(0, loadingToHomeOpen)
            elif modelsCount != 4:
                for link, destination in zip(links, destinations):
                    print('downloading')
                    download_file(link, destination)
                    modelsCount += 1
                    print('downloaded')
                    if modelsCount == 4:
                        self.after(0, loadingToHomeOpen)


        thread1 = threading.Thread(target=downloadModels)
        thread1.start()
          


    
class Home(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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
                                         text="Start", font=font, command=homeToMainOpen)
        self.startButton.grid(row=0, column=0, columnspan=3, 
                                        padx=250, 
                                        pady=190, ipadx = 40, ipady = 30,
                                        sticky="nw")
        
        # Settings Button
        self.settingsButton = ctk.CTkButton(self,
                                        text="Settings", font=font,command=homeToSettingsOpen)
        self.settingsButton.grid(row=0, column=0, columnspan=3, 
                                        padx=250, 
                                        pady=300, ipadx = 40, ipady = 30,
                                        sticky="nw")  

        # About us Button
        self.weButton = ctk.CTkButton(self, 
                                        text="About us", font=font, 
                                        width=50, height=20,
                                        command=self.openURL)
        self.weButton.grid(row=0, column=0, 
                                        padx=5, 
                                        pady=15,
                                        sticky="sw")

    def openURL(self):
        webbrowser.open(weURL,new=1)





#Settings page
class Settings(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title(f"{appName} - Settings")
        self.iconbitmap(appLogoPath)
        self.resizable(False,False)
        self.geometry(f"{appWidth}x{appHeight}")
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)
        font = ctk.CTkFont(family='arial', size=20)
        fontTitle = ctk.CTkFont(family='arial', size=65, slant='roman')
        self.appearanceVar = tk.StringVar(self)
        self.themeVar = tk.StringVar(self)
        padx = 280

        # ChromaAi Title
        self.settingsLabel = ctk.CTkLabel(self,
                                    text=f"  {appName} \n Settings", font=fontTitle)
        
        self.settingsLabel.grid(row=0, column=0, 
                                        padx=220,
                                        pady=35,
                                        sticky="nw")
        
        # Appearance
        self.appearanceLabel = ctk.CTkLabel(self,
                                    text="Appearance \n Dark (Default)", font=font)
        
        self.appearanceLabel.grid(row=0, column=0, columnspan = 1,
                                padx=padx, 
                                pady=200,
                                sticky="nw")
        
        self.appearanceOptionMenu = ctk.CTkOptionMenu(self,
                                                    values=["System", "Light", "Dark"],
                                                    variable = self.appearanceVar, font=font,
                                                    command=self.selectAppearance)

        self.appearanceOptionMenu.grid(row=0, column=0, columnspan=3, 
                                        padx=padx,
                                        pady=280,
                                        sticky="nw")
        
        # Theme
        self.themeLabel = ctk.CTkLabel(self,
                                    text="Theme \n Green (Default)", font=font)
        
        self.themeLabel.grid(row=0, column=0, columnspan = 1,
                            padx=padx, 
                            pady=380,
                            sticky="nw")
        
        themeValues=["green", "dark-blue", "blue"]
        self.themeOptionMenu = ctk.CTkOptionMenu(self, values=themeValues,  
                                                variable = self.themeVar, font=font,
                                                command=self.selectTheme)

        self.themeOptionMenu.grid(row=0, column=0, columnspan=3, 
                                padx=padx,
                                pady=460,
                                sticky="nw")
        
        self.goToHomeButton = ctk.CTkButton(self, text='Home', font=font,
                                            command=settingsToHomeOpen)
        
        self.goToHomeButton.grid(row=0, column=0, columnspan=3, 
                                padx=padx,
                                pady=520,
                                sticky="nw")
        
        # Will be added in the next versions
        # self.fullscreenSwitch = ctk.CTkSwitch(self, variable=self.fullscreenVar, command=)
        
        
    def selectAppearance(self, appearanceVar):
        ctk.set_appearance_mode(appearanceVar)
        
    def selectTheme(self, themeVar):
        ctk.set_default_color_theme(themeVar)


# Main Window Class
class Main(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title(appName)
        self.iconbitmap(appLogoPath)
        self.geometry(f"{appWidth}x{appHeight}")
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)
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
        self.blindnessVar = tk.StringVar(value="None")
 
        self.deuRadioButton = ctk.CTkRadioButton(self,
                                  text="Deuteranopia", font=font,
                                  variable=self.blindnessVar, value='deuteranopia', 
                                  command=self.blindnessSelect)
        self.deuRadioButton.grid(row=0, column=0, columnspan=3, 
                                padx=50, 
                                pady=160,
                                sticky="nw")
 
        self.triRadioButton = ctk.CTkRadioButton(self,
                                      text="Tritanopia", font=font,
                                      variable=self.blindnessVar, value='tritanopia',
                                      command=self.blindnessSelect)
        self.triRadioButton.grid(row=0, column=0, columnspan=3, 
                                padx=50, 
                                pady=200,
                                sticky="nw")
         
        self.proRadioButton = ctk.CTkRadioButton(self,
                                    text="Protanopia", font=font,
                                    variable=self.blindnessVar, value='protanopia',
                                    command=self.blindnessSelect)
        self.proRadioButton.grid(row=0, column=0, columnspan=3, 
                                padx=50, 
                                pady=240,
                                sticky="nw")
        self.noneRadioButton = ctk.CTkRadioButton(self,
                                    text="None", font=font,
                                    variable=self.blindnessVar, value='None',
                                    command=self.blindnessSelect)
        self.noneRadioButton.grid(row=0, column=0, columnspan=3, 
                                padx=50, 
                                pady=280,
                                sticky="nw")
 
        # Generate Button
        self.generateResultsButton = ctk.CTkButton(self,
                                         text="Generate Results", font=font, command=self.renderImage)
        self.generateResultsButton.grid(row=0, column=0, columnspan=3, 
                                        padx=50, 
                                        pady=340, ipady = 15,
                                        sticky="nw") 
        
        
        # Model Select and install https://imageai.readthedocs.io/en/latest/detection/ https://github.com/OlafenwaMoses/ImageAI/releases
        
        self.modelLabel = ctk.CTkLabel(self,
                                    text="Model Settings", font=font)
        
        self.modelLabel.grid(row=0, column=0, columnspan = 1,
                            padx=50, 
                            pady=600,
                            sticky="nw")
        
        self.modelOptionMenu = ctk.CTkOptionMenu(self,
                                        values=["RetinaNet", "YOLOv3", "TinyYOLOv3"], font=font, variable = self.modelVar, command=self.modelSelect) 
        
        self.modelOptionMenu.grid(row=0, column=0, columnspan=3, 
                                        padx=50,
                                        pady=640,
                                        sticky="nw")
        
        self.goToSettingsButton = ctk.CTkButton(self, text='Home', 
                                                font=font, 
                                                command=mainToHomeOpen)
        
        self.goToSettingsButton.grid(row=0, column=0, columnspan=3, 
                                    padx=50,
                                    pady=700,
                                    sticky="nw")
        

    def blindnessSelect(self):
        value = self.blindnessVar.get()    
        if value == 'deuteranopia':
            userdata.saveBlindness('deuteranopia')
        elif value == 'tritanopia':
            userdata.saveBlindness('tritanopia')
        elif value == 'protanopia':
            userdata.saveBlindness('protanopia')
        elif value == 'None':
            userdata.saveBlindness('None')


    def modelSelect(self, modelVar):
        if modelVar == 'RetinaNet':
            return 'models\retinanet_resnet50_fpn_coco-eeacb38b.pth'
        if modelVar == 'YOLOv3':
            return 'models\yolov3.pt'
        if modelVar == 'TinyYOLOv3':
            return 'models\tiny-yolov3.pt'


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
        self.originalImageButton = ctk.CTkLabel(self, image=originalImage, height=10, width=10)
        
        self.originalImageButton.grid(row=0, rowspan = 1,
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
        
        imgColoring.manipulate(self.blindnessVar.get())

        self.refreshObjMenu()

            
        
    def refreshObjMenu(self):
        jsonPath = r'output\obj.json'
        with open(jsonPath, 'r') as j:
            data = json.load(j)
    
        self.objPaths = {}
        self.objList = ['None']
        for key, value in data.items():
            self.objVar = ctk.StringVar(self)

            objId = key
            objData = value
            objName = objData[0]
            objPercentage = objData[1]
            objPath = objData[2]
            obj = f'{objId} | {objName}'
            self.objPaths[obj] = objPath
            self.objList.append(obj)
            
        # obj Label
        self.objLabel = ctk.CTkLabel(self,text="Object Selection", 
                                     font=ctk.CTkFont(family='arial', size=20))
        self.objLabel.grid(row=0, column=0, columnspan=3, 
                                padx=50,
                                pady=480,
                                sticky="nw")
        
        # Obj drop box
        self.objOptionMenu = ctk.CTkOptionMenu(self, values=self.objList, 
                                               font=ctk.CTkFont(family='arial', size=16),
                                               variable=self.objVar, command=self.chooseObj)
        self.objOptionMenu.grid(row=0, column=0, columnspan=3, 
                                padx=50,
                                pady=520,
                                sticky="nw")
        
        print(obj)
        print(self.objPaths)

        
        
    def chooseObj(self, value):
        objPath = self.objPaths[value]
        
        if objPath is not None:
            # Display the image
            objImg = cv2.imread(objPath)
            cv2.namedWindow(f'{appName} - Objects view', cv2.WINDOW_AUTOSIZE)
            cv2.imshow(f'{appName} - Objects view', objImg)
            cv2.waitKey(0)  # Wait for a key press to close the image window
            cv2.destroyAllWindows()





# Not used - maybe used in the future
def RetinaNet():
    thread2 = dt.RetinaNet(filePath)
    thread2.start()
    thread2.join()




def download_file(url, destination):
    response = get(url)
    with open(destination, 'wb') as file:
        file.write(response.content)




def homeToSettingsOpen():
    home.withdraw()
    settings.deiconify()

def homeToMainOpen():
    home.withdraw()
    main.deiconify()

def loadingToHomeOpen():
    loading.withdraw()
    home.deiconify()

def settingsToHomeOpen():
    settings.withdraw()
    home.deiconify()

def mainToHomeOpen():
    main.withdraw()
    home.deiconify()





if __name__ == "__main__":
    '''
    
    !!!README!!! : main = Main() needs to be always at the top or it will cause a bug
    
    '''

    main = Main()
    home = Home()
    loading = Loading()
    settings = Settings()

    loading.mainloop()
    
    settings.mainloop()
    settings.withdraw()
    main.mainloop()
    main.withdraw()
=======
'''

Chroma.Ai 
v0.2.3

'''

import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog
from PIL import Image

import os
from requests import get
import threading
import webbrowser
import json

import cv2
import pandas as pd

import userdata
import imgColoring
import detection as dt





# --Model installation vars --
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

# --Data set vars--
dataSetIndex=["Name", "Hex", "Red", "Green", "Blue"]
dataSetPath = r'H:\Adam\School\Coding\Chroma.AI\data\color_names.csv'
dataSet = pd.read_csv(dataSetPath, names=dataSetIndex, header=None)

# --App vars--
appName = 'Chroma.AI'

appLogoPath = r'img\app\icon.ico'

newFilePath = r'output\output.jpg'

modelsCount = 0

weURL = r'https://github.com/JustSnofi/Chroma.AI#readme'

appWidth, appHeight = 780, 780

# Supported modes : Light, Dark, System
ctk.set_appearance_mode('dark')
# Supported themes : green, dark-blue, blue
ctk.set_default_color_theme("green")

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
                self.after(0, loadingToHomeOpen)
            elif modelsCount != 4:
                for link, destination in zip(links, destinations):
                    print('downloading')
                    download_file(link, destination)
                    modelsCount += 1
                    print('downloaded')
                    if modelsCount == 4:
                        self.after(0, loadingToHomeOpen)


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
                                         text="Start", font=font, command=homeToMainOpen)
        self.startButton.grid(row=0, column=0, columnspan=3, 
                                        padx=250, 
                                        pady=190, ipadx = 40, ipady = 30,
                                        sticky="nw")
        
        # Settings Button
        self.settingsButton = ctk.CTkButton(self,
                                        text="Settings", font=font,command=settingsOpen)
        self.settingsButton.grid(row=0, column=0, columnspan=3, 
                                        padx=250, 
                                        pady=300, ipadx = 40, ipady = 30,
                                        sticky="nw")  

        # About us Button
        self.weButton = ctk.CTkButton(self, 
                                        text="About us", font=font, 
                                        width=50, height=20,
                                        command=self.openURL)
        self.weButton.grid(row=0, column=0, 
                                        padx=5, 
                                        pady=15,
                                        sticky="sw")

    def openURL(self):
        webbrowser.open(weURL,new=1)

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
        self.appearanceVar = tk.StringVar(self)
        self.themeVar = tk.StringVar(self)
        padx = 260

        # ChromaAi Title
        self.settingsLabel = ctk.CTkLabel(self,
                                    text="Settings", font=fontTitle)
        
        self.settingsLabel.grid(row=0, column=0, 
                                        padx=220,
                                        pady=35,
                                        sticky="nw")
        
        # Appearance
        self.appearanceLabel = ctk.CTkLabel(self,
                                    text="Appearance \n Dark (Default)", font=font)
        
        self.appearanceLabel.grid(row=0, column=0, columnspan = 1,
                                padx=padx, 
                                pady=200,
                                sticky="nw")
        
        self.appearanceOptionMenu = ctk.CTkOptionMenu(self,
                                                    values=["System", "Light", "Dark"],
                                                    variable = self.appearanceVar, font=font,
                                                    command=self.selectAppearance)

        self.appearanceOptionMenu.grid(row=0, column=0, columnspan=3, 
                                        padx=padx,
                                        pady=280,
                                        sticky="nw")
        
        # Theme
        self.themeLabel = ctk.CTkLabel(self,
                                    text="Theme \n Green (Default)", font=font)
        
        self.themeLabel.grid(row=0, column=0, columnspan = 1,
                            padx=padx, 
                            pady=380,
                            sticky="nw")
        
        themeValues=["green", "dark-blue", "blue"]
        self.themeOptionMenu = ctk.CTkOptionMenu(self, values=themeValues,  
                                                variable = self.themeVar, font=font,
                                                command=self.selectTheme)

        self.themeOptionMenu.grid(row=0, column=0, columnspan=3, 
                                padx=padx,
                                pady=460,
                                sticky="nw")
        
        # Will be added in the next versions
        # self.fullscreenSwitch = ctk.CTkSwitch(self, variable=self.fullscreenVar, command=)
        
        
    def selectAppearance(self, appearanceVar):
        ctk.set_appearance_mode(appearanceVar)
    def selectTheme(self, themeVar):
        ctk.set_default_color_theme(themeVar)
        

# Main Window Class
class Main(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title(appName)
        self.iconbitmap(appLogoPath)
        self.geometry(f"{appWidth}x{appHeight}")
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)
        # self.appearanceVar = tk.StringVar(self)
        # self.themeVar = tk.StringVar(self)
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
        self.blindnessVar = tk.StringVar(value="None")
 
        self.deuRadioButton = ctk.CTkRadioButton(self,
                                  text="Deuteranopia", font=font,
                                  variable=self.blindnessVar, value='deuteranopia', 
                                  command=self.blindnessSelect)
        self.deuRadioButton.grid(row=0, column=0, columnspan=3, 
                                padx=50, 
                                pady=160,
                                sticky="nw")
 
        self.triRadioButton = ctk.CTkRadioButton(self,
                                      text="Tritanopia", font=font,
                                      variable=self.blindnessVar, value='tritanopia',
                                      command=self.blindnessSelect)
        self.triRadioButton.grid(row=0, column=0, columnspan=3, 
                                padx=50, 
                                pady=200,
                                sticky="nw")
         
        self.proRadioButton = ctk.CTkRadioButton(self,
                                    text="Protanopia", font=font,
                                    variable=self.blindnessVar, value='protanopia',
                                    command=self.blindnessSelect)
        self.proRadioButton.grid(row=0, column=0, columnspan=3, 
                                padx=50, 
                                pady=240,
                                sticky="nw")
        self.noneRadioButton = ctk.CTkRadioButton(self,
                                    text="None", font=font,
                                    variable=self.blindnessVar, value='None',
                                    command=self.blindnessSelect)
        self.noneRadioButton.grid(row=0, column=0, columnspan=3, 
                                padx=50, 
                                pady=280,
                                sticky="nw")
 
        # Generate Button
        self.generateResultsButton = ctk.CTkButton(self,
                                         text="Generate Results", font=font, command=self.renderImage)
        self.generateResultsButton.grid(row=0, column=0, columnspan=3, 
                                        padx=50, 
                                        pady=340, ipady = 15,
                                        sticky="nw") 
        
        
        # Model Select and install https://imageai.readthedocs.io/en/latest/detection/ https://github.com/OlafenwaMoses/ImageAI/releases
        
        self.modelLabel = ctk.CTkLabel(self,
                                    text="Model Settings", font=font)
        
        self.modelLabel.grid(row=0, column=0, columnspan = 1,
                            padx=50, 
                            pady=600,
                            sticky="nw")
        
        self.modelOptionMenu = ctk.CTkOptionMenu(self,
                                        values=["RetinaNet", "YOLOv3", "TinyYOLOv3"], font=font, variable = self.modelVar, command=self.modelSelect) 
        
        self.modelOptionMenu.grid(row=0, column=0, columnspan=3, 
                                        padx=50,
                                        pady=640,
                                        sticky="nw")
        
        self.goToSettingsButton = ctk.CTkButton(self, text='Settings', 
                                                font=font, 
                                                command=settingsOpen)
        
        self.goToSettingsButton.grid(row=0, column=0, columnspan=3, 
                                    padx=50,
                                    pady=700,
                                    sticky="nw")
        
    def blindnessSelect(self):
        value = self.blindnessVar.get()    
        if value == 'deuteranopia':
            userdata.saveBlindness('deuteranopia')
        elif value == 'tritanopia':
            userdata.saveBlindness('tritanopia')
        elif value == 'protanopia':
            userdata.saveBlindness('protanopia')
        elif value == 'None':
            userdata.saveBlindness('None')

    def modelSelect(self, modelVar):
        if modelVar == 'RetinaNet':
            return 'models\retinanet_resnet50_fpn_coco-eeacb38b.pth'
        if modelVar == 'YOLOv3':
            return 'models\yolov3.pt'
        if modelVar == 'TinyYOLOv3':
            return 'models\tiny-yolov3.pt'
    
    # def selectAppearance(self, appearanceVar):
    #     ctk.set_appearance_mode(appearanceVar)

    # def selectTheme(self, themeVar):
    #     ctk.set_default_color_theme(themeVar)


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
        self.originalImageButton = ctk.CTkLabel(self, image=originalImage, height=10, width=10)
        
        self.originalImageButton.grid(row=0, rowspan = 1,
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
        
        imgColoring.manipulate(self.blindnessVar.get())

        self.refreshObjMenu()

            
        
    def refreshObjMenu(self):
        jsonPath = r'output\obj.json'
        with open(jsonPath, 'r') as j:
            data = json.load(j)
    
        self.objPaths = {}
        self.objList = ['None']
        for key, value in data.items():
            self.objVar = ctk.StringVar(self)

            objId = key
            objData = value
            objName = objData[0]
            objPercentage = objData[1]
            objPath = objData[2]
            obj = f'{objId} | {objName}'
            self.objPaths[obj] = objPath
            self.objList.append(obj)
            
        # obj Label
        self.objLabel = ctk.CTkLabel(self,text="Object Selection", 
                                     font=ctk.CTkFont(family='arial', size=20))
        self.objLabel.grid(row=0, column=0, columnspan=3, 
                                padx=50,
                                pady=480,
                                sticky="nw")
        
        # Obj drop box
        self.objOptionMenu = ctk.CTkOptionMenu(self, values=self.objList, 
                                               font=ctk.CTkFont(family='arial', size=16),
                                               variable=self.objVar, command=self.chooseObj)
        self.objOptionMenu.grid(row=0, column=0, columnspan=3, 
                                padx=50,
                                pady=520,
                                sticky="nw")
        
        print(obj)
        print(self.objPaths)

    
        
    def chooseObj(self, value):
        objPath = self.objPaths[self.objVar.get()]
        _windowName = f"{appName} - Image Preview"

        if objPath is not None:
            # Color Recognition
            def _recognizeColor(R,G,B):
                print('color recognized')
                _minimum = 10000
                for _colorSet in range(len(dataSet)):
                    _d = abs(R - int(dataSet.loc[_colorSet,"Red"])) 
                    + abs(G - int(dataSet.loc[_colorSet,"Green"])) 
                    + abs(B - int(dataSet.loc[_colorSet,"Blue"]))

                    if(_d<=_minimum):
                        _minimum = _d
                        _cname = dataSet.loc[_colorSet,"Name"]
                return _cname


            def _clickEvent(event, x, y, flags, param):
                if event == cv2.EVENT_LBUTTONDOWN:
                    _imgColor = _img[y, x]  # Get the color of the clicked pixel
                    _imgColor = _imgColor.tolist()  # Convert color to a Python list
                    _imgColor = [int(c) for c in _imgColor]  # Convert color values to integers

                    _r, _g, _b = _imgColor[0], _imgColor[1], _imgColor[2]

                    # Display a rectangle at the top of the window with the clicked color
                    cv2.rectangle(_img, (0, 0), (_imgWidth, 28), _imgColor, -1)

                    if _r + _g + _b >= 300:
                        _textColor = (0, 0, 0)
                    else:
                        _textColor = (255, 255, 255)

                    cv2.putText(_img, f"{_recognizeColor(_r, _g, _b)} | {_r} , {_g} , {_b}", (10, 20), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, _textColor, 1)

                    cv2.imshow(_windowName, _img)

            # Load the image
            _img = cv2.imread(objPath)
            _imgHeight, _imgWidth, _imgChannels = _img.shape
            # Create a window and bind the mouse callback function
            cv2.namedWindow(_windowName)
            cv2.setMouseCallback(_windowName, _clickEvent)
            # Show the original image
            cv2.imshow(_windowName, _img)
            # Wait for a key press to exit
            cv2.waitKey(0)
            cv2.destroyAllWindows()





# Not used - maybe used in the future
def RetinaNet():
    thread2 = dt.RetinaNet(filePath)
    thread2.start()
    thread2.join()




def download_file(url, destination):
    response = get(url)
    with open(destination, 'wb') as file:
        file.write(response.content)



def settingsOpen():
    settings.mainloop()

def homeToMainOpen():
    home.destroy()
    main.mainloop()

def loadingToHomeOpen():
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

    loading.mainloop()



>>>>>>> Stashed changes
