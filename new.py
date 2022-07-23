import cv2     ##Importing the OpenCV module 
import numpy as np

Video = cv2.VideoCapture("Helicopter.mp4")   ## reading the video file
image = cv2.imread("sky.png")                ## reading the image file

while True:                                  
    ret , frame = Video.read()               ## If there are no video the loop will terminate
    frame = cv2.resize(frame,(640,480))      ## Resize the framer of the video
    image = cv2.resize(image,(640,480))      ## Resize the frame of the image
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)  ## Changing the color from RGB to HSV


    lower = np.array([20,230,100])
    upper = np.array([179,255,255])

    mask = cv2.inRange(hsv,lower,upper)         ## Creating mask for the object 

    
    res = cv2.bitwise_and(frame,frame,mask=mask)## overlapping the mask and the video
    f = frame - res                             ## Adding the object
    green_screen = np.where(f == 0,image,f)     ## Replace the green background by the image



    #cv2.imshow("Frame",frame)
    #cv2.imshow("Mask",mask)
    #cv2.imshow("Res",res)
    #cv2.imshow("f",f)
    cv2.imshow("Final",green_screen)            ## Showing the final image
    k = cv2.waitKey(1)
    if k ==ord('q'):
        break                                   ## If q is pressed then the video will exit.


Video.release()                  ## Releasing the Video              
cv2.destroyAllWindows()          ## Close all window after the video will execute