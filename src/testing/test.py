import os
import json

extractedPath = 'path_to_extracted_folder'
jsonPath = 'path_to_output_json_file'
detections = [...]  # Your detections list

num = 0

for filename, eachObject in zip(os.listdir(extractedPath), detections):
    num += 1
    newName = eachObject['name']
    objProb = eachObject['percentage_probability']
    newFileName = os.path.join(extractedPath, newName)

    if os.path.isfile(os.path.join(extractedPath, filename)):
        filePath = os.path.join(extractedPath, filename)
        os.rename(filePath, newFileName)

        # Write object information to JSON file
        with open(jsonPath, 'a') as j:
            data = {
                'filename': newFileName,
                'object_name': newName,
                'object_probability': objProb
            }
            json.dump(data, j)
            j.write('\n')