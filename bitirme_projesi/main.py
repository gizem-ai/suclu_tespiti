import cv2 as cv
import numpy as np
import face_recognition

imgJohn1=face_recognition.load_image_file("images/johndepp.jpg");
imgJohn1=cv.cvtColor(imgJohn1,cv.COLOR_BGR2RGB);
imgJohn2=face_recognition.load_image_file("images/johnnydepp1.jpg");
imgJohn2=cv.cvtColor(imgJohn2,cv.COLOR_BGR2RGB);

faceLoc=face_recognition.face_locations(imgJohn1)[0]
encodeElon=face_recognition.face_encodings(imgJohn1)[0]
cv.rectangle(imgJohn1,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)
#print(faceLoc)   fotoda ki yüzün lokasyonunu aldı
faceLoc=face_recognition.face_locations(imgJohn2)[0]
encodeTest=face_recognition.face_encodings(imgJohn2)[0]
cv.rectangle(imgJohn2,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)

results=face_recognition.compare_faces([encodeElon],encodeTest)
faceDis=face_recognition.face_distance([encodeElon],encodeTest)
#print(results,faceDis)
cv.putText(imgJohn2,f'{results}{round(faceDis[0],2)}',(20,20),cv.FONT_HERSHEY_COMPLEX_SMALL,1,(200,12,75),1)

cv.imshow("deneme1",imgJohn1)
cv.imshow("deneme2",imgJohn2)
cv.waitKey(0)