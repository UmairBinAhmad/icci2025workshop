import cv2

cap = cv2.VideoCapture(0)

lower=(5,100,100)
upper=(30,255,255)


while True:
  isVideo, frame = cap.read()
  if isVideo == False:
    break

  hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  mask = cv2.inRange(hsv_frame, lower, upper)

  contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

  for cnt in contours:
    area = cv2.contourArea(cnt)
    if area>500:
      #draw circle around the ball
      (x,y), radius = cv2.minEnclosingCircle(cnt)
      center = (int(x), int(y))
      radius = int(radius)
      cv2.circle(frame, center, radius, (0,255,0), 3)
      
      #x,y,w,h = cv2.boundingRect(cnt)
      #cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)
      #cv2.putText(frame, "Ball", (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)

  
  cv2.imshow("Frame",frame)
  cv2.imshow("HSV Frame",hsv_frame)
  cv2.imshow("mask",mask)


  key = cv2.waitKey(1)
  if key==ord('q'):
    break

cap.release()
cv2.destroyAllWindows()