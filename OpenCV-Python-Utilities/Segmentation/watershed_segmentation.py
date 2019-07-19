import cv2
import numpy as np


img = cv2.imread("water_coins.jpg", 3)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
cv2.imwrite("thresholded.jpg", thresh)

kernel = np.ones((3,3), np.uint8)

opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
cv2.imwrite("opening.jpg", opening)

sure_bg = cv2.dilate(opening, kernel, iterations=3)
cv2.imwrite("sure_bg.jpg", sure_bg)

dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
cv2.imwrite("dist_transform.jpg", dist_transform)

ret, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
sure_fg = np.uint8(sure_fg)
cv2.imwrite("sure_fg.jpg", sure_fg)

unknown = cv2.subtract(sure_bg, sure_fg)
cv2.imwrite("unknown.jpg", unknown)

ret, markers = cv2.connectedComponents(sure_fg)
cv2.imwrite("markers1.jpg", markers)

markers += 1
markers[unknown==255] = 0

markers = cv2.watershed(img, markers)
cv2.imwrite("markers2.jpg", markers)

img[markers == -1] = [255,0,0]
cv2.imwrite("final_segmentation.jpg", img)

img[markers == 1] = [0,0,255]
img[markers > 1] = [0,255,0]
cv2.imwrite("final_segmentation_BGFG.jpg", img)

