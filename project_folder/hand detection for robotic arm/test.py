import cv2
import mediapipe as mp

mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.8, min_tracking_confidence=0.5)
mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
cap.set(3, 1288)
cap.set(4, 720)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            thumb_tip = handLms.landmark[4]  # Thumb tip landmark
            index_tip = handLms.landmark[8]  # Index finger tip landmark

            h, w, c = img.shape
            thumb_x, thumb_y = int(thumb_tip.x * w), int(thumb_tip.y * h)
            index_x, index_y = int(index_tip.x * w), int(index_tip.y * h)

            print(f"Thumb: X={thumb_x}, Y={thumb_y}")
            print(f"Index: X={index_x}, Y={index_y}")

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
