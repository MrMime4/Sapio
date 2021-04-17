from imutils.video import VideoStream
import imutils
import cv2,os,urllib.request
import numpy as np
from django.conf import settings
import datetime


class VideoCamera(object):
	def __init__(self):
		self.video = cv2.VideoCapture(0)

		_,inp_img = self.video.read()
		print(_)
		inp_img = cv2.flip(inp_img, 1)
		inp_img = cv2.blur(inp_img, (4,4))
		self.gray_inp_img = cv2.cvtColor(inp_img, cv2.COLOR_BGR2GRAY)

		self.old_pts = np.array([[350, 180], [350, 350]], dtype=np.float32).reshape(-1,1,2)

		self.backup = self.old_pts.copy()
		self.backup_img = self.gray_inp_img.copy()

		#### text o/p window
		self.outp = np.zeros((480,640,3))

		#### variable ####
		self.ytest_pos = 40

	def __del__(self):
		self.video.release()

	def send_data(self):
		return ([self.gray_inp_img,self.old_pts,self.backup,self.backup_img,self.outp,self.ytest_pos])	

	def get_frame(self):
		success, image = self.video.read()

		frame_flip = cv2.flip(image,1)
		blur_img = cv2.blur(frame_flip, (4,4))
		gray = cv2.cvtColor(blur_img, cv2.COLOR_BGR2GRAY)
		ret, jpeg = cv2.imencode('.jpg', gray)
		return ([jpeg.tobytes(),gray])
