import cv2
import mediapipe as mp
import time
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

# load camera from iphone
address = r"http://192.168.8.100:4747/video"
video = cv2.VideoCapture(address)
while True:
    check, frame = video.read()
    if frame is not None:
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)
        # print(results.multi_hand_landmarks)
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                # draw the points
                mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        cv2.putText(frame, str(int(fps)), (10,70), cv2.FONT_ITALIC, 3, (255, 0, 255), 3)


        cv2.imshow("my iphone", frame)
        key = cv2.waitKey(1)

        if key==ord("q"):
            break
video.release()
cv2.destroyAllWindows()