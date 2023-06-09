from imageai.Detection import ObjectDetection
import os
import cv2
import PIL
import json
import shutil

execution_path = os.getcwd()
detector = ObjectDetection()
extractedPath = r'output\output-extracted'
# extractedPath = r'img\testing\output-extracted' - for testing
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
    
    # Making sure the Paths exist so it does not cause any errors
    os.makedirs(extractedPath)
    shutil.rmtree(extractedPath)

    detector.setModelTypeAsRetinaNet()
    detector.setModelPath(r"models\RetinaNet.pth")
    detector.loadModel()
    input_image = os.path.join(execution_path , img_path)
    detection = detector.detectObjectsFromImage(input_image=input_image, output_image_path=newFilePath, extract_detected_objects = False)
    detectionsSplit = detector.detectObjectsFromImage(input_image=input_image, output_image_path=newFilePath, extract_detected_objects = True)
    Local.enumExtracted()

def YoloV3(img_path, output_image_path):
    '''
    
    Using YoloV3 ImageAI model
    
    - Recieves Image Path and new Image Path
    - Creates Image
    - Returns None
    
    '''

    global detection
    global detectionsSplit

    num = 0
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(r"models\TinyYoloV3.pt")
    detector.loadModel()
    output_image_path=os.path.join(execution_path , "imagenew.jpg")
    input_image = os.path.join(execution_path , img_path)
    detectionSplit = detector.detectObjectsFromImage(input_image=input_image, output_image_path=output_image_path, extract_detected_objects = True)
    detection = detector.detectObjectsFromImage(input_image=input_image, output_image_path=output_image_path)

def TinyYoloV3(img_path, output_image_path):
    '''
    
    Using TinyYoloV3 ImageAI model
    
    - Recieves Image Path and new Image Path
    - Creates Image
    - Returns None
    
    '''
    
    global detection
    global detectionsSplit

    num = 0
    detector.setModelTypeAsTinyYOLOv3()
    detector.setModelPath(r"models\YoloV3.pt")
    detector.loadModel()
    output_image_path=os.path.join(execution_path , "imagenew.jpg")
    input_image = os.path.join(execution_path , img_path)
    detections = detector.detectObjectsFromImage(input_image=input_image, output_image_path=output_image_path)
    


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
        data = {}


        for eachObject in detection:
            num += 1
            data[num] = None
            objInfo = [eachObject['name'] , eachObject['percentage_probability']]
        try:
            for filename in os.listdir(extractedPath):
                filePath = os.path.join(extractedPath, filename)
                objInfo.append(filePath)    
                for num in data:
                    data[num] = objInfo   
        except:
            pass

        # Write data dictionary to JSON file
        with open(jsonPath, 'w') as f:
            json.dump(data, f)

        print(data)

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

    imgPath = r'img\testing\haifa.png'
    
    RetinaNet(imgPath)
