# ICCI Conference 2025

## Workshop Title
**Intelligent Vision Systems: Computer Vision and Pattern Recognition Workshop**

---

## Project Files

This repository contains the following computer vision projects:

### 1. Color-Based Ball Detection
- **Folder:** `color based ball detection/`
- **File:** `color_based_ball_detection.py`
- **Description:** Real-time color-based ball detection and tracking using OpenCV HSV color space

### 2. MediaPipe Pose and Hand Detection
- **Folder:** `mediapipe pose detection/`
- **Files:**
  - `mediapipe_pose_detection.py` - Real-time human pose detection with 33 body landmarks
  - `mediapipe_hand_detection.py` - Real-time hand and finger detection with 21 hand landmarks
- **Description:** Real-time pose estimation and hand tracking using MediaPipe

### 3. YOLO Object Detection
- **Folder:** `object detection/`
- **Files:**
  - `detect_webcam.py` - Real-time object detection using YOLOv11 on webcam feed
  - `train_yolo11_object_detection_on_custom_dataset.ipynb` - Jupyter notebook for training custom YOLO models using Roboflow
  - `yolo11s.pt` - Pre-trained YOLOv11 small weights
  - `best.pt` - Custom trained model weights
- **Description:** Real-time object detection and custom model training with YOLOv11

---

## Setup Instructions

### 1. Install Python 3.12

Download and install Python 3.12 from the official website:
- Visit: https://www.python.org/downloads/
- Download Python 3.12
- During installation, make sure to check "Add Python to PATH"

Verify installation:
```bash
python --version
```

### 2. Install Visual Studio Code

Download and install VS Code:
- Visit: https://code.visualstudio.com/
- Download and install for your operating system
- Recommended: Install the Python extension in VS Code

### 3. Install Required Libraries

Open terminal/command prompt and run:

```bash
# Install OpenCV
pip install opencv-python

# Install MediaPipe (for pose and hand detection)
pip install mediapipe

# Install Ultralytics (for YOLO object detection)
pip install ultralytics

# Install NumPy (if needed)
pip install numpy

# For Jupyter notebook (optional)
pip install notebook
```

### 4. Run the Projects

```bash
# For ball detection
python "color based ball detection/color_based_ball_detection.py"

# For pose detection
python "mediapipe pose detection/mediapipe_pose_detection.py"

# For hand detection
python "mediapipe pose detection/mediapipe_hand_detection.py"

# For YOLO object detection
python "object detection/detect_webcam.py"

# For training custom YOLO model (Jupyter notebook)
jupyter notebook "object detection/train_yolo11_object_detection_on_custom_dataset.ipynb"
```

Press 'q' to quit any running program.

---

## Requirements

- Python 3.12+
- OpenCV
- MediaPipe
- Ultralytics YOLO
- Jupyter Notebook (for training)
- Webcam (for real-time detection)

---

## Project Details

### Color-Based Ball Detection
- Uses HSV color space for robust color detection
- Real-time tracking with contour detection
- Adjustable color thresholds

### MediaPipe Solutions
- 33 pose landmarks for full body tracking
- 21 hand landmarks per hand
- High-accuracy real-time inference

### YOLO Object Detection
- Detects 80 object classes
- Real-time inference on webcam
- Custom model training with Roboflow integration
- Pre-trained and custom trained weights included

---

## Workshop Information

For detailed documentation:
- **MediaPipe:** See README in `mediapipe pose detection/` folder
- **YOLO:** See README in `object detection/` folder