import cv2
import numpy as np
import face_recognition
imgowner =face_recognition.load_image_file('Image/Ravi.jpG')
imgowner =cv2.cvtColor(imgowner,cv2.COLOR_BGR2RGB)

imgtester =face_recognition.load_image_file('Image/mam.jpg')
imgtester =cv2.cvtColor(imgtester,cv2.COLOR_BGR2RGB)

faceLoc =face_recognition.face_locations(imgowner)[0]
encodeowner = face_recognition.face_encodings(imgowner)[0]
cv2.rectangle(imgowner,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)


faceLoctester =face_recognition.face_locations(imgtester)[0]
encodetester= face_recognition.face_encodings(imgtester)[0]
cv2.rectangle(imgtester,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)

results=face_recognition.compare_faces([encodeowner],encodetester)
faceDis= face_recognition.face_distance([encodeowner],encodetester)

print(results,faceDis)
print(encodeowner)
print(encodetester)



cv2.putText(imgtester,f'{results}{round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)

cv2.imshow('Owner',imgowner)
cv2.imshow('TESTER ',imgtester)




cv2.waitKey(0)