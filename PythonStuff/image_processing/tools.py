from PIL import Image
import numpy as np 
import pandas as pd
import sys

# pass in pixel1, and pixel2 as np arrays
def directional_derivative(pixel1, pixel2):
	return pixel1 - pixel2

# pass in a pixel as an np array
def norm(pixel):
	return np.inner(pixel, pixel)

def edge_detection(pixel, epsilon, image, n):
	# find norms of all neighboring pixels
	# get a list of neighbouring pixels
	# n = 3 # this corresponds to precision
	(x,y) = pixel
	nbrs = image[x-n:x+n+1,y-n:y+n+1]
	derivatives = [directional_derivative(image[x,y], p) for p in nbrs if image[x,y] != p]
	norms = [norm(p) for p in derivatives]
	sup = max(norms)

	if sup > epsilon:
		image[x,y] = (0,0,0) # set pixel to black

