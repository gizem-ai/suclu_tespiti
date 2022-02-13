import cv2 as cv
import numpy as np
import face_recognition
import os

dosyaYolu = "kamera_icin"
images=[]
classNames=[]
veriListesi= os.listdir(dosyaYolu)
#print(veriListesi)

for cl in veriListesi:
    curImg=cv.imread(f"{dosyaYolu}/{cl}")
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

def findEncodings(dosyaIci):
    yeniBosYuzListesi=[]
    for dosyaIci_yuzBulma in dosyaIci:
        dosyaIci_yuzBulma = cv.cvtColor(dosyaIci_yuzBulma, cv.COLOR_BGR2RGB)
        dosyaIci_bulunanYuz = face_recognition.face_encodings(dosyaIci_yuzBulma)[0]
        yeniBosYuzListesi.append(dosyaIci_bulunanYuz)
    return yeniBosYuzListesi

encodeListKnow=findEncodings(images)
print("Encoding Complete")

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
            cv.rectangle(kamera,(x1,y1),(x2,y2),(54,26,153),2)
            cv.rectangle(kamera,(x1,y2-35),(x2,y2),(54,87,125),cv.FILLED)
            cv.putText(kamera,name,(x1+6,y2-6),cv.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)

    cv.imshow("Webcam",kamera)
    if cv.waitKey(1) & 0xFF == ord('q'):  # q ile çıkış yapabilirsiniz
        break
    cv.waitKey(1)

#38. dakikada kaldım.




