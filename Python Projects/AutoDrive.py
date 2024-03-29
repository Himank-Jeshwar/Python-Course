from googleapiclient.http import MediaFileUpload
from Google import Create_Service
CLIENT_SECRET_FILE = "Client_Secret.json"
API_NAME = "drive"
API_VERSION  = "v3"
SCOPES = ["https://www.googleapis.com/auth/drive"]

service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

folder_id = "1U_TEJM4poBNFcfWuBGRCH0--1TDCzYLE"
filenames = ["Gta v game.jpg","Gta vice city game.jpg"]
mime_types = ["image/jpeg","image/jpeg"]
for file_name,mime_type in zip(filenames,mime_types) :
    file_metadata = {
        "name":file_name,
        "parents":[folder_id]
    }
    media = MediaFileUpload("/Test/{0}".format(file_name),mimetype=mime_type)
    service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()