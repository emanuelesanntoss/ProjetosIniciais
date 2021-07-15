import cv2

#carrega modelo
#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

#carrega imagem
img = cv2.imread('mia.jpg')

#converte para escala em cinza
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#detectar rostos
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

#desenhar relangulo no rosoto detectado
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)

#mostrar resultado
cv2.imshow('img', img)
cv2.waitKey(0)

