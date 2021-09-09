# Importando las librerías necesarias
from imutils.video import VideoStream
import imutils
import time
import cv2
import os
# Creando la carpeta de exportación
nombre_carpeta = "dataset/20171099F"
os.makedirs(nombre_carpeta, exist_ok=True)
# Cargando el clasificador
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# Inicializamos el video
print("[INFO] Empezando a grabar..")
vs = VideoStream(src=0).start()
time.sleep(2.0)
total = 0
# Recorremos los fotogramas
while True:
	# Capturamos el fotogramas
	frame = vs.read()
	orig = frame.copy()
	frame = imutils.resize(frame, width=400)
	# Detectamos los rostros
	rects = detector.detectMultiScale(
		cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), scaleFactor=1.1, 
		minNeighbors=5, minSize=(30, 30))
	# Recorremos los rostros detectados
	for (x, y, w, h) in rects:
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # Mostramos el fotograma
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
    # Tomamos captura presionando "f"
	if key == ord("f"):
		p = os.path.sep.join(["dataset/20171099F", "{}.png".format(
			str(total).zfill(5))])
		cv2.imwrite(p, orig)
		total += 1
	# Cerramos presionando "q"
	elif key == ord("q"):
		break
# Resumen general:
print("[INFO] {} imagenes guardadas".format(total))
print("[INFO] Cerrando...")
cv2.destroyAllWindows()
vs.stop()