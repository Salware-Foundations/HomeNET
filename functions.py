from flask import json
import requests
import psutil
import socket

def max_upload_size():
    data = json.load(open("./json/config.json"))["upload_size"]
        
    return data.rstrip()

def get_local_version():
    data = json.load(open("./json/runtime.json"))["version_local"]
    
    return data.rstrip()

def get_online_version():
    data = requests.get("https://raw.githubusercontent.com/Salware-Foundations/HomeNET/main/db/ver.txt")
    
    return data.text.rstrip()

def memory_usage():
    return int(psutil.virtual_memory().total - psutil.virtual_memory().available)


def cpu_usage():
    return psutil.cpu_percent()


def get_ipaddr():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]