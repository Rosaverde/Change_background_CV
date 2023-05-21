import numpy as np
import cv2
from urllib.request import urlopen

url = 'https://www.constructionplusasia.com/wp-content/uploads/2020/04/Office-View-1-1.png'
response = urlopen(url)
image = np.asarray(bytearray(response.read()), dtype="uint8")
img = cv2.imdecode(image, cv2.IMREAD_COLOR)

img = cv2.resize(img, (640, 480))
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (0, 0, 0), (20, 255, 255))
    # Display the resulting frame
    frame[mask == 0] = img[mask == 0]
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()