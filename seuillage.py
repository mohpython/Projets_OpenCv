import cv2


'''img=cv2.imread('images/gradient.png')

_, tres=cv2.threshold(img, 127, 255, cv2.THRESH_BINARY,)
_, tres1=cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV,)
_, tres2=cv2.threshold(img, 200, 255, cv2.THRESH_TRUNC,)
_, tres3=cv2.threshold(img, 200, 255, cv2.THRESH_TOZERO,)

cv2.imshow('Degrade',img)
cv2.imshow('Binary',tres)
cv2.imshow('Binary IV',tres1)
cv2.imshow('TRUCH',tres2)
cv2.imshow('ZERO',tres3)
'''
img=cv2.imread("images/sudoku.png", 0)
thres=cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
cv2.imshow('Simple',thres)

cv2.waitKey(0)
cv2.destroyAllWindows()