
#%trackbar app

import cv2
import numpy as np
def nothing(x):
    pass

i=np.zeros((512,512,3),np.uint8)

cv2.namedWindow("image")

# 5 adet parametre

r=cv2.createTrackbar("r"," image", 0, 255, nothing)

cv2.createTrackbar("g"," image", 0, 255, nothing)
cv2.createTrackbar("b"," image", 0, 255, nothing)
cv2.create("sw","image",0,1,nothing)



while True:
    cv2.imshow("image",i)
    if cv2.waitKey(1) & 0xff ==ord("q"):
        break
    
    r=cv2.getTrackbarPos("r","image")
    g=cv2.getTrackbarPos("r","image")
    b=cv2.getTrackbarPos("r","image")
    S=cv2.getTrackbarPos("sw","image")
     
    if s==0:
        im[:]=[0,0,0]
    if s==1:
        im[:]=[b,g,r]

cv2.destroyAllWindows()