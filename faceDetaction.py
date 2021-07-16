import cv2
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
######### face detect for an image start ###########
img = cv2.imread('ab.jpg')
gray_scaled_image = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
#train data
face_coordinates = trained_face_data.detectMultiScale(gray_scaled_image)
#print(face_coordinates)
for (x,y,w,h) in face_coordinates:
    cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),5)

cv2.imshow('hell no', img)
cv2.waitKey()
######### face detect for an image end ###########
#-----------------------------------------------------------------------



######### face detect for a video start ###########
webcam = cv2.VideoCapture(0)
while True:
    sucessful_frame_read, frame = webcam.read()
    gray_scaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    #train data
    face_coordinates = trained_face_data.detectMultiScale(gray_scaled_frame)
    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),5)
    cv2.imshow('hell no', frame)
    key = cv2.waitKey(1)

    #stop if Q/q key is pressed
    if key==81 or key==113:
        break
webcam.release()
######### face detect for a video end ###########
print("code completed")