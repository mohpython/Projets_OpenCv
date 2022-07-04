import cv2
import numpy  as np



img=cv2.imread("images/lena.jpg")
img_blur=cv2.blur(img,(3, 3))
img_gauss=cv2.GaussianBlur(img, (3, 3),0)
img_media=cv2.medianBlur(img, 3)


image_top=cv2.hconcat([img, img_blur])
image_bot=cv2.hconcat([img_gauss, img_media])

images=cv2.vconcat([image_top, image_bot])

kernel=np.ones((3,3))
cv2.filter2D(img, -1, kernel)

cv2.imshow('original+ ima_flou', images)
cv2.waitKey(0)
cv2.destroyAllWindows()