import cv2
import datetime

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) ## its value is 3
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) ## its value is 4

cap.set(3,500)
cap.set(4,500)

print(cap.get(3))
print(cap.get(4))
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        font = cv2.FONT_HERSHEY_COMPLEX
        text = 'With:' + str(cap.get(3)) + 'Height:' + str(cap.get(4))
        datet = str(datetime.datetime.now())
        frame = cv2.putText(frame, datet, (10, 50), font, 1,(0, 255,255), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
##### Hey buddy I treid to clean my laptop because its performance was not good and now if hope its working....



