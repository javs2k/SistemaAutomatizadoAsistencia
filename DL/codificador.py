# Importando las librerías necesarias
from imutils import paths
import face_recognition
import pickle
import cv2

# Obteniendo las rutas de la imagenes de entrada
print("[INFO] Cuantificando rostros...")
imagePaths = list(paths.list_images('dataset'))
# Inicializando listas
knownEncodings = []
knownNames = []
# Recorriendo imagenes de entrada
for (i, imagePath) in enumerate(imagePaths):
	# Extrayendo el código de cada alumno
	print("[INFO] Procesando imagen {}/{}".format(i + 1,
		len(imagePaths)))
	name = imagePath.split(".")[1]
	# Cargando imagen y convirtiendo a RGB
	image = cv2.imread(imagePath)
	rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Detectando las coordenadas del rostro
	boxes = face_recognition.face_locations(rgb,
		model="cnn")
	# Codificando el rostro a un vector
	encodings = face_recognition.face_encodings(rgb, boxes)
	# Recorriendo las codificaciones
	for encoding in encodings:
		# Agregando la codificación y nombre correspondiente
		knownEncodings.append(encoding)
		knownNames.append(name)

# Guardamos la data
print("[INFO] Serializando...")
data = {"encodings": knownEncodings, "names": knownNames}
f = open("encodings.pickle", "wb")
f.write(pickle.dumps(data))
f.close()