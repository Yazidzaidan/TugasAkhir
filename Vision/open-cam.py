import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)
# cap3 = cv2.VideoCapture(2)

def rescale_frame(frame, percent):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)



while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    ret, frame2 = cap2.read()
    # ret, frame3 = cap3.read()

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame 
    cv2.imshow('frame',frame)
    cv2.imshow('frame2',frame2)
    # cv2.imshow('frame3',frame3)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Display the resulting frame (scale)
    #frame40 = rescale_frame(frame, percent=40)
    #cv2.imshow('frame40', frame40)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
    #    break

# When everything done, release the capture
cv2.destroyAllWindows()
