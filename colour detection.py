import cv2
import numpy as np

def onchange(a):
    pass

path = r"C:\Users\hp\Downloads\images\images\1.png"

cv2.namedWindow("trackbars")
cv2.resizeWindow("trackbars", 640, 320)

cv2.createTrackbar("hue min", "trackbars", 0, 179, onchange)
cv2.createTrackbar("hue max", "trackbars", 179, 179, onchange)
cv2.createTrackbar("sat min", "trackbars", 0, 255, onchange)
cv2.createTrackbar("sat max", "trackbars", 255, 255, onchange)
cv2.createTrackbar("val min", "trackbars", 0, 255, onchange)
cv2.createTrackbar("val max", "trackbars", 255, 255, onchange)

cv2.waitKey(1)

while True:
    img = cv2.imread(path)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    H_MIN = cv2.getTrackbarPos("hue min", "trackbars")
    h_max = cv2.getTrackbarPos("hue max", "trackbars")
    s_MIN = cv2.getTrackbarPos("sat min", "trackbars")
    s_MAX = cv2.getTrackbarPos("sat max", "trackbars")
    v_MIN = cv2.getTrackbarPos("val min", "trackbars")
    v_MAX = cv2.getTrackbarPos("val max", "trackbars")
    lower = np.array([H_MIN, s_MIN, v_MIN])
    upper = np.array([h_max, s_MAX, v_MAX])
    mask = cv2.inRange(img_hsv, lower, upper)
    cv2.imshow("original", img)
    cv2.imshow("mask", mask)
    imgresult = cv2.bitwise_and(img, img, mask=mask)
    cv2.waitKey(1)