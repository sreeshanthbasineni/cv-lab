import cv2

watch_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

image = cv2.imread("sample1.jpg")

if image is None:
    print("ERROR: sample.jpg not found!")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

watches = watch_cascade.detectMultiScale(gray, 1.3, 5)

for (x, y, w, h) in watches:
    cv2.rectangle(image, (x,y), (x+w,y+h), (255,0,0), 2)

cv2.imshow("Object Detection", image)
cv2.waitKey(0)

cv2.destroyAllWindows()