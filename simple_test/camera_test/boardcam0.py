import cv2
cap = "nvarguscamerasrc ! video/x-raw(memory:NVMM), width=640, height=480,format=(string)NV12, framerate=(fraction)30/1 ! nvvidconv flip-method=0 ! video/x-raw, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink"

capture = cv2.VideoCapture(cap)


while capture.isOpened():
    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)
    # ESC를 누르면 종료
    key = cv2.waitKey(1) & 0xFF
    if (key == 27):
        break

capture.release()
cv2.destroyAllWindows()


