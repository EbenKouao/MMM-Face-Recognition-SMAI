# SMAI V1.0 - Face Recognition Module

# Modified by: Pratik & Eben
# This is a modified script from the open source face recognition repo:
#https://github.com/ageitgey/face_recognition

import face_recognition
import picamera
import numpy as np
import sys
import os
import time

# Get a reference to the Raspberry Pi camera.
# If this fails, make sure you have a camera connected to the RPi and that you
# enabled your camera in raspi-config and rebooted first.
camera = picamera.PiCamera()
camera.resolution = (320, 240)
output = np.empty((240, 320, 3), dtype=np.uint8)

# Load a sample picture and learn how to recognize it.
print("Loading known face image(s)")
rec_image = face_recognition.load_image_file("/home/pi/MagicMirror/modules/MMM-Face-Recognition-SMAI/public/face.png")
rec_face_encoding = face_recognition.face_encodings(rec_image)[0]

# Initialize some variables
face_locations = []
face_encodings = []

id_check = 0

while True:
    print("Capturing image.")
    # Grab a single frame of video from the RPi camera as a numpy array
    camera.capture(output, format="rgb")

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(output)
    print("Found {} faces in image.".format(len(face_locations)))
    face_encodings = face_recognition.face_encodings(output, face_locations)
    
    face_id = "Guest"
    

    # Loop over each face found in the frame to see if it's someone we know.
    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        match = face_recognition.compare_faces([rec_face_encoding], face_encoding)
        name = "<Unknown Person>"
   
        if id_check == 0:
            for file in os.listdir("/home/pi/MagicMirror/modules/MMM-Face-Recognition-SMAI/public"):
                if file.endswith("-id.png"):
                    face_id = file.replace('-', ' ').split(' ')[0]
                    #print(face_id)
            id_check = 0
            #print(face_id) -- print the name you saved as the MM picture


        if match[0]:
            name = face_id
        
            

        print("Person Detected: {}!".format(face_id))
        f = open("/home/pi/MagicMirror/modules/MMM-Face-Recognition-SMAI/sample.txt", "w")
        f.write(face_id)
        f.close()
        #time taken before the user is logged off from the mirror
        time.sleep(15)
        
    f = open("/home/pi/MagicMirror/modules/MMM-Face-Recognition-SMAI/sample.txt", "w")
    f.write(face_id)
    f.close()