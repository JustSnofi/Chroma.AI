'''

Models from the lib imageai

RetinaNet is the main model

Other models will work in the future with Chroma.AI

Models are located in "models\" folder and are downloaded automaticlly when starting main.py

main.py will do an automatic check everytime it opens and see if the models exist.

'''

from imageai.Detection import ObjectDetection
import os
import json
import shutil

execution_path = os.getcwd()
detector = ObjectDetection()
extractedPath = r'output\output-extracted'
# extractedPath = r'img\testing\output-extracted' - for testing
manipulatedPath = r'output\manipulated'
outputPath = r'output'
newFilePath = r'output\output.jpg'

def RetinaNet(img_path) -> None:
    '''
    
    Using RetinaNet ImageAI model
    
    - Recieves Image Path and new Image Path
    - Creates Image
    - Returns None
    
    '''
    
    global detection
    global detectionsSplit
    
    
    Local.handleFolder()

    detector.setModelTypeAsRetinaNet()
    detector.setModelPath(r"models\RetinaNet.pth")
    detector.loadModel()
    input_image = os.path.join(execution_path , img_path)
    detection = detector.detectObjectsFromImage(input_image=input_image, 
                                                output_image_path=newFilePath, 
                                                extract_detected_objects = False)
    detectionsSplit = detector.detectObjectsFromImage(input_image=input_image, 
                                                      output_image_path=newFilePath, 
                                                      extract_detected_objects = True)
    
    Local.enumExtracted()

def YoloV3(img_path):
    '''
    
    Using YoloV3 ImageAI model
    
    - Recieves Image Path and new Image Path
    - Creates Image
    - Returns None
    
    '''

    global detection
    global detectionsSplit

    
    Local.handleFolder()

    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(r"models\TinyYoloV3.pt")
    detector.loadModel()
    output_image_path=os.path.join(execution_path , "imagenew.jpg")
    input_image = os.path.join(execution_path , img_path)
    detectionSplit = detector.detectObjectsFromImage(input_image=input_image, output_image_path=output_image_path, extract_detected_objects = True)
    detection = detector.detectObjectsFromImage(input_image=input_image, output_image_path=output_image_path)
    
    Local.enumExtracted

def TinyYoloV3(img_path):
    '''
    
    Using TinyYoloV3 ImageAI model
    
    - Recieves Image Path and new Image Path
    - Creates Image
    - Returns None
    
    '''
    
    global detection
    global detectionsSplit

    
    Local.handleFolder
    
    detector.setModelTypeAsTinyYOLOv3()
    detector.setModelPath(r"models\YoloV3.pt")
    detector.loadModel()
    output_image_path=os.path.join(execution_path , "imagenew.jpg")
    input_image = os.path.join(execution_path , img_path)
    detections = detector.detectObjectsFromImage(input_image=input_image, output_image_path=output_image_path)
    
    Local.enumExtracted


class Local():
    '''
    
    This class is used locally only on in this file.
    
    '''
    def enumExtracted():
        '''

        Enumerates and renames extracted images

        obj.json stracture: 

        {Object Number(int) : Object Name(str), Object Prob(int), Path(str)}

        '''

        num = 0
        jsonPath = r'output\obj.json'

        with open(r'.userdata\data.json', 'r') as f:
            userdata = json.load(f)

        if userdata['blindness_type'] == 'None':
            data = {}
            files = []
            print(os.listdir)
            for filenameN in os.listdir(extractedPath):
                filePathN = os.path.join(extractedPath, filenameN)
                files.append(filePathN)
        else:
            data = {}
            files = []

            print(os.listdir)
            for filename in os.listdir(extractedPath):
                filePath = os.path.join(manipulatedPath, filename)
                files.append(filePath)
        

        for eachObject in detection:
            num += 1
            objInfo = [eachObject['name'] , eachObject['percentage_probability'], files[num - 1]]
            data[num] = objInfo   

        # Write data dictionary to JSON file
        with open(jsonPath, 'w') as f:
            json.dump(data, f)

        print(data)

    def handleFolder():
        '''
        
        Checking if files exist
        
        '''
        if os.path.exists('output'):
            shutil.rmtree('output')
        if os.path.exists('output') == False:
            os.mkdir('output')


    def deleteFiles():
        '''
        
        Deletes files.
        
        !!!Always use this in each model function, if not it will cause erros!!!
        
        '''

        for filename in os.listdir(outputPath):
            deleteFile = os.path.join(outputPath, filename)
            if os.path.isfile(deleteFile):
                os.remove(deleteFile)


    def deleteFolder():
        '''
        
        Deletes folder.
        
        !!!Always use this in each model function, if not it will cause erros!!!
        
        !!!Always use this together with Local.deleteFiles() if not it will cause errors!!!

        '''
        os.removedirs(extractedPath) 


if __name__ == "__main__":
    '''
    
    !!!Used for testing only!!!
    
    '''

    imgPath = r'img\testing\cars.png'
    
    # RetinaNet(imgPath)
    YoloV3(imgPath)
    # TinyYoloV3(imgPath)
