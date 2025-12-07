# YOLO Object Detection

Real-time object detection and custom model training using YOLOv11 and Ultralytics library.

---

## Files in This Folder

### 1. detect_webcam.py
**Real-time Video Inference**
- Opens webcam for live object detection
- Uses pre-trained YOLOv11 model
- Displays bounding boxes, class names, and confidence scores
- Press 'q' to quit

### 2. train_yolo11_object_detection_on_custom_dataset.ipynb
**Custom Model Training Notebook**
- Jupyter notebook for training custom YOLO models
- Integrates with Roboflow for dataset management
- Step-by-step guide for:
  - Dataset preparation
  - Model training
  - Evaluation and validation
  - Export trained weights

### 3. Model Weights
- `yolo11s.pt` - Pre-trained YOLOv11 small model (80 classes)
- `best.pt` - Custom trained model weights

---

## Setup Instructions

### Install Required Libraries

Open your terminal and run:

```bash
# Install Ultralytics YOLO
pip install ultralytics

# Install Jupyter for training notebook
pip install notebook

# Install Roboflow (for custom training)
pip install roboflow
```

### Additional Requirements
- OpenCV (automatically installed with ultralytics)
- PyTorch (automatically installed with ultralytics)

---

## Running the Code

### Real-Time Webcam Detection

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

### Training Custom YOLO Model

**Option 1: Run on Google Colab (Recommended)**

1. Upload the notebook to Google Colab:
   - Go to https://colab.research.google.com/
   - Click "File" → "Upload notebook"
   - Select `train_yolo11_object_detection_on_custom_dataset.ipynb`
   - Or use "File" → "Open notebook" → "GitHub" and paste the repository URL

2. Enable GPU in Colab:
   - Click "Runtime" → "Change runtime type"
   - Select "GPU" as Hardware accelerator
   - Click "Save"

3. Run the notebook cells sequentially

**Option 2: Run Locally with Jupyter**

```bash
jupyter notebook train_yolo11_object_detection_on_custom_dataset.ipynb
```

**Training Process:**
1. Prepare your dataset on Roboflow
2. Download dataset using Roboflow API
3. Configure training parameters
4. Train the model
5. Evaluate results
6. Export custom weights

---

## Features

### Real-Time Detection
- Fast inference with YOLOv11 small model
- Multiple object classes supported
- Confidence score display
- Bounding box visualization
- Real-time performance on CPU/GPU

### Custom Training
- Train on custom datasets
- Roboflow integration for easy dataset management
- Transfer learning from pre-trained weights
- Model evaluation and metrics
- Export trained model for deployment

---

## Supported Object Classes

### Pre-trained Model (80 Classes)
YOLOv11 can detect 80 different object classes including:
- **People & Animals:** Person, dog, cat, bird, horse, sheep, cow
- **Vehicles:** Car, bicycle, motorcycle, truck, bus, train, airplane, boat
- **Street Objects:** Traffic light, stop sign, parking meter, bench
- **Indoor Items:** Chair, couch, bed, dining table, TV, laptop, keyboard, mouse
- **Kitchen:** Bottle, wine glass, cup, fork, knife, spoon, bowl
- **Food:** Banana, apple, sandwich, orange, broccoli, carrot, hot dog, pizza
- And many more...

### Custom Model
- Train on your own dataset with custom classes
- Suitable for specialized applications

---

## Performance Tips

### For Real-Time Detection

1. **Reduce frame size:**
   ```python
   frame = cv2.resize(frame, (640, 480))
   ```

2. **Set confidence threshold:**
   ```python
   results = model(frame, conf=0.5)
   ```

3. **Use GPU acceleration:**
   - Ensure CUDA is installed for GPU support
   - Model automatically uses GPU if available

### For Training

1. **Use GPU for faster training:**
   - Google Colab (free GPU)
   - Local GPU (NVIDIA with CUDA)

2. **Optimize dataset:**
   - Use consistent image sizes
   - Balance class distribution
   - Augment data for better generalization

---

## Requirements

- Python 3.7+
- OpenCV
- Ultralytics YOLO
- PyTorch
- Jupyter Notebook (for training)
- Roboflow account (for custom dataset)
- Webcam (for real-time detection)
- GPU (recommended for training)

---

## Resources

- **YOLOv11 Documentation:** https://docs.ultralytics.com/
- **GitHub Repository:** https://github.com/ultralytics/ultralytics
- **Roboflow:** https://roboflow.com/
- **Pretrained Models:** https://docs.ultralytics.com/models/yolo11/

---

## Notes

- The model will download additional files on first run
- Processing time depends on your hardware
- GPU acceleration significantly improves performance
- Training custom models requires labeled dataset
- Use Roboflow for easy dataset management and annotation
