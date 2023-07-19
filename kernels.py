import math
import numpy as np

# returns 3x3 matrix of specified kernel
def get_kernel(kernel_name):
	dimensions = (3,3)
	match kernel_name:
		case "identity":
			return identity(dimensions)
		case "blur":
			return average_blur(dimensions)
		case "gaussian blur":
			return gaussian_blur(9)
		case "x sobel":
			return x_sobel(dimensions)
		case "y sobel":
			return y_sobel(dimensions)
		case "none":
			return np.zeros(dimensions)
		case other:
			raise Exception("kernels.py: Invalid kernel name.")

def identity(dimensions):
	result = np.zeros(dimensions)
	result[math.floor(dimensions[0]/2)][math.floor(dimensions[1]/2)] = 1
	return result

def average_blur(dimensions):
	return np.ones(dimensions)/(dimensions[0]*dimensions[1])

def x_sobel(dimensions):
	return np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])

def y_sobel(dimensions):
	return np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

# code modified from @clemisch 
# create a gaussian kernel
# @param sigma controls blur intensity
def gaussian_blur(side=9, sigma=100.0):
    ax = np.linspace(-(side - 1) / 2., (side - 1) / 2., side)
    gauss = np.exp(-0.5 * np.square(ax) / np.square(sigma))
    kernel = np.outer(gauss, gauss)
    return kernel / np.sum(kernel)
