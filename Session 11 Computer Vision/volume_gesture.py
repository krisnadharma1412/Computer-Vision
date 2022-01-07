import cv2
import mediapipe as mp
import math
from mediapipe.python.solutions import drawing_utils
import numpy as np

from volume_api import VolumeApi

class VolumeGesture:
    def __init__(self):
        self.capture = cv2.VideoCapture(0)
        self.MP_HANDS = mp.solutions.hands
        self.hands = self.MP_HANDS.Hands()
        self.draw_util = mp.solutions.drawing_utils
        self.result = None
        self.vol_api = VolumeApi()

    def DrawMark(self, img):
        self.result = self.hands.process(img)
        if self.result.multi_hand_landmarks:
            for landmark in self.result.multi_hand_landmarks:
                self.draw_util.draw_landmarks(img, landmark, self.MP_HANDS.HAND_CONNECTIONS)

        return img

    def FindLandmark(self, img, point_number=0):
        landmarks = []
        if self.result.multi_hand_landmarks:
            hand = self.result.multi_hand_landmarks[point_number]
            for id, landmark in enumerate(hand.landmark):
                h, w, _ = img.shape
                lx, ly = int(landmark.x * w), int(landmark.y * h)
                landmarks.append([id, lx, ly])
        
        return landmarks


    def Capture(self):
        while True:
            _, img = self.capture.read()

            img = self.DrawMark(img)
            landmarks = self.FindLandmark(img)

            if len(landmarks) !=0:

                x1, y1 = landmarks[4][1], landmarks[4][2]
                x2, y2 = landmarks[8][1], landmarks[8][2]
               
                cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 3)
                distance = math.hypot(x2 - x1, y2 - y1)
                minVol, maxVol = self.vol_api.RetrieveVolumeRange()

                volume_range = np.interp(distance, [25, 280], [minVol, maxVol])

                self.vol_api.vol_obj.SetMasterVolumeLevel(volume_range, None)
                


            cv2.imshow('Hand Gesture', img)
            key = cv2.waitKey(1)
            if key == 27:
                self.Capture.release()
                break
    
if __name__ == '__main__':
    vol_gesture = VolumeGesture()
    vol_gesture.Capture()