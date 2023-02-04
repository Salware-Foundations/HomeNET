from flask import json

def max_upload_size():
    data = json.load(open("./json/config.json"))["upload_size"]
        
    return data.rstrip()

def get_local_version():
    data = json.load(open("./json/runtime.json"))["version_local"]
    
    return data.rstrip()