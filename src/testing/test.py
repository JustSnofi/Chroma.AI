from tkinter import *
import customtkinter as ctk
from tkinter import filedialog
from PIL import ImageTk, Image
import numpy as np
import pathlib

class Application(ctk.CTk):
    def __init__(self, master=None):
        self.master = master
        root.title("ChromAi - color blind helper")  # title of the GUI window
        root.maxsize(870, 525)  # specify the max size the window can expand to
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("green")
        self.create_widgets()

    def create_widgets(self):
        left_frame = Frame(root, width=100, height=100, bg='grey')
        left_frame.grid(row=0, column=0, padx=10, pady=5)

        right_frame = Frame(root, width=400, height=400, bg='grey')
        right_frame.grid(row=0, column=1, padx=10, pady=5)

        ctk.CTkButton(left_frame, text="Original Image", command=self.select_file).grid(row=0, column=0, padx=5, pady=5)

        self.selected_image_label = Label(left_frame)
        self.selected_image_label.grid(row=1, column=0, padx=5, pady=5)

        self.selected_image_label_right = Label(right_frame)
        self.selected_image_label_right.grid(row=0, column=0, padx=5, pady=5)

        tool_bar = Frame(left_frame, width=180, height=185,bg='grey')
        tool_bar.grid(row=2, column=0, padx=5, pady=5)

        ctk.CTkLabel(tool_bar, text="Blindness Types",text_color="black").grid(row=0, column=0, padx=5, pady=3, ipadx=10)

        ctk.CTkRadioButton(tool_bar, text="Select").grid(row=1, column=0, padx=5, pady=5)
        ctk.CTkRadioButton(tool_bar, text="Select").grid(row=2, column=0, padx=5, pady=5)
        Label(tool_bar, text="Rotate & Flip").grid(row=3, column=0, padx=5, pady=5)
        Label(tool_bar, text="Resize").grid(row=4, column=0, padx=5, pady=5)
        Label(tool_bar, text="Exposure").grid(row=5, column=0, padx=5, pady=5)

    def select_file(self):
        global file_path
        file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png"), ('JPEG files', "*.jpg"), ('JPEG files', "*.jpeg")])
        if file_path:
            img = Image.open(file_path)
            img = img.resize((200, 200))
            img_tk = ImageTk.PhotoImage(img)

            self.selected_image_label.config(image=img_tk)
            self.selected_image_label.image = img_tk

            img = Image.open(file_path)
            img = img.resize((600, 500))
            img_tk = ImageTk.PhotoImage(img)
            self.selected_image_label_right.config(image=img_tk)
            self.selected_image_label_right.image = img_tk

root = ctk.CTk()
app = Application(master=root)
root.mainloop()