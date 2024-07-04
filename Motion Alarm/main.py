# import threading 
# import winsound

# import cv2
# import imutils
# from threading import Thread

# cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT,500)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT,500)

# _,start_frame = cap.read()
# start_frame = imutils.resize(start_frame,width=500)
# start_frame = cv2.cvtColor(start_frame,cv2.COLOR_BGR2GRAY)
# start_frame = cv2.GaussianBlur(start_frame,(21,21),0)

# alarm = False
# alarm_mode = False
# alarm_counter = 0

# def beep_alarm():
#     global alarm
#     for _ in range(5):
#         if not alarm_mode:
#             break
#         print("ALARM")
#         winsound.Beep(2500,1000)
#     alarm = False

# while True:
#     _,frame = cap.read()
#     frame = imutils.resize(frame,width = 500)

#     if alarm_mode:
#         frame_bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         frame_bw = cv2.GaussianBlur(frame,(21,21),0)

#         difference = cv2.absdiff(frame_bw, start_frame)
#         threshold = cv2.threshold(difference,25,255,cv2.THRESH_BINARY)[1]
#         start_frame = frame_bw

#         if threshold.sum() > 300:
#             alarm_counter += 1
#         else:
#             if alarm_counter > 0 :
#                 alarm_counter -= 1
#         cv2.imshow("Cam", threshold)

#     else:
#         cv2.imshow("Cam",frame)

#     if alarm_counter > 20:
#         if not alarm:
#             alarm = True
#             threading = Thread(target=beep_alarm).start()

#     key_pressed = cv2.waitKey(30)
#     if key_pressed == ord("t"):
#         alarm_mode = not alarm_mode
#         alarm_counter = 0
#     if key_pressed == ord("q"):
#         alarm_mode =False
#         break

# cap.release()
# cv2.destroyAllWindows()

import threading
import winsound
import cv2
import imutils

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Set frame width
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # Set frame height

_, start_frame = cap.read()
start_frame = imutils.resize(start_frame, width=500)
start_frame = cv2.cvtColor(start_frame, cv2.COLOR_BGR2GRAY)
start_frame = cv2.GaussianBlur(start_frame, (21, 21), 0)

alarm = False
alarm_mode = False
alarm_counter = 0

def beep_alarm():
    global alarm
    for _ in range(5):
        if not alarm_mode:
            break
        print("ALARM")
        winsound.Beep(2500, 1000)
    alarm = False

while True:
    _, frame = cap.read()
    frame = imutils.resize(frame, width=500)

    if alarm_mode:
        frame_bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_bw = cv2.GaussianBlur(frame_bw, (21, 21), 0)

        difference = cv2.absdiff(frame_bw, start_frame)
        threshold = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)[1]
        start_frame = frame_bw

        if threshold.sum() > 100:
            alarm_counter += 1
        else:
            if alarm_counter > 0:
                alarm_counter -= 1
        cv2.imshow("Cam", threshold)

    else:
        cv2.imshow("Cam", frame)

    if alarm_counter > 10:
        if not alarm:
            alarm = True
            threading.Thread(target=beep_alarm).start()  # Start the thread properly

    key_pressed = cv2.waitKey(30)
    if key_pressed == ord("t"):
        alarm_mode = not alarm_mode
        alarm_counter = 0
    if key_pressed == ord("q"):
        alarm_mode = False
        break

cap.release()
cv2.destroyAllWindows()
