import cv2

img=cv2.imread('images/bird.jpg')

print(img.shape)
print(img.size)
print(img.dtype)

b, g, r=cv2.split(img)
img=cv2.merge((b, g, r))#Regio Of Iterrest

ball=img[280:340, 330:390]
img2=img[250:333, 160:100] = ball


cv2.imshow('image',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()