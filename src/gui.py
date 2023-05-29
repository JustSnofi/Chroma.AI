import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import numpy as np
import pathlib
import os
from os import path
import shelve
import userdata as ud

username = os.getlogin()

class Application(tk.Frame):
    '''GUI Application'''
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("600x600")
        self.master.title("ChromAi - color blind helper")
        icon_image = tk.PhotoImage(file="img\icon.png")
        self.master.iconphoto(True, icon_image)
        self.option_var = tk.StringVar(self)

        self.blindness_types = ('Normal', 
                                'Deuteranopia', 
                                'Tritanopia', 
                                'Monochromacy')
        
        self.pack()
        self.create_widgets()
    
    def create_widgets(self):
        self.select_file_button = tk.Button(self, text="Select Image", command=self.select_file).pack()
        
        self.color_label = tk.Label(self, text="Color in Center Pixel: ").pack()
        
        self.image_label = tk.Label(self).pack()

        self.select_blindness = tk.OptionMenu(self, self.option_var,*self.blindness_types, command=self.get_blindness).pack()

        self.save_userdata_button = tk.Button(self, 'Save your Userdata', command=self.make_userdata).pack()

        if not path.exists(f'.userdata/{username}'):
            self.load_userdata_button = tk.Button(self, text='Load your Userdata', command=self.load_userdata).pack()

    def select_file(self):
        global file_path
        file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png"), ('JPEG files', "*.jpg"), ('JPEG files', "*.jpeg")])
        if file_path:
            img = Image.open(file_path)
            img_array = np.array(img)
            center_pixel_color = img_array[img_array.shape[0]//2, img_array.shape[1]//2]
            self.color_label.config(text=f"Color in Center Pixel: {center_pixel_color}")
            
            img = Image.open(file_path)
            img = img.resize((300, 300))
            img_tk = ImageTk.PhotoImage(img)
            self.image_label.config(image=img_tk)
            self.image_label.image = img_tk
            # make_user_data()
            return file_path
    
    def get_blindness(self, *args):
        return self.option_var.get()
    

    '''User Data functions (make/load)'''
    def make_userdata(self):
        global data
        data = shelve.open(f'.userdata/{username}')
        data['file_path'] = file_path
        data['file_ext'] = 'jpg'
        data['blindness_type'] = blindness_type
        data.close()

    def load_userdata():
        file_path = data['file_path']
        file_ext = data['file_ext']
        blindness_type = data['blindness_type']
        data.close()

        return (file_path, file_ext, blindness_type)
    

def get_file_path() -> str:
    '''Returns file_path'''
    return file_path

def get_file_extension() -> str:
    '''Returns file_path'''
    global file_extension
    file_extension = pathlib.Path(file_path).suffix
    return file_extension
   
def make_user_data():
    with open('.userdata\data.csv', 'w') as f:
        f.write(file_path + '/n' + file_extension) 

    
root = tk.Tk()
app = Application(master=root)
app.mainloop()