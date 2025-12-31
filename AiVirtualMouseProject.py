import cv2
import numpy as np
import HandTrackingModule as htm
import time
import pyautogui

wCam, hCam = 640, 480
frameR = 100
smoothening = 7

pTime = 0
plocX = plocY = 0
clocX = clocY = 0

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

detector = htm.handDetector(maxHands=1)
wScr, hScr = pyautogui.size()

cv2.namedWindow("AI Virtual Mouse")

while True:
    success, img = cap.read()
    if not success:
        break

    img = detector.findHands(img)
    lmList, _ = detector.findPosition(img)

    if lmList:
        x1, y1 = lmList[8][1:]
        fingers = detector.fingersUp()

        cv2.rectangle(
            img, (frameR, frameR),
            (wCam - frameR, hCam - frameR),
            (255, 0, 255), 2
        )

        if fingers[1] == 1 and fingers[2] == 0:
            x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))

            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening

            pyautogui.moveTo(wScr - clocX, clocY)
            plocX, plocY = clocX, clocY

        if fingers[1] == 1 and fingers[2] == 1:
            length, img = detector.findDistance(8, 12, img)
            if length < 40:
                pyautogui.click()
                time.sleep(0.2)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS:{int(fps)}', (20, 50),
                cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv2.imshow("AI Virtual Mouse", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if cv2.getWindowProperty("AI Virtual Mouse", cv2.WND_PROP_VISIBLE) < 1:
        break

cap.release()
cv2.destroyAllWindows()
