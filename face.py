import cv2
import pygame
import threading
from pathlib import Path
from ultralytics import YOLO
pygame.mixer.init()
alarm_sound = pygame.mixer.Sound("alarm.wav")
is_playing = False
best_conf=0.0
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
def play_sound():
    global is_playing
    is_playing = True
    alarm_sound.play()
    pygame.time.wait(int(alarm_sound.get_length() * 1000))
    is_playing = False
def face_detection(faces,frame):
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
        face=frame[y:y+h, x:x+w]
        cv2.imwrite("face.png", face)
def overlay(frame):
    image_path = Path("person.png")
    face_path = Path("face.png")
    if image_path.exists():

        image = cv2.imread("person.png")
        aspect_ratio=float(image.shape[1]/image.shape[0])
        image=cv2.resize(image, (int(100*aspect_ratio), 100))   
        frame[10:10+image.shape[0], 10:10+image.shape[1]] = image
        if face_path.exists():
            face = cv2.imread("face.png")
            aspect_ratio=float(face.shape[1]/face.shape[0])
            face=cv2.resize(face, (int(100*aspect_ratio), 100))
            x_start = 10 + image.shape[1] + 10
            x_end = x_start + face.shape[1]
                
            frame[10:10+face.shape[0], x_start:x_end] = face

model=YOLO("yolov8n.pt")
cap=cv2.VideoCapture("people-detection.mp4")
while True:
    ret, frame=cap.read()
    if not ret:
        print("End of video stream.")
        break
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray, 1.1, 5) 
    face_detection(faces, frame)
    result = model(frame, verbose=False)
    classes = result[0].boxes.cls.tolist()
    boxes=result[0].boxes
    person_confs = [box.conf.item() for box in boxes if int(box.cls.item()) == 0]
    overlay(frame)
    if 0 in classes:
        
        max_current_conf = max(person_confs)
        if max_current_conf > best_conf:
            best_conf = max_current_conf
            cv2.imwrite("person.png", frame)

            if not is_playing:
                threading.Thread(target=play_sound,daemon=True).start()
    person=result[0].plot()
    cv2.imshow("Video", person)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()