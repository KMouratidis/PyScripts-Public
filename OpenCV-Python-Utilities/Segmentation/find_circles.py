import cv2

img = cv2.imread("water_coins.jpg", 3)

blurred = cv2.medianBlur(img, 5)
gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=50,
			   param2=30, minRadius=0, maxRadius=0)

for i in circles[0,:]:
    cv2.circle(img, (i[0], i[1]), i[2], (0,255,0), 2)
    cv2.circle(img, (i[0], i[1]), 2, (0,0,255), 2)

cv2.imwrite("circles.jpg", img)
