import numpy as np
import cv2

cap = cv2.VideoCapture("rtsp://username:password@camera_ip:RSTP_code_No/Streaming/Channels/101")

# cap.open()
while(True):
     # Capture frame-by-frame
    ret, frame = cap.read()

    # for operations on the frame or recoloring the following line is used
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # to resize frame the following line is used
    resized_frame = cv2.resize(frame, (640,480))
    
    # Display the resulting frame
    cv2.imshow("RTSP",resized_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

