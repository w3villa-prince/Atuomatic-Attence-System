import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

path = 'ImageAttendace'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cls in myList:
    curImg = cv2.imread(f'{path}/{cls}')
    images.append(curImg)
    print("print image len")
    print(len(images))
    classNames.append(os.path.splitext(cls)[0])

print(classNames)


def findEncoding(images):
    encodeList = []

    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        print("Take Image in encode")
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
       # print(len(encodeList))
        print(classNames[img])
       # print(encodeList)
    return encodeList

    encodeListKnow =  findEncoding(images)
    print(len(encodeListKnow))
    print(encodeListKnow)

def markAttendace(name):
    with open('Attendance.csv','r+') as f:
        myDataList= f.readline();
        nameList=[]
        for line in myDataList:
            entry= line.split(' ,')
            nameList.append(entry[0])
            if name not in nameList:
                now =datetime.now()
                dtString= now.strftime('%H:%M,%S')
                f.writelines(f'\n{name},{dtString}')




#markAttendace('prince')


print('Encoding Done ')


cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
        matches = face_recognition.compare_faces(encodeListKnow, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnow, encodeFace)
        print(faceDis)

        matchIndex = np.argmin(faceDis)
        # print(matchIndex)
        # print(classNames[matchIndex])

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4;
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            markAttendace('Prince')

    cv2.imshow('WebCam', img)
    cv2.waitKey(1)









