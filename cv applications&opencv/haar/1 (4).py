#videolar

import cv2 



cap=cv2.VideoCapture(0) #real timeyapalim

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


while True:
    ret,frame=cap.read()
    
    if ret==False:
        break
        
        
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #graye cevirmemiz gerekiyor
    faces_frame = face_cascade.detectMultiScale(gray_frame, 1.3, 3) # x,y,w,h  
    for (x,y,w,h) in faces_frame:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,50), 3)
    #forla her bbir frame kontrol 
    cv2.imshow("elon",frame)
    
    
    if cv2.waitKey(30)& 0xFF== ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()