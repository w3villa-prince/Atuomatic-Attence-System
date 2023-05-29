import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime


def Mark_Attendace(name):
    with open('Attendance.csv', 'r+') as f:
        myDataList = f.readline(1)
        nameList = []
        for line in myDataList:
            entry = line.split(' ,')
            nameList.append(entry[0])
            if name not in nameList:
                now = datetime.now()
                dtString = now.strftime('%H:%M:%S')
                f.writelines(f'\n{name}::-   {dtString}')





# markAttendace('Vikas')
Mark_Attendace('RAVI')