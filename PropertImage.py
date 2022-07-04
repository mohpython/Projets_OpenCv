import cv2
import numpy as np

img=cv2.imread("images/Fay.jpg")
#value=img[0, 0]
#print(value)

"""roi=img[100:750, 180:750]

img[0:100, 100:250]=roi



cv2.imshow("Test",img )
cv2.waitKey(0)  """
#propriete d'image
dim=img.shape
print(dim)

prix=img.size
print(prix)

data=img.dtype
print(data)

#slitter

red_cal=img[:, :, 0]
red=np.zeros(img.shape, dtype=np.uint8)
red[:, :, 0]=red_cal
cv2.imshow('',red)
cv2.waitKey(0)

 