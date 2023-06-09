import numpy as np
import cv2
from colorblind import colorblind
import matplotlib.pyplot as plt
import os

extractedPath = r'output\output-extracted'
mainImgPath = r'output\output.jpg'


def manipulate(type):
    '''
    
    Type(String) - excepted values:
    deuteranopia
    tritanopia
    protanopia
    
    '''
    
    if type is not 'None':
        for imgName in os.listdir(extractedPath):
            imgPath = os.path.join(extractedPath, imgName)
            outputName = os.path.splitext(imgName)[0] + '.jpg'  # Change the extension to .jpg
            outputPath = os.path.join(r'output\manipulated', outputName)
            img = cv2.imread(imgPath)
            manipulatedImg = colorblind.hsv_color_correct(img, colorblind_type=type)

            cv2.imwrite(outputPath, manipulatedImg)

        img = cv2.imread(mainImgPath)
        mainManipulatedImg = colorblind.hsv_color_correct(img, colorblind_type=type)
        cv2.imwrite('../images/protanopia_img.jpg', mainManipulatedImg[..., ::-1])
        plt.imshow(mainManipulatedImg.astype(np.uint8))
        plt.savefig(r'output\manipulated\output.jpg')




if __name__ == '__main__':
    manipulate('deuteranopia')