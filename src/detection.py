from imageai.Detection import ObjectDetection
import os
import cv2
import PIL

execution_path = os.getcwd()
detector = ObjectDetection()
def RetinaNet(img_path):
    num = 0
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath(r"models\RetinaNet.pth")
    detector.loadModel()
    output_image_path= r"img\testingimagenew.jpg"
    input_image = os.path.join(execution_path , img_path)
    detections = detector.detectObjectsFromImage(input_image=input_image, output_image_path=output_image_path)
    
    # for eachObject in detections:
    #     num += 1
    #     with open('.obj', 'w') as f:
    #         f.write(num,": ", eachObject["name"] , " : " , eachObject["percentage_probability"])

def YoloV3(img_path):
    num = 0
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(r"models\TinyYoloV3.pt")
    detector.loadModel()
    output_image_path=os.path.join(execution_path , "imagenew.jpg")
    input_image = os.path.join(execution_path , img_path)
    detections = detector.detectObjectsFromImage(input_image=input_image, output_image_path=output_image_path)
    
    for eachObject in detections:
        num += 1
        print(num,": ", eachObject["name"] , " : " , eachObject["percentage_probability"])

def TinyYoloV3(img_path):
    num = 0
    detector.setModelTypeAsTinyYOLOv3()
    detector.setModelPath(r"models\YoloV3.pt")
    detector.loadModel()
    output_image_path=os.path.join(execution_path , "imagenew.jpg")
    input_image = os.path.join(execution_path , img_path)
    detections = detector.detectObjectsFromImage(input_image=input_image, output_image_path=output_image_path)
    
    for eachObject in detections:
        num += 1
        print(num,": ", eachObject["name"] , " : " , eachObject["percentage_probability"])