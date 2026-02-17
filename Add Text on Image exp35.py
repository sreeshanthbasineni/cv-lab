import cv2

# Read image
image = cv2.imread("sample.jpg")

if image is None:
    print("ERROR: sample.jpg not found!")
    exit()

# Add text
cv2.putText(image,
            "Computer Vision Lab",
            (100, 100),                 # Position (x, y)
            cv2.FONT_HERSHEY_SIMPLEX,   # Font
            1,                          # Font scale
            (0, 0, 255),                # Color (Red)
            2)                          # Thickness

# Show image
cv2.imshow("Text on Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()