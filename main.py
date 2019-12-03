from detect_blinks1 import *
from gui import *

if __name__ == '__main__':
	EYE_AR_THRESH = 0.16
	FRAME_THRES = 0.5
	vs = cv2.VideoCapture(0)
	fileStream = True
	detect = detector(EYE_AR_THRESH,FRAME_THRES)
	initialize()
	root.after(0, show, vs, detect)
	root.mainloop()
	cv2.destroyAllWindows()
	vs.release()