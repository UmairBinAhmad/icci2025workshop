# MediaPipe Pose and Hand Detection

Real-time pose and hand detection using MediaPipe and OpenCV.

## Installation Steps

### Step 1: Install Required Libraries

Open your terminal and run the following commands:

```bash
# Install OpenCV
pip install opencv-python

# Install MediaPipe
pip install mediapipe

# Optional: If you encounter any issues, also install:
pip install numpy
```

### Step 2: Verify Installation

Check if the libraries are installed correctly:

```bash
python -c "import cv2; print('OpenCV version:', cv2.__version__)"
python -c "import mediapipe; print('MediaPipe installed successfully')"
```

## Running the Code

### Pose Detection

Run the pose detection script:

```bash
python mediapipe_pose_detection.py
```

**What it does:**
- Opens your webcam
- Detects human pose landmarks (body keypoints)
- Draws skeleton connections on the video feed
- Press 'q' to quit

### Hand and Finger Detection

Run the hand detection script:

```bash
python mediapipe_hand_detection.py
```

**What it does:**
- Opens your webcam
- Detects up to 2 hands
- Draws hand landmarks and finger connections
- Shows the number of hands detected
- Press 'q' to quit

## Troubleshooting

### Camera not opening
- Make sure your webcam is connected and not being used by another application
- Try changing `cv2.VideoCapture(0)` to `cv2.VideoCapture(1)` or `cv2.VideoCapture(2)`

### Import errors
- Make sure you're using Python 3.7 or higher
- Try installing in a virtual environment:
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Linux/Mac
  # venv\Scripts\activate  # On Windows
  pip install opencv-python mediapipe
  ```

### Performance issues
- Reduce frame resolution by adding this after `cap = cv2.VideoCapture(0)`:
  ```python
  cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
  cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
  ```

## Features

### Pose Detection Features:
- 33 body landmarks
- Full body pose estimation
- Real-time tracking

### Hand Detection Features:
- 21 hand landmarks per hand
- Detects up to 2 hands simultaneously
- Finger tracking for gesture recognition

## Requirements

- Python 3.7+
- OpenCV (cv2)
- MediaPipe
- Webcam

## Notes

- Both scripts use webcam feed (camera index 0)
- Press 'q' key to exit the program
- Green landmarks indicate detected keypoints
- Lines connect related landmarks to show body/hand structure
