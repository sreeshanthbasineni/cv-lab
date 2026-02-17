import cv2

# Read image
image = cv2.imread("sample.jpg")

if image is None:
    print("ERROR: sample.jpg not found!")
    exit()

# Draw circle
# Center (x, y)
# Radius = 100
cv2.circle(image, (300, 200), 100, (255, 0, 0), 3)

# Show image
cv2.imshow("Circle on Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()