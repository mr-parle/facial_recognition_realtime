import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facialrecgrealtime-default-rtdb.firebaseio.com/",
    'storageBucket': "facialrecgrealtime.appspot.com"
})

# Importing Images

folderPath = "images"
PathList = os.listdir(folderPath)
imgList = []
studentIDs = []
# print(PathList)

for path in PathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    # print(path)
    studentIDs.append(os.path.splitext(path)[0])

    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)

print(studentIDs)


def findEncoding(imgList):
    encodeList = []
    for img in imgList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList


print("Encoding Started.........")
encodeListKnown = findEncoding(imgList)
encodeListKnownWithIDs = [encodeListKnown, studentIDs]

print("Encoding Compplete ")

file = open("EncoderFile.p", "wb")
pickle.dump(encodeListKnownWithIDs, file)
file.close()
print("File Saved ")
