import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import numpy as np


class Application(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("600x600")
        self.master.title("ChromAi - color blind helper")
        # icon_image = tk.PhotoImage(file="icon.png")
        # self.master.iconphoto(True, icon_image)
        self.pack()
        self.create_widgets()
    
    def create_widgets(self):
        self.select_file_button = tk.Button(self, text="Select Image", command=self.select_file)
        self.select_file_button.pack()
        
        self.color_label = tk.Label(self, text="Color in Center Pixel: ")
        self.color_label.pack()
        
        self.image_label = tk.Label(self)
        self.image_label.pack()
    
    def select_file(self):
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
            return file_path
    
root = tk.Tk()
app = Application(master=root)
app.mainloop()