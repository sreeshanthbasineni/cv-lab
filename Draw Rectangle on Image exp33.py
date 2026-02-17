import cv2

# Read image
image = cv2.imread("sample.jpg")

if image is None:
    print("ERROR: sample.jpg not found!")
    exit()

# Draw rectangle
# (x1,y1) = Top-left corner
# (x2,y2) = Bottom-right corner
cv2.rectangle(image, (100, 100), (400, 300), (0, 255, 0), 3)

# Show image
cv2.imshow("Rectangle on Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()