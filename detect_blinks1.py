# USAGE

from scipy.spatial import distance as dist
from imutils import face_utils
import dlib
import cv2
import matplotlib.pyplot as plt
import time

class detector():
    def __init__(self, EYE__RATIO_THRES, FRAME_THRES):
        self.EYE__RATIO_THRES = EYE__RATIO_THRES
        self.FRAME_THRES = FRAME_THRES
        
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
        
        (self.lStart, self.lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
        (self.rStart, self.rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]
        
        self.detect = []
        self.time1 = 0
        self.status = [1]
        self.rising = []
        self.falling = []
        self.length = []
        self.a11 = []
        
        self.t0 = time.time()
        self.lastdown = 0
        self.t1 = 0
        self.response = []
        
        
    def get_rects(self,frame):
        
        rects = self.detector(frame, 0)
        if rects == None:
            return 0
        else:
            return rects[0]
    
    def get_ear(self, picture):
        rect = self.get_rects(picture)
        if rect == 0:
            return 0
        shape = self.predictor(picture, rect)
        shape = face_utils.shape_to_np(shape)
        
        self.leftEye = shape[self.lStart:self.lEnd]
        self.rightEye = shape[self.rStart:self.rEnd]
        
        leftEAR = self.eye_aspect_ratio(self.leftEye)
        rightEAR = self.eye_aspect_ratio(self.rightEye)
        
        
        ears = (leftEAR + rightEAR) / 2
        
        return ears
    
    def eye_aspect_ratio(self,eye):
        
        A = dist.euclidean(eye[1], eye[5])
        B = dist.euclidean(eye[2], eye[4])   
        C = dist.euclidean(eye[0], eye[3])

        self.ear = (A + B) / (2.0 * C)

        return self.ear
    
    def draw(self, frame):
        
        leftEyeHull = cv2.convexHull(self.leftEye)
        rightEyeHull = cv2.convexHull(self.rightEye)
        
        cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)
        frame = cv2.resize(frame, (400,300))  
        cv2.imshow("Frame", frame)
        cv2.moveWindow('Frame',0,300)
        cv2.resizeWindow('Frame', 400,300)
        
    def get_status(self, vs):
        ret, frame = vs.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ear = self.get_ear(gray)
        self.draw(frame)
        if ear < self.EYE__RATIO_THRES:
            self.detect.append(0)
        else:
            self.detect.append(1)
        self.t1 = time.time()
        if self.t1 - self.t0 > 0.5:
            if sum(self.detect[-5:-1]) > 3: # count the past few frames to eliminate the errors
                self.status.append(1)
            else:
                self.status.append(0)
            if self.status[-2] ==1 and self.status[-1] == 0:
                self.lastdown = self.t1
            if self.status[-1] == 0:
                t2 = time.time()
                if t2 - self.lastdown > 0.75:
                    return 1
                else:
                    return 0
            return 0
        return 0
        
    def plot_status(self):
        plt.plot(self.status)
        
def confirm_status(vs,detector):
    a = 0
    key = 0
    for i in range(20):
        a += detector.get_status(vs)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            return(0,key)
    print(a)
    print(detector.ear)

    if a >= 8:
        detector.response.append(1)
        return (1,key)
    else:
        detector.response.append(0)
        return (0,key)