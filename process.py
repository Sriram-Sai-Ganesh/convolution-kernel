import cv2
import time

from kernels import get_kernel

# process image frames from webcam by default, video files if specified.
def process_video(source_name = "", kernel = get_kernel("identity")):
	
	source = cv2.VideoCapture(0) if source_name=="" else cv2.VideoCapture(source_name)
	print("\n\nConvolution time (per frame):")

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

def process_image(source_name = "", kernel = get_kernel("identity")):
	if source_name == "":
		raise Exception("process.py: No image source specified.")
	image = cv2.imread(source_name)
	filtered_image = process_frame(image, kernel)
	cv2.imshow(kernel_name, filtered_image)
	cv2.waitKey()
	outfile_name = "output/"+kernel_name+" "+source_name.split("/")[-1]
	cv2.imwrite(outfile_name, filtered_image)
	cv2.destroyAllWindows()

def process_frame(image, kernel):
	# Get height and width of the frame.
	h, w = image.shape[:2]
	start_time = time.time()
	result = cv2.filter2D(src=image, ddepth=-1, kernel=kernel)
	print("Frame %i x %ip :  "%(h,w), end="")
	print("%5.3f"%((time.time() - start_time)*1000), end="")
	print("ms")
	return result

def run_gaussian():
	kernel_name = "gaussian blur"
	kernel = get_kernel(kernel_name)
	print("\nKernel dimensions: ",len(kernel),"x",len(kernel[0]))
	print("Using kernel:\n", kernel)
	# process_video(kernel=kernel)
	process_image(source_name = "input/barn.jpg", kernel = kernel)


kernel_name = "x sobel"
kernel = get_kernel(kernel_name)
print("\nKernel dimensions: ",len(kernel),"x",len(kernel[0]))
print("Using kernel:\n", kernel)
# process_video(kernel=kernel)
process_image(source_name = "input/barn.jpg", kernel = kernel)