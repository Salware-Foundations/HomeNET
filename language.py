from flask import json

language = json.load(open("./json/config.json"))["language"]

if language == "en":
    WelcomeText = "Welcome to SecureCloud!"

elif language == "de":
    WelcomeText = "Willkommen bei SecureCloud!"
