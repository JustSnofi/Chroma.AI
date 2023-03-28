import pandas as pd
import seaborn as sb
import numpy as np
import cv2
from IPython.display import display
import matplotlib
from PIL import Image


data_set_path = r'data\color_names.csv' 
data_set = pd.read_csv(data_set_path)
img_path = r'etc\test_img.jpg' 
img = Image.open(img_path).convert("RGB")
display(data_set)

r, g ,b = img.getpixel((5,5))


a = (r,g,b)
display(a)

cv2.waitKey(0)
cv2.destroyAllWindows()