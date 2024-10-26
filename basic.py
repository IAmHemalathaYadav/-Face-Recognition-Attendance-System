import cv2
import numpy as np
import face_recognition

imghema = face_recognition.load_image_file('C:\\Users\\hemal\\.vscode\\project2\\imagesdata\\hema.jpg')
imghema = cv2.cvtColor(imghema,cv2.COLOR_BGR2RGB)
imgvikram = face_recognition.load_image_file('C:\\Users\\hemal\\.vscode\\project2\\imagesdata\\vikram.jpg')
imgvikram = cv2.cvtColor(imgvikram,cv2.COLOR_BGR2RGB)
imgsrilatha = face_recognition.load_image_file('C:\\Users\\hemal\\.vscode\\project2\\imagesdata\\srilatha.jpg')
imgsrilatha = cv2.cvtColor(imgsrilatha,cv2.COLOR_BGR2RGB)
imgmadhukiran = face_recognition.load_image_file('C:\\Users\\hemal\\.vscode\\project2\\imagesdata\\madhukiran.jpg')
imgmadhukiran = cv2.cvtColor(imgmadhukiran,cv2.COLOR_BGR2RGB)
faceLoc=face_recognition.face_locations(imghema)[0]
encodehema=face_recognition.face_encodings(imghema)[0]
cv2.rectangle(imghema,(faceLoc[3],faceLoc[0],faceLoc[1],faceLoc[2]),(255,0,255))

faceLocV=face_recognition.face_locations(imgvikram)[0]
encodeV=face_recognition.face_encodings(imgvikram)[0]
cv2.rectangle(imgvikram,(faceLoc[3],faceLoc[0],faceLoc[1],faceLoc[2]),(255,0,255))

results = face_recognition.compare_faces([encodeV],encodehema)
faceDis=face_recognition.face_distance([encodeV],encodehema)

print(results,faceDis)
cv2.putText(imgvikram,f'{results} {round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
cv2.imshow('hema',imghema)
cv2.imshow('vikram',imgvikram)


cv2.waitKey(0)