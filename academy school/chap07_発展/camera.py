import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2imshow('camera', frame)

    key = cv2.waitKey(10)
    if key == 27
    break:

cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()cv2.imshow('Detected Circles', img)
cv2.waitKey(0)
