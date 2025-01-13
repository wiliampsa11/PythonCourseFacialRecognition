import cv2
imagen=cv2.imread('MonedasContornos\contorno.jpg')
grises=cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
_,umbral=cv2.threshold(grises,100,255,cv2.THRESH_BINARY)
contorno, jerarquia =cv2.findContours(umbral,cv2.RETR_LIST , cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imagen,contorno, -1,(182, 9, 0),3)

#mostrar la imagen
cv2.imshow('imagen original',imagen)
#cv2.imshow('imagen en gris',grises)
#cv2.imshow('Imagen umbraL',umbral)
cv2.waitKey(0)
cv2.destroyAllWindows()