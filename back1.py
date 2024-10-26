import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import csv
import webbrowser

path = 'C:\\Users\\hemal\\.vscode\\project2\\imagesdata'
images = []
classNames = [] 
myList = os.listdir(path)
background_img = cv2.imread('C:\\Users\\hemal\\.vscode\\project2\\f.png', cv2.IMREAD_UNCHANGED)
print(myList)

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])

print(classNames)

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def markAttendance(name):
    try:
        now = datetime.now()
        dtstr = now.strftime('%d-%m-%Y')
        csv_filename = f'{dtstr}.csv'
        
        if not os.path.exists(csv_filename):
            with open(csv_filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Name', 'Time','Date'])
        
        with open(csv_filename, 'r+', newline='') as f:
            reader = csv.reader(f)
            next(reader) 
            nameList = [row[0] for row in reader]
            
            if name not in nameList:
                dtString = now.strftime('%H:%M:%S')
                dates=now.strftime('%d-%m-%Y')
                writer = csv.writer(f)
                writer.writerow([name, dtString,dates])
    except Exception as e:
        print(f"Error: {e}")

encodeListKnown = findEncodings(images)
print('Encoding complete')

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    facesCurFrame = face_recognition.face_locations(imgS)
    #print(facesCurFrame)
    encodeCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodeCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        #print(faceDis)
        matchIndex = np.argmin(faceDis)
        #print(matchIndex)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (160, 32, 240), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (160, 32, 240), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            markAttendance(name)

        background_img[240:720, 520:1160] = img

    cv2.imshow('webcam', background_img)
    k = cv2.waitKey(1) 

    if k == ord('q'):
        break

cv2.destroyAllWindows()

webbrowser.open('http://127.0.0.1:5000/')