import cv2
from cv2 import polylines
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread("images/eagle.jpg", 1)

H, W=img.shape[:2]
print(H, W)

#insertion de ligne
img=cv2.line(img,(0, 0), (0, 200), (255, 0, 0), 10)
img=cv2.line(img,(0, 0), (200, 0), (255, 0, 0), 10)
img=cv2.arrowedLine(img, (0, 0), (200, 200), (255, 0, 0), 10)

#circle
img=cv2.circle(img, (40, 40), 40, (255, 255, 0), 10)

pts=np.array([[0, H-1], [W-1, H-1], [W-1, 0]], np.int32)
img=cv2.polylines(img, [pts], True, (0, 0, 255), 10)

#rectagle
img=cv2.rectangle(img, (500, 0), (1250, 1000), (0, 255, 0), 8)

#text
img=cv2.putText(img, "Aigle", (590, 64), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), thickness=10)
plt.imshow(img[:,:,::-1])
plt.show()

 