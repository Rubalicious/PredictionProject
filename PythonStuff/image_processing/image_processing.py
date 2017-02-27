from PIL import Image
import numpy as np 
import pandas as pd
import sys
from tools import *

def encode_pixel(binary, parsed_bits):
	return binary[:-2] + parsed_bits

def diff(list1, list2):
	count = 0
	for a,b in zip(list1, list2):
		if tuple(a) != tuple(b):
			print a, b
		else:	count += 1
	return count

def main(filename, secret_message):
	im = Image.open(filename)
	# im.show()
	width, height = im.size
	area = width*height
	pixels = np.array([ im.getpixel((i,j)) for i in xrange(width) for j in xrange(height) ])
	binary_pixels = np.array([(bin(r), bin(g), bin(b)) for (r,g,b) in pixels])
	encoded_pixels = np.copy(binary_pixels)
	# idea: check to see if I can convert encoded pixels (a copy) back into an Image object


	binary_msg = np.array([bin(ord(i)) for i in secret_message])
	parsed_bin_msg = np.array([(string[-6:-4], string[-4:-2], string[-2:]) for string in binary_msg ])

	# hash values of each letter
	hash_values = np.array([ hash(i) %area for i in secret_message])

	# map each value to a pixel
	# for each letter in the binary_msg, 
		# choose a pixel - the hashed value of the binary letter
		# edit the pixel's (r,g,b) values with the parsed_bin_msg
	i = 0
	for letter in binary_msg:
		r,g,b = binary_pixels[hash_values[i]]
		# if i == 0:	print r,g,b 
		en_r, en_g, en_b = parsed_bin_msg[i]
		n_r = encode_pixel(r, en_r)
		n_g = encode_pixel(g, en_g)
		n_b = encode_pixel(b, en_b)
		# if i == 0:	print encoded_pixels[hash_values[i]]
		encoded_pixels[hash_values[i]] = (n_r, n_g, n_b)
		# if i == 0:	print encoded_pixels[hash_values[i]]
		i+=1

	# print encoded_pixels

	encoded_im = np.array([(int(r,2), int(g, 2), int(b, 2)) for (r,g,b) in encoded_pixels])
	print encoded_im[hash_values[0]]
	print pixels[hash_values[0]]
	print type(encoded_im), type(pixels)
	print diff(encoded_im, pixels)
	print i, area

	# print type(encoded_im)
	new_im = Image.fromarray(encoded_im, 'RGB')
	# new_im.save('encodedmsg.jpg')
	# print encoded_im, len(encoded_im)
	new_im.show()
	im.show()


def main2(filename):
	im = Image.open(filename)
	# im.show()
	width, height = im.size
	area = width*height
	pixels = np.array([ im.getpixel((i,j)) for i in xrange(width) for j in xrange(height) ]).reshape(im.size)



if __name__ == '__main__':
	# main(sys.argv[1], sys.argv[2])
	main2(filename)


