import asyncio
import os
os.environ["OPENCV_LOG_LEVEL"] = "OFF"
import cv2
from face import Surveillance_App

async def main():
    available_devices=[]
    print("Do you want to use a webcam or load a video file?")
    print("1. Webcam")
    print("2. Video file")
    print("3. Demo File")
    print("4. Exit")
    inpt=input("Enter your choice: ")
    if inpt=="1":

        for index in range(10):
            cap = cv2.VideoCapture(index, cv2.CAP_V4L2)

            if cap.isOpened():
                ret, frame = cap.read()
                if ret and frame is not None:
                    available_devices.append(index)
                cap.release()
        
        await Surveillance_App(str(available_devices[0]))
    elif inpt=="2":
        path=input("Enter the path of the video file: ")
        await Surveillance_App(path)
    elif inpt=="3":
        await Surveillance_App("people-detection.mp4")
    elif inpt=='4':

        print("Exiting...")
        exit()

asyncio.run(main())