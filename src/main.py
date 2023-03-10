import pandas as pd
import seaborn as sb
import numpy as np
import cv2
from IPython.display import display
import matplotlib


data_set_path = r'data\color_names.csv' 
data_set = pd.read_csv(data_set_path)
img_path = r'etc\test_img.jpg' 
img = cv2.imread(img_path, 1)
display(data_set)

#FIXME
cv2.imshow('image', img)
color_point = img[300,300]

print(matplotlib.colors.to_hex(color_point))


cv2.waitKey(0)
cv2.destroyAllWindows()