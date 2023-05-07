import json 
import os
import requests
os.chdir(f"{os.getcwd()}\\Test")
accessToken = "ya29.A0ARrdaM9OtwhGgfhPHso7qTUJOeyAUum8vHLXrfvvVL2G_7FGQGtcEHVzokXo_OPa_P28JEG67HRsBXZP3h5oGsRes1Fc7daDnoajJkAJnu9_g-1sbBmxCFNBAiX9uHDnH-uDSi9CDQ4wF5cElkf5UbY_vAO_"
headers = {"Authorization": f"Bearer {accessToken}"}
keyword = "game"
while True:
    para = {
        "name":[fileName for fileName in os.listdir() if keyword in fileName],
        "parents":["1U_TEJM4poBNFcfWuBGRCH0--1TDCzYLE"]
    } 

    for openFile in para["name"]: 
        files = {
            "data":("metadata",json.dumps(para),"application/json; charset=U"), 
            "file": open(openFile,"rb")  

        }
        r = requests.post(
            "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
            headers=headers,
            files=files
            )
# print(f"{fileName} has been uploaded to Google Drive.")