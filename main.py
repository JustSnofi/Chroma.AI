import numpy as np
import pandas as pd
import cv2
import gui
from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()
detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath(r"data\model.pth")
detector.loadModel()
img_path = gui.get_file_path()
data_set_path = r'data\color_names.csv'
data_set = pd.read_csv(data_set_path)
img = cv2.imread(img_path, 1)
output_image_path=os.path.join(execution_path , "imagenew.jpg")
input_image = os.path.join(execution_path , img_path)
detections = detector.detectObjectsFromImage(input_image=input_image, output_image_path=output_image_path)
num = 0


index=["Name", "Hex", "Red", "Green", "Blue"]
csv = pd.read_csv(data_set_path, names=index, header=None)


# Recognizing beta
for eachObject in detections:
        num += 1
        print(num,": ", eachObject["name"] , " : " , eachObject["percentage_probability"] )


# Color Recognition
r = g = b = xpos = ypos = 0
def recognize_color(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i,"Red"])) + abs(G - int(csv.loc[i,"Green"]))+ abs(B - int(csv.loc[i,"Blue"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"Name"]
    return cname

# Click
clicked = False
def mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)


cv2.namedWindow('Color Recognition App')
cv2.setMouseCallback('Color Recognition App', mouse_click)

# Main
while True:
    cv2.imshow("Color Recognition App", cv2.imread(output_image_path)) #cv2.resize(output_image_path, (640, 480))
    if (clicked):
    
        #cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle 
        cv2.rectangle(img,(20,20), (750,60), (b,g,r), -1)
        #Creating text string to display( Color name and RGB values )
        text = recognize_color(r,g,b) + 'R=' + str(r) +  ' G='+ str(g) +  ' B='+ str(b)
            
        #cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
        cv2.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)
        #For very light colours we will display text in black colour
        if(r+g+b>=600):
            cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
                
        clicked=False

    #Break the loop when user hits 'esc' key    
    if cv2.waitKey(20) & 0xFF ==27:
        break
cv2.destroyAllWindows()
cv2.waitKey(0)
