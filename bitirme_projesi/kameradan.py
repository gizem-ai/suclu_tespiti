import cv2 as cv
import numpy as np
import face_recognition
import os
import csv
import datetime
import json
from urllib.request import urlopen

dosyaYolu = "kamera_icin"
images=[]
classNames=[]
veriListesi= os.listdir(dosyaYolu)
for cl in veriListesi:
    curImg=cv.imread(f"{dosyaYolu}/{cl}")
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
def findEncodings(dosyaIci):
    yeniBosYuzListesi=[]
    for dosyaIci_yuzBulma in dosyaIci:
        dosyaIci_yuzBulma = cv.cvtColor(dosyaIci_yuzBulma, cv.COLOR_BGR2RGB)
        dosyaIci_bulunanYuz = face_recognition.face_encodings(dosyaIci_yuzBulma)[0]
        yeniBosYuzListesi.append(dosyaIci_bulunanYuz)
    return yeniBosYuzListesi
encodeListKnow=findEncodings(images)

cap=cv.VideoCapture(0)
while True:
    success, kamera = cap.read()
    boyutlandirilmisGoruntu=cv.resize(kamera,(0,0),None,0.25,0.25)
    boyutlandirilmisGoruntu = cv.cvtColor(boyutlandirilmisGoruntu, cv.COLOR_BGR2RGB)
    faceCurFrame = face_recognition.face_locations(boyutlandirilmisGoruntu)
    encodesCutFrame = face_recognition.face_encodings(boyutlandirilmisGoruntu,faceCurFrame)
    for encodeFace,faceLoc in zip(encodesCutFrame,faceCurFrame):
        matches=face_recognition.compare_faces(encodeListKnow,encodeFace)
        faceDis=face_recognition.face_distance(encodeListKnow,encodeFace)
        #print(faceDis)
        matchIndex=np.argmin(faceDis)
        if matches[matchIndex]:
            name=classNames[matchIndex].upper()
            #print(name)
            y1, x2, y2, x1=faceLoc
            y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4
            cv.rectangle(kamera,(x1,y1),(x2,y2),(0,0,255),3)
            cv.rectangle(kamera,(x1,y2-35),(x2,y2),(0,0,0),cv.FILLED)
            cv.putText(kamera,name,(x1+6,y2-6),cv.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
        else:
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv.rectangle(kamera, (x1, y1), (x2, y2), (0, 0, 0),3)
            cv.rectangle(kamera, (x1, y2 - 35), (x2, y2), (0,0,0), cv.FILLED)
            cv.putText(kamera, "Bilinmeyen", (x1 + 6, y2 - 6), cv.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)

    cv.imshow("Webcam",kamera)
    if cv.waitKey(1) & 0xFF == ord('q'):  # q ile çıkış yapabilirsiniz

        with open(name+".csv", "a", newline="") as f:
            url = 'http://ipinfo.io/json'
            response = urlopen(url)
            konum = json.load(response)
            yazıcı = csv.writer(f)
            yazıcı.writerow([name, datetime.datetime.now(),konum])
        break
    cv.waitKey(1)
