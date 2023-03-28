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
img_cv2 = cv2.imread(img_path, 1)
display(data_set)

#Doesn't work for some reason
r, g ,b = img.getpixel((616,459))
a = (r,g,b)
display(a)


#MouseCords
def click_event(event, x, y, flags, params):
  
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
  
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)
  
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(x) + ',' +
                    str(y), (x,y), font,
                    1, (255, 0, 0), 2)
        cv2.imshow('image', img)
  
    # checking for right mouse clicks     
    if event==cv2.EVENT_RBUTTONDOWN:
  
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)
  
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        cv2.putText(img, str(b) + ',' +
                    str(g) + ',' + str(r),
                    (x,y), font, 1,
                    (255, 255, 0), 2)
        cv2.imshow('image', img)



if __name__=="__main__":
  
    # reading the image
    img = cv2.imread(img_path, 1)
  
    # displaying the image
    cv2.imshow('image', img)
  
    # setting mouse handler for the image
    # and calling the click_event() function
    cv2.setMouseCallback('image', click_event)
  
    # wait for a key to be pressed to exit
    cv2.waitKey(0)
  
    # close the window
    cv2.destroyAllWindows()

