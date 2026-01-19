import cv2

image = cv2.imread(r"Phase1\download.jpg")

if image is not None:
    success = cv2.imwrite("output_python.jpg", image)
    if success:
        print("Image saved successfully as 'output_python.jpg'")
    else:
        print("Failed to save an image")
else:
    print("Error: Could not load image")