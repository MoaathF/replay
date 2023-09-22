import numpy as np
import cv2

cap = cv2.VideoCapture("rtsp://admin:wwww@1234@192.168.1.168:554/Streaming/Channels/101")

# cap.open()
while(True):
     # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # resize frame
    resized_frame = cv2.resize(frame, (640,480))
    
    # Display the resulting frame
    cv2.imshow("RTSP",resized_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

