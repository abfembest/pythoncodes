import cv2
import matplotlib as plt
import numpy as np
print(cv2.__version__)

#cv2.imread(path, flag = 1)

img = cv2.imread("Abraham.jpg",cv2.IMREAD_COLOR)
img2 = cv2.imread("ade.png",0)
cv2.waitKey(100)
cv2.destroyAllWindows()
cv2.imshow("Abray", img)
#cv2.imshow("Abray", img2)

#Adding images
#img = cv2.imread("Abraham.jpg")
#img2 = cv2.imread("ade.png")
#a = cv2.addWeighted(img, 0.5, img2, 0.4, 0)
#cv2.imshow(a)

