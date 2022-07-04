 
import cv2
import numpy as np

img1=np.zeros((255, 500,3), np.uint8)
img2=cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)
img2=cv2.imread("images/image_1.png")
#cv2.imwrite("images/image1.png",img1)

bitAnd=cv2.bitwise_and(img1,img2)


cv2.imshow("image1",img1)
cv2.imshow("image2",img2)
cv2.imshow("bitAnd", bitAnd)

cv2.waitKey(0)
cv2.destroyAllWindows()