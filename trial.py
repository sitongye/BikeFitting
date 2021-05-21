import cv2
import numpy as np
import time
import PoseModule as pm

cap = cv2.VideoCapture("AiTrainer/IMG_2063.MOV")

detector = pm.poseDetector()
count = 0
dir = 0
pTime = 0
maxAngle = 0
start_time = time.time()
while True:
    success, img = cap.read()
    h,w,c = img.shape
    img = cv2.resize(img, (w*2, h*2))
    # img = cv2.imread("AiTrainer/test.jpg")
    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, True)
    if len(lmList)!=0:
        x27, y27 = lmList[27][1:]
        if time.time() - start_time > 5:
            angle = detector.findAngle(img, 23, 25, 29, draw=True, extra_text=" MAX: "+str(int(maxAngle))+" ")
            maxAngle = max(angle, maxAngle)



    cv2.imshow("Image", img)
    cv2.waitKey(1)
