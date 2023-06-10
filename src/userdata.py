import json
import os
from os import path

username = os.getlogin()

data = {}
jsonPath = r'.userdata\data.json'

def saveBlindness(type):
    data['blindness_type'] = type
    print(data)
    with open(jsonPath, 'w') as f:
        json.dump(data, f)


def make(file_path, file_ext, blindness_type):
    global data
    data['file_path'] = file_path
    data['file_ext'] = file_ext
    data['blindness_type'] = blindness_type
    
def load():
    file_path = data['file_path']
    file_ext = data['file_ext']
    blindness_type = data['blindness_type']
    
    return (file_path, file_ext, blindness_type)

#if path.exists(f'.userdata/{username}'):
    
if __name__ == '__main__':
    saveBlindness('test')
