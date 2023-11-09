import requests
import cv2
import numpy as np
import os

# Setze die URL der IP Webcam-App mit deinem Handy und den angegebenen Port.
# Stelle sicher, dass dein Handy und dein Computer im selben Netzwerk sind.
urls = ["http://192.168.178.20:4747/video", "http://192.168.178.29:4747/video"]
dirs = ['kampos0/','kampos1/']

def doFoto(url,dirname):
    # Fordere das Kamerabild von der IP Webcam-App an.
    cap = cv2.VideoCapture(url)

    if not cap.isOpened():
        print("Die Kamera konnte nicht geöffnet werden. Stelle sicher, dass IP Webcam läuft und die URL korrekt ist.")
    else:
        # Erfasse ein Foto von der Handykamera.
        ret, frame = cap.read()

        if ret:
            # Speichere das aufgenommene Foto auf deinem Computer.
            cv2.imwrite(dirname, frame)
            print("Foto wurde aufgenommen und gespeichert.")

        # Kamera schließen.
        cap.release()

    # Schließe OpenCV.
    cv2.destroyAllWindows()

def createFileName(path):
    i = 0
    for osl in os.listdir(path):
        i = i+1
    fileName = path + str(i+1) + ".jpg"
    return fileName   


i = 0
for url in urls:
    # dirname = dirs[i] +"foto.jpg"
    dirname = createFileName(dirs[i])
    doFoto(url,dirname)
    i = i+1 
