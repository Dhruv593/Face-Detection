import cv2

face_cascade = cv2.CascadeClassifier("C:/Users/cocdh/AppData/Local/Programs/Python/Python311/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")

image= cv2.imread('1.jpg')
img = cv2.resize(image,None,fx=0.3,fy=0.3)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(
        imgGray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

for (x,y,w,h) in faces:
	cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)

cv2.imshow('img', img)
cv2.waitKey()