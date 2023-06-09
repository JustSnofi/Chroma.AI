import shelve
import os
from os import path

username = os.getlogin()

def make(file_path, file_ext, blindness_type):
    global data
    data = shelve.open(username)
    data['file_path'] = file_path
    data['file_ext'] = file_ext
    data['blindness_type'] = blindness_type
    data.close()

def load():
    file_path = data['file_path']
    file_ext = data['file_ext']
    blindness_type = data['blindness_type']
    data.close()
    
    return (file_path, file_ext, blindness_type)

#if path.exists(f'.userdata/{username}'):
    
    