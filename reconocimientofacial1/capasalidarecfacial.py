import cv2
import os
import imutils

dataRuta='reconocimientofacial1/data'
listaData=os.listdir(dataRuta)

entrenamientoEigenFaceRecognizer=cv2.face.EigenFaceRecognizer_create()
entrenamientoEigenFaceRecognizer.read('reconocimientofacial1/EntrenamientoEigenFaceRecognizer.xml')
ruidos=cv2.CascadeClassifier('entrenamientos opencv ruidos/opencv-4.x/data/haarcascades/haarcascade_frontalface_default.xml')
camara=cv2.VideoCapture("reconocimientofacial1/videos/ElonMusk.mp4")

while True:
    _,captura=camara.read()
    captura=imutils.resize(captura,width=640)
    grises=cv2.cvtColor(captura, cv2.COLOR_BGR2GRAY)
    idcaptura=grises.copy()

    cara=ruidos.detectMultiScale(grises, 1.3,5)

    for(x,y,e1,e2) in cara:
        rostrocapturado=idcaptura[y:y+e2,x:x+e1]
        rostrocapturado=cv2.resize(rostrocapturado, (160,160), interpolation=cv2.INTER_CUBIC)
        resultado=entrenamientoEigenFaceRecognizer.predict(rostrocapturado)
        cv2.putText(captura, "{}".format(resultado),(x,y-5),1,1.3,(0,255,0),1, cv2.LINE_AA)
        if resultado[1]<8900:
            cv2.putText(captura, "{}".format(listaData[resultado[0]]),(x,y-20),2,1.1,(0,255,0),1, cv2.LINE_AA)
            cv2.rectangle(captura,(x,y),(x+e1,y+e2),(255,0,0),2)
        else:
            cv2.putText(captura, "{}".format(listaData[resultado[0]]),(x,y-20),2,0.7,(0,255,0),1, cv2.LINE_AA)
            cv2.rectangle(captura,(x,y),(x+e1,y+e2),(255,0,0),2)
    cv2.imshow('Resultados',captura)

    if cv2.waitKey(1)==ord('q'):
        break

camara.release()
cv2.destroyAllWindows()