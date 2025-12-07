# YOLO Object Detection

Real-time object detection using YOLOv11 and Ultralytics library.

## Setup Instructions

### Install Ultralytics Library

Open your terminal and run:

```bash
pip install ultralytics
```

### Pre-trained Weights

The YOLOv11 small weights file (`yolo11s.pt`) is already included in this folder.

For more information on YOLOv11:
- GitHub: https://github.com/ultralytics/ultralytics
- Documentation: https://docs.ultralytics.com/

## Running the Code

Execute the real-time object detection script:

```bash
python detect_webcam.py
```

**What it does:**
- Opens your webcam
- Loads the YOLOv11 model with pre-trained weights
- Detects objects in real-time
- Draws bounding boxes around detected objects
- Displays class names and confidence scores
- Press 'q' to quit

## Features

- Real-time object detection
- Multiple object classes supported
- Confidence score display
- Bounding box visualization
- Fast inference with YOLOv11 small model

## Supported Object Classes

YOLOv11 can detect 80 different object classes including:
- Person, car, dog, cat, bicycle, motorcycle, truck, bus
- Traffic lights, stop signs, benches, birds, airplanes
- And many more...

## Performance Tips

- If you get low FPS, try reducing frame size:
  ```python
  frame = cv2.resize(frame, (640, 480))
  ```

- For faster inference, use confidence threshold:
  ```python
  results = model(frame, conf=0.5)
  ```

## Requirements

- Python 3.7+
- OpenCV
- Ultralytics YOLO
- Webcam

## Notes

- The model will download additional files on first run
- Processing time depends on your hardware
- GPU acceleration is recommended for better performance
