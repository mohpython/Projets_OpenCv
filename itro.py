
import cv2

img=cv2.imread('images/eagle.jpg', 0)
print(img.shape)

cv2.imshow("Image Test",img)
k=cv2.waitKey(0)


if k==ord("s"):
    cv2.imwrite("images/eagle_copy.jpg",img)
    print('image a été sauvée')

else:
    cv2.destroyAllWindows()
    print("toutes les fênetres ont été detruites")