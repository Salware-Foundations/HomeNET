''' 
    Copyright (C) 2023 Juliandev02 and matteodev08 - Authors of HomeNET - Salware Foundations
    You can redistribut it and/or modify it under the terms of the
    GNU General Public License as published by the Free Software Foundation, 
    either version 3 of the License, or (at your option) any later version.
    https://github.com/Salware-Foundations/HomeNET
    
'''

from flask import Flask
from flask import *

from werkzeug.utils import secure_filename

from language import *
from functions import *

import time
import os

# Global Variables
template_path                   = json.load(open("./json/runtime.json"))["template_path"]
static_url_path                 = json.load(open("./json/runtime.json"))["static_url_path"]
static_folder                   = json.load(open("./json/runtime.json"))["static_folder"]
address                         = json.load(open("./json/runtime.json"))["address"]
ip_type                         = json.load(open("./json/runtime.json"))["ip_type"]
port                            = json.load(open("./json/runtime.json"))["port"]
debug_mode                      = json.load(open("./json/runtime.json"))["debug"]


upload_size                     = json.load(open("./json/config.json"))["upload_size"]

github_release                  = "github.com"
build_date                      = "2022-04-02"
build_version                   = "2202.04"
version                         = json.load(open("./json/runtime.json"))["version_local"]
codename                        = "Vanilla Cake"
edition_version                 = "Developer Preview"
uptime                          = time.time()


# App Declaration
system = Flask(__name__, template_folder=template_path, static_url_path=static_url_path, static_folder=static_folder)

system.config["MAX_CONTENT_LENGTH"] = int(upload_size) * 1024^2    # Max upload size in MegaBytes
system.config["SECRET_KEY"] = "rnloJIYsiMVrbPxpDJBR2Em3YuUO6f"     # Secret key for session. Change this to something else.


''' 
    * -- HomeNET Routes -- *
'''

if ip_type == "auto":
    ip = get_ipaddr()

elif ip_type == "local":
    ip = "localhost"

elif ip_type == "all":
    ip = "0.0.0.0"

else:
    ip = "localhost"

# Start HomeNET
if __name__ == "__main__":
    system.run(host=ip, port=port, debug=debug_mode)