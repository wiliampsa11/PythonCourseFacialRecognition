from cProfile import label
import cv2
import os
import numpy as np
from time import time

dataRuta='reconocimientofacial1/data'
listaData=os.listdir(dataRuta)

ids=[]
rostrosData=[]
id=0
tiempoInicial=time()

for fila in listaData:
    rutacompleta=dataRuta+'/'+fila
    print('Iniciando lectura...')
    for archivo in os.listdir(rutacompleta):
        print('Imagenes:',fila + '/' + archivo)
        ids.append(id)
        rostrosData.append(cv2.imread(rutacompleta+'/'+archivo,0))
    
    id=id+1
    tiempoFinal=time()
    tiempoTotal=tiempoFinal-tiempoInicial
    print('Tiempo total de lectura:',tiempoTotal,'segundos')

entrenamientoEigenFaceRecognizer=cv2.face.EigenFaceRecognizer_create()
print("Iniciando el entrenamiento...Espere")
entrenamientoEigenFaceRecognizer.train(rostrosData,np.array(ids))
TiempoFinalEntrenamiento=time()
TiempoTotalEntrenamiento=TiempoFinalEntrenamiento-tiempoTotal
print("Tiempo de treinamento total: ",TiempoTotalEntrenamiento)
entrenamientoEigenFaceRecognizer.write('EntrenamientoEigenFaceRecognizer.xml')
print('Entrenamiento concluído')