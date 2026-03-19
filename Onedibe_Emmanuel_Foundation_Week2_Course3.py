import cv2

# Load the corrupted image
image = cv2.imread("corrupted_image.jpg")

# Adjust contrast (alpha) and brightness (beta)
alpha = 1.5   # contrast control
beta = 20     # brightness control

restored = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

# Show images
cv2.imshow("Original Corrupted Image", image)
cv2.imshow("Restored Image", restored)

cv2.waitKey(0)
cv2.destroyAllWindows()
