import cv2
image = cv2.imread(r"D:\dataset\WhatsApp Image 2025-07-03 at 10.13.26_364d70bb.jpg")  
edges = cv2.Canny(image, threshold1=30, threshold2=100)
cv2.imshow('Original Image', image)
cv2.imshow('Canny Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()