# Real-Time AI Surveillance & Detection System

A lightweight, multi-threaded surveillance application that combines deep learning object detection (YOLOv8) and traditional computer vision (OpenCV) to track people and trigger automated audio alarms.

## Features
* **Dual Detection Engine:** Uses YOLOv8 (`yolov8n.pt`) and Haar Cascade classifiers for real-time video frame analysis.
* **Automated Audio Alerts:** Fires non-blocking audio alarms (`alarm.wav`) using background threading and Pygame sound engines.
* **Snapshot Export:** Automatically logs and saves high-confidence detection snapshots (`person.png`).
* **Visual Overlay:** Draws live target bounding boxes, confidence metrics, and state overlays on the video stream.

## Tech Stack
* **Language:** Python 3.12
* **Computer Vision:** OpenCV
* **Object Detection:** Ultralytics YOLOv8
* **Audio Playback:** Pygame

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR-USERNAME/surveillance-system.git
   cd "surveillance system"
   ```

2. **Set up a virtual environment:**
   ```bash
   python3 -m venv .env
   source .env/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the surveillance program:**
   ```bash
   python face.py
   ```
