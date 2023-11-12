import cv2 as cv
from cvzone.HandTrackingModule import HandDetector

cap = cv.VideoCapture(0)

detector = HandDetector(detectionCon=0.8, maxHands=2)
                        
while True:
    _, frame = cap.read()
    Hands, frame = detector.findHands(frame)
    if Hands:
        Hand1 = Hands[0]
        lmList1 = Hand1["lmList"]
        if len(Hands) == 2:
            Hand2 = Hands[1]
            lmList2 = Hand2["lmList"]

            length, Info, frame = detector.findDistance(lmList1[8][0:2], lmList2[8][0:2], frame)


    cv.imshow("Hand distance", frame)
    cv.waitKey(1)