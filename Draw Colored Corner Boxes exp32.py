import cv2

# Read image
image = cv2.imread("sample.jpg")

if image is None:
    print("ERROR: sample.jpg not found!")
    exit()

height, width, _ = image.shape

# Length of corner lines
length = 40
thickness = 4

# Top-left corner (Blue)
cv2.line(image, (0,0), (length,0), (255,0,0), thickness)
cv2.line(image, (0,0), (0,length), (255,0,0), thickness)

# Top-right corner (Green)
cv2.line(image, (width,0), (width-length,0), (0,255,0), thickness)
cv2.line(image, (width,0), (width,length), (0,255,0), thickness)

# Bottom-left corner (Red)
cv2.line(image, (0,height), (length,height), (0,0,255), thickness)
cv2.line(image, (0,height), (0,height-length), (0,0,255), thickness)

# Bottom-right corner (Yellow)
cv2.line(image, (width,height), (width-length,height), (0,255,255), thickness)
cv2.line(image, (width,height), (width,height-length), (0,255,255), thickness)

# Show result
cv2.imshow("Colored Corner Boxes", image)
cv2.waitKey(0)
cv2.destroyAllWindows()