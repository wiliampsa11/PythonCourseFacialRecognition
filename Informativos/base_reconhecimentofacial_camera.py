#Capa de entrada
import cv2
import os
import imutils

modelo='FotosUiliam'
ruta1='C:/Users/uilia/Desktop/Programas/PythonCourseFacialRecognition/reconocimientofacial1'
rutacompleta=ruta1+'/'+modelo
if not os.path.exists(rutacompleta):
    os.makedirs(rutacompleta)
    print('Carpeta creada:',modelo)

camara=cv2.VideoCapture(0)
ruidos=cv2.CascadeClassifier('entrenamientos opencv ruidos/opencv-4.x/data/haarcascades/haarcascade_frontalface_default.xml')
id=0
while True:
    respuesta,captura=camara.read()
    if respuesta==False:break
    captura=imutils.resize(captura,width=640)
    
    grises=cv2.cvtColor(captura, cv2.COLOR_BGR2GRAY)
    idcaptura=captura.copy()

    cara=ruidos.detectMultiScale(grises, 1.3,5)

    for(x,y,e1,e2) in cara:
        cv2.rectangle(captura,(x,y),(x+e1,y+e2),(255,0,0),2)
        rostrocapturado=idcaptura[y:y+e2,x:x+e1]
        rostrocapturado=cv2.resize(rostrocapturado, (160,160), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(rutacompleta+'/imagen_{}.jpg'.format(id),rostrocapturado)
        id+=1

    cv2.imshow('Resultado',captura)

    if id==351:
        break

camara.release()
cv2.destroyAllWindows()