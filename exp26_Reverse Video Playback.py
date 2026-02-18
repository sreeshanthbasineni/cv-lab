import cv2

# Open video file
cap = cv2.VideoCapture("video.mp4")

if not cap.isOpened():
    print("ERROR: video.mp4 not found!")
    exit()

frames = []

# Read and store all frames
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)

cap.release()

# Play frames in reverse
for frame in reversed(frames):
    cv2.imshow("Reverse Video", frame)

    # Normal speed
    if cv2.waitKey(30) & 0xFF == 27:
        break

cv2.destroyAllWindows()
