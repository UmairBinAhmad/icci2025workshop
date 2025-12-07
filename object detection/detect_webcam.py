import cv2
from ultralytics import YOLO

# Load the YOLO model
model = YOLO('yolo11s.pt')

# Open the webcam
cap = cv2.VideoCapture(0)

print("Starting YOLO real-time object detection...")
print("Press 'q' to quit")

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Failed to grab frame")
        break
    
    # Run inference
    results = model(frame)
    
    # Draw bounding boxes and labels on the frame
    for result in results:
        boxes = result.boxes
        
        for box in boxes:
            # Get box coordinates
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            
            # Get confidence score
            confidence = box.conf[0]
            
            # Get class name
            class_id = int(box.cls[0])
            class_name = model.names[class_id]
            
            # Draw rectangle
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            
            # Put label with class name and confidence
            label = f"{class_name}: {confidence:.2f}"
            cv2.putText(
                frame,
                label,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 255, 0),
                2
            )
    
    # Display the frame
    cv2.imshow('YOLO Real-time Object Detection', frame)
    
    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

print("Object detection stopped")
