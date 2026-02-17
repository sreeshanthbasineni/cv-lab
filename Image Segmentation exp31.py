import cv2

# Read image
image = cv2.imread("sample.jpg")

if image is None:
    print("ERROR: sample.jpg not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Display results
cv2.imshow("Original Image", gray)
cv2.imshow("Segmented Image (Binary)", thresh)

cv2.waitKey(0)

cv2.destroyAllWindows()