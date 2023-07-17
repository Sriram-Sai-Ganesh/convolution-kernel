import cv2
import time

from kernels import get_kernel

# process frames from 
def process_video(source_name = "", kernel_name = "none", side_length = 3, output_file = False):
	
	source = cv2.VideoCapture(0) if source_name=="" else cv2.VideoCapture(source_name)
	kernel = get_kernel(kernel_name, side_length)
	
	print("\nUsing kernel: ")
	print(kernel,"\n\nConvolution time (per frame):")

	# run until video cap is closed, or 'q' is pressed.
	while source.isOpened() and (cv2.waitKey(25) & 0xFF != ord('q')):
		# Capture frames.
		success, image = source.read()
		# print error if no cap
		if not success:
			raise Exception("process.py: Null.Frames.")
			break
		filtered_image = process_frame(image, kernel)
		cv2.imshow(kernel_name, filtered_image)
		# wait 1ms between frames (not a bottleneck)
		cv2.waitKey(1)

def process_image(source=""):
	if source=="":
		raise Exception("process.py: No image source specified.")

def process_frame(image, kernel):
	# Get height and width of the frame.
	h, w = image.shape[:2]
	start_time = time.time()
	result = cv2.filter2D(src=image, ddepth=-1, kernel=kernel)
	print("%5.3f"%((time.time() - start_time)*1000), end="")
	print("ms")
	return result

process_video(kernel_name = "gaussian blur", side_length=3)