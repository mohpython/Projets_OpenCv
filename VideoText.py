import cv2


cap=cv2.VideoCapture("images/fay.mp4")

fps= cap.get(cv2.CAP_PROP_FPS)
H = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
W = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(fps)

out=cv2.VideoWriter("images/gray.avi", cv2.VideoWriter_fourcc("X","V", "I", "D"), int(fps), (H, W))

while cap.isOpened():

    ret, frame=cap.read()
    if ret==True:

        #algorithme de traitemt

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_text=cv2.putText(gray, "Video Gris", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 5)
        #Enregistrement de la video
        out.write(gray_text)
        cv2.imshow("Faynaraa", gray_text)
        if cv2.waitKey(int(1000/fps)) & 0xFF ==ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()

