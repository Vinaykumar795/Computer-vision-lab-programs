import cv2
import numpy as np

img = cv2.imread(r"D:\dataset\WhatsApp Image 2025-07-03 at 10.13.26_364d70bb.jpg")

kernel = np.ones((5, 5), np.uint8)
eroded_img = cv2.erode(img, kernel, iterations=1)

cv2.imshow("Original Image", img)
cv2.imshow("Eroded Image", eroded_img)
cv2.imwrite("eroded_image.jpg", eroded_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
