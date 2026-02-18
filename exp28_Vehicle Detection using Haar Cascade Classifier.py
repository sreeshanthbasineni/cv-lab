import cv2

# Load built-in car cascade (if available)
car_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Read image
image = cv2.imread("veh.jpg")

if image is None:
    print("ERROR: sample.jpg not found!")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect objects
cars = car_cascade.detectMultiScale(gray, 1.1, 3)

# Draw rectangles
for (x, y, w, h) in cars:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Vehicle Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
