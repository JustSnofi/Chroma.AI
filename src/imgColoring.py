'''

Image coloring for colorblind using colorblind lib

'''

import numpy as np
import cv2
from colorblind import colorblind
import matplotlib.pyplot as plt
import os
import shutil
import json

extractedPath = r'output\output-extracted'
manipulatedPath = r'output\manipulated'
mainImgPath = r'output\output.jpg'
jsonPath = r'.userdata\data.json'


def manipulate(type):
    '''
    
    Type(String) - excepted values:
    deuteranopia
    tritanopia
    protanopia
    
    '''

    with open(jsonPath, 'r') as f:
        data = json.load(f)
    
    
    if type != 'None':
        os.mkdir(r'output\manipulated')
        for imgName in os.listdir(extractedPath):
            imgPath = os.path.join(extractedPath, imgName)
            outputPath = os.path.join(r'output\manipulated', imgName)
            img = cv2.imread(imgPath)
            manipulatedImg = colorblind.simulate_colorblindness(img, colorblind_type=type)
            cv2.imwrite(outputPath, manipulatedImg)

        mainImgPath = os.path.join(r'output\manipulated\output.jpg')
        mainOutputName = os.path.splitext(mainImgPath)[0] + '.jpg'  # Change the extension to .jpg
        mainOutputPath = os.path.join(r'output\manipulated', mainOutputName)
        img = cv2.imread(imgPath)
        mainManipulatedImg = colorblind.simulate_colorblindness(img, colorblind_type=type)
        cv2.imwrite(mainOutputPath, mainManipulatedImg)



if __name__ == '__main__':
    manipulate(type='tritanopia')