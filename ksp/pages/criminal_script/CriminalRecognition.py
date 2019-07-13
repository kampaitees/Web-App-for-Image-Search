import face_recognition
import cv2
import numpy
from PIL import Image

class CriminalRecognition:

    def __init__(self):
        return
    
    def validator(self,img):
        #print(img)
        face_loc = face_recognition.face_locations(img)
        if len(face_loc)==0:
            return 0
        else:
            return 1

    def face_compare(self,img1,img2):

        if not self.validator(img2):
            return False
 
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
        # small_frame = cv2.resize(img1, (0, 0), fx=0.25, fy=0.25)
        # rgb_small_frame = small_frame[:, :, ::-1]

        
        face_loc_1 = face_recognition.face_locations(img1)
        face_encoding_1 = face_recognition.face_encodings(img1,face_loc_1)

        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
        # small_frame_2 = cv2.resize(img2, (0, 0), fx=0.25, fy=0.25)
        # rgb_small_frame_2 = small_frame_2[:, :, ::-1]

        
        face_loc_2 = face_recognition.face_locations(img2)
        face_encoding_2 = face_recognition.face_encodings(img2,face_loc_2)
        
        if len(face_encoding_1)==len(face_encoding_2):
            check = face_recognition.compare_faces(numpy.array(face_encoding_1), numpy.array(face_encoding_2))
                    
        else:
            return False
    
