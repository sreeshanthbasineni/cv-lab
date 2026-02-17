import cv2

# Load face cascade
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Read image
image = cv2.imread("sample1.jpg")

if image is None:
    print("ERROR: human.jpg not found!")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# Draw rectangles
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,0), 2)

# Count faces
count = len(faces)

print("Number of faces detected:", count)

# Display result
cv2.putText(image,
            f"Faces Count: {count}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,0,255),
            2)

cv2.imshow("Face Counting", image)
cv2.waitKey(0)

cv2.destroyAllWindows()