import cv2

image = cv2.imread("Phase1\download.jpg")

if image is None:
   print("Error: Image not found")
else:
   print("Image loaded successfully")