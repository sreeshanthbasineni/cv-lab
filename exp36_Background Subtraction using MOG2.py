import cv2

# Load video
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

    cv2.imshow("Original Video", frame)
    cv2.imshow("Foreground Mask", fgmask)

    # Press ESC to exit
    if cv2.waitKey(30) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
