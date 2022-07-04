
import cv2

cap=cv2.VideoCapture('C:\\Users\\Python\\Desktop\\OPENCV\\OPCV\\images\\test2.mp4')

if not (cap.isOpened()):
    print("Erreur de chargement de la vidéo")

face=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while(True):
    _,image=cap.read()

    image_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    faces=face.detectMultiScale(image_gray, 1.6, 5)
    for x, y, width, height in faces:
        cv2.rectangle(image, (x, y),(x+width, y+height), color=(255, 0, 0), thickness=2)
    cv2.imshow("Algorithme Divin-visage detectes", image)

    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
