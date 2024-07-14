import cv2

image = cv2.imread('s.jpg')

gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

contour_image = image.copy()

cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)

cv2.imshow("original Image",image)
cv2.imshow("Image with Contours", contour_image)

cv2.waitKey(0)
cv2.destroyAllWindows()