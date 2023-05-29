import cv2
import numpy as np
import face_recognition
import os


path='ImageAttendace'
images=[]
classNames=[]
myList=os.listdir(path)
print(myList)
for cl in myList:
    curImg=cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    print(len(images))
    classNames.append(os.path.splitext(cl)[0])


print(classNames)








def findEncoding(images):
        encodeList=[]
        for img in images:
            img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
            print(len(encodeList))
           # print(classNames[img])
            print(encodeList)
            return encodeList




encodeListKnow = findEncoding(images)
print('Encoding Done ')
print(len(encodeListKnow))
print(encodeListKnow)