import threading
import winsound
import cv2
import imutils
import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode, VideoTransformerBase

# Global variables for alarm state
alarm = False
alarm_mode = False
alarm_counter = 0

def beep_alarm():
    global alarm
    print("Beep alarm function started")
    for _ in range(5):
        if not alarm_mode:
            break
        print("ALARM")
        winsound.Beep(2500, 1000)
    alarm = False

class VideoTransformer(VideoTransformerBase):
    def __init__(self):
        self.start_frame = None
        self.alarm_counter = 0

    def transform(self, frame):
        global alarm, alarm_mode, alarm_counter
        
        img = frame.to_ndarray(format="bgr24")
        img = imutils.resize(img, width=500)
        
        if self.start_frame is None:
            self.start_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            self.start_frame = cv2.GaussianBlur(self.start_frame, (21, 21), 0)
            print("Initial frame captured and processed")
            return img

        if alarm_mode:
            frame_bw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            frame_bw = cv2.GaussianBlur(frame_bw, (21, 21), 0)

            difference = cv2.absdiff(frame_bw, self.start_frame)
            threshold = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)[1]
            self.start_frame = frame_bw

            print(f"Threshold sum: {threshold.sum()}")

            if threshold.sum() > 300:
                self.alarm_counter += 1
            else:
                if self.alarm_counter > 0:
                    self.alarm_counter -= 1

            print(f"Alarm counter: {self.alarm_counter}")

            if self.alarm_counter > 20:
                if not alarm:
                    alarm = True
                    print("Starting alarm thread")
                    threading.Thread(target=beep_alarm).start()
            return threshold

        return img

def toggle_alarm_mode():
    global alarm_mode, alarm_counter
    alarm_mode = not alarm_mode
    alarm_counter = 0
    print(f"Alarm mode toggled to: {alarm_mode}")

st.title("Real-Time Alarm System")

# Controls for the alarm mode
if st.button("Toggle Alarm Mode"):
    toggle_alarm_mode()

if alarm_mode:
    st.write("Alarm Mode is ON")
else:
    st.write("Alarm Mode is OFF")

# Streamlit WebRTC component for video streaming
webrtc_streamer(key="example", mode=WebRtcMode.SENDRECV, video_transformer_factory=VideoTransformer)

if st.button("Quit"):
    alarm_mode = False
    st.stop()
