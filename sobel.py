import cv2
import numpy as np
import time
# displays result of sobel filter on webcam feed, in a loop.

# optional @param source_name -- for input file path. Defaults to using webcam feed if left empty.
def get_frame(source_name=''):
	if source_name!='':
		return cv2.imread(source_name)
	else:
		return cv2.VideoCapture(0).read()[1]

def process_frame(img):
	# Convert to graycsale
	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	# Blur the image for better edge detection
	img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 

	# Sobel Edge Detection
	sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
	sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
	sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection
	# Display Sobel Edge Detection Images
	cv2.imshow('Sobel X', sobelx)
	cv2.waitKey(0)
	cv2.imshow('Sobel Y', sobely)
	cv2.waitKey(0)
	cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
	cv2.waitKey(0)


def run_camera():
	cam = cv2.VideoCapture(0)

	cv2.namedWindow("imcap")
	img_counter = 0

	while True:
		ret, frame = cam.read()
		if not ret:
			print("failed to grab frame")
			break
		keypress = cv2.waitKey(1)
		if keypress%256 == 27 or keypress&0xFF!=ord('q'):	# ESC or q pressed
			print("Escape hit, closing...")
			break
		elif keypress%256 == 32:	# SPACE pressed
			img_name = f"frames/opencv_frame_{img_counter}.png"
			cv2.imwrite(img_name, frame)
			print("{} written!".format(img_name))
			img_counter += 1

	cam.release()
	cv2.destroyAllWindows()

img = get_frame()	# swap out with single frame of video later
process_frame(img)
# cv2.imshow('image',img)
# cv2.waitKey()
