import cv2
import face_recognition

def compare_faces(img1, img2):
	# load images with face_recognition
	face = face_recognition.load_image_file(img1)
	face2compare = face_recognition.load_image_file(img2)

	# change the default BGR channel to RGB
	face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
	face2compare = cv2.cvtColor(face2compare, cv2.COLOR_BGR2RGB)

	# load images with opencv, no need to change the color channel
	#face = cv2.imread(img1)
	#face2compare = cv2.imread(img2)

	# get the encoding of the faces
	encoding_face = face_recognition.face_encodings(face)[0]
	encoding_face2compare = face_recognition.face_encodings(face2compare)[0]
	# compare faces
	result = face_recognition.compare_faces([encoding_face], encoding_face2compare)
	return True in result
