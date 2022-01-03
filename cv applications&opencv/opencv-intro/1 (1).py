#resimlere giris


#%%okuma



import cv2
import matplotlib.pyplot as plt
import numpy as np


a=cv2.imread("super-mario.jpg")

#print(a)

cv2.imshow("foto",a)
cv2.imwrite("a1.jpg",a) #kayt
cv2.waitKey()
cv2.destroyAllWindows()

#%% video
import cv2 

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    cv2.imshow("w",frame)
    #cv2.waitkey(30) # 30 ms gorun 
    cv2.waitkey(100)
cap.release()
cv2.destroyAllWindows()

#%%cizim fonk

import cv2
import numpy as np


canvas=np.zeros((300,300,3),dtype=np.uint8) #+255


cv2.line(canvas,(0,30),(300,300),(255,0,0),thickness=5)
cv2.rectangle(canvas,(0,30),(300,300),(0,255,0),thickness=3)
cv2.circle(canvas,(56,30),4,(0,0,255),thickness=2)

a=(100,200)
b=(200,200)
c=(300,100)



cv2.line(canvas,a,b,(255,0,0),thickness=5)
cv2.line(canvas,b,c,(255,0,0),thickness=5)
cv2.line(canvas,a,c,(255,0,0),thickness=5)
cv2.imshow("c",canvas)

cv2.waitKey()
cv2.destroyAllWindows()

#%%-->yazi  yazma

import cv2
import numpy as np


canvas=np.zeros((300,300,3),dtype=np.uint8) 
font=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(canvas,"hello",(10,70),font,3,(255,0,0),cv2.LINE_AA)



cv2.imshow("c",canvas)
cv2.waitKey()
cv2.destroyAllWindows()












