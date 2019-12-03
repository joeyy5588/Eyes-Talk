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
        
        
    def get_rects(self,frame):
        
        rects = self.detector(frame, 0)
        
        return rects[0]
    
    def get_ear(self, picture):
        
        rect = self.get_rects(picture)
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

        ear = (A + B) / (2.0 * C)

        return ear
    
    def draw(self, frame):
        
        leftEyeHull = cv2.convexHull(self.leftEye)
        rightEyeHull = cv2.convexHull(self.rightEye)
        
        cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)
        cv2.imshow("Frame", frame)
        
    def get_status(self, vs):
        
        ret, frame = vs.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #vs frame to grayscale
        ear = self.get_ear(gray)
        #get the eye aspect ratio
        self.draw(frame)
        if ear < self.EYE__RATIO_THRES:
            self.detect.append(0)
        else:
            self.detect.append(1)
        #append the detection list
        self.t1 = time.time()
#        print(self.t1-self.t0)
        if self.t1 - self.t0 > 0.5:
            if sum(self.detect[-8:-1]) > 5: # count the past few frames to eliminate the errors
                self.status.append(1)
            else:
                self.status.append(0)
        #get the actually eyestatus
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
    for i in range(45):
        a += detector.get_status(vs)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            return(0,key)
    if a > 15:
        return (1,key)
    else:
        return (0,key)
'''
if __name__ == '__main__':
    EYE_AR_THRESH = 0.16
    FRAME_THRES = 0.5
    vs = cv2.VideoCapture(0)
    fileStream = True
    detect = detector(EYE_AR_THRESH,FRAME_THRES)

    while True:
        (m ,key)= confirm_status(vs,detect)
        print(m)
        
        if key == ord("q"):
            break
    detect.plot_status()
    cv2.destroyAllWindows()
    vs.release()
'''