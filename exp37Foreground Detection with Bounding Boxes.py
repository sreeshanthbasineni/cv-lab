import cv2

# Open video
cap = cv2.VideoCapture("video.mp4")

if not cap.isOpened():
    print("ERROR: video.mp4 not found!")
    exit()

# Create background subtractor
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Apply background subtraction
    fgmask = fgbg.apply(frame)

    # Threshold to remove shadows/noise
    _, thresh = cv2.threshold(fgmask, 200, 255, cv2.THRESH_BINARY)

    # Find contours
    contours, _ = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Ignore small areas
        if cv2.contourArea(contour) > 800:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Foreground Detection", frame)
    cv2.imshow("Foreground Mask", thresh)

    # Press ESC to stop
    if cv2.waitKey(30) & 0xFF == 27:
        break

cap.release()

cv2.destroyAllWindows()
