import cv2

image = cv2.imread("Filtering&Bluring\Alps-Switzerland.webp")

blurred = cv2.medianBlur(image, 9)

cv2.imshow("Original", image)
cv2.imshow("Clean Image", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()