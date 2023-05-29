import cv2
import numpy as np
import face_recognition
import  os
from datetime import datetime


path ='ImageAttendace'
images=[]
classNames=[]
myList=os.listdir(path)
print(myList)

for cl in myList:
    curImg= cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

def findEncoding (images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        faceEncodings = face_recognition.face_encodings(img)
        if len(faceEncodings) > 0:
            encode = faceEncodings[0]
            encodeList.append(encode)
    return encodeList


def markAttendance(name):
    with open ('Attendance1.csv','r+') as f:
        myDataList= f.readlines()
        nameList= []
        for line in myDataList:
            entry= line.split(',')
            nameList.append(entry[0])
        if name not in nameList :
            now = datetime.now()
            dtString= now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')


markAttendance('prince')



encodeListKnown = findEncoding(images)
print(len(encodeListKnown))
print('EncodingComplete')


# def Mark_Attendace(name):
#     with open('Attendance1.csv', 'r+') as f:
#         myDataList = f.readline(1)
#         nameList = []
#         for line in myDataList:
#             entry = line.split(' ,')
#             nameList.append(entry[0])
#             if name not in nameList:
#                 now = datetime.now()
#                 dtString = now.strftime('%H:%M:%S')
#                 print('Enter Input')
#                 f.writelines(f'\n{name}::-   {dtString}')
#
#
# Mark_Attendace('Prince')










cap =cv2.VideoCapture(0)

while True :
    success,img = cap.read()
    imgS=cv2.resize(img,(0,0),None,0.25,0.25)
    imgS=cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCurFrame= face_recognition.face_locations(imgS)
    encodesCurFrame= face_recognition.face_encodings(imgS,faceCurFrame)


    for encodeFace ,faceLoc in zip(encodesCurFrame,faceCurFrame):
        matches= face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
        print(faceDis)
        matchIndex= np.argmin(faceDis)


        if matches[matchIndex]:
            name= classNames[matchIndex].upper()
            print(name)
            markAttendance(name)
            y1,x2,y2,x1= faceLoc
            y1,x2,y2,x1= y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)



    cv2.imshow('Webcam',img)
    cv2.waitKey(1)

