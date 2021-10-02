import numpy as np 
import cv2

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    #Capture frame-by-frame
    ret, frame = cap.read()

    if ret==True:        
        #define range of blue color in BGR
        lower_blue = np.array([140, 0, 0])
        upper_blue = np.array([255, 255, 120])

        #Threshold the HSV image to get only blue colors
        mask = cv2.inRange(frame, lower_blue, upper_blue)
        mask_rgb = cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)

        # Bitwise-AND mask and original image
        res = frame & mask_rgb

        gray_res = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
        uh, thresh = cv2.threshold(gray_res, 0, 255, 0)
        th2 = cv2.adaptiveThreshold(gray_res, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2) 

        contours, hierarchy =  cv2.findContours(th2, 1, 2)

        if len(contours)>0:
            for uh1, contour in enumerate(contours): 
                area = cv2.contourArea(contour) 
                if(area > 300): 
                    x, y, w, h = cv2.boundingRect(contour)
                    frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)


        #Display the resulting frame
        cv2.imshow('frame', frame)
        cv2.imshow('mask_rgb', mask)
        cv2.imshow('res', res)

        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

#When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
