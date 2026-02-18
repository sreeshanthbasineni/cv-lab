import cv2
import pytesseract

# Set path to tesseract (change if needed)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load video
cap = cv2.VideoCapture("video.mp4")

if not cap.isOpened():
    print("ERROR: video.mp4 not found!")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Extract text
    text = pytesseract.image_to_string(gray)

    print("Detected Text:")
    print(text)

    cv2.imshow("Video Frame", frame)

    if cv2.waitKey(1000) & 0xFF == 27:
        break

cap.release()

cv2.destroyAllWindows()
