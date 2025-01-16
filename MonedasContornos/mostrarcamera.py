import cv2
capturaVideo=cv2.VideoCapture(1)
if not capturaVideo.isOpened():
    print("No se puede abrir la cámara")
    exit()
while True:
    tipocamara,Camara=capturaVideo.read()
    grises=cv2.cvtColor(Camara, cv2.COLOR_BGR2GRAY)
    cv2.imshow("En vivo", grises)
    if cv2.waitKey(1)==ord('q'):
        break
capturaVideo.release()
cv2.destroyAllWindows()