import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


webcam = cv2.VideoCapture(0)
while True:
    ret, frame = webcam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow('Face Detection', frame)
    if cv2.waitKey(10) & 0xFF == ord('e'):
        break
webcam.release()
cv2.destroyAllWindows()
