# 
# 	Author: Ruby Abrams
# 	Descriptions:
# 			This script will output the set of pairs of integers 
# 			that solve the the equation m*m + n*n = k for given
# 			command line argument integer k.
# 

import sys
import numpy as np

def main(k):
	if float(k) < 0 or float(k) != int(k):
		print("The input is not a positive integer")
		return

	# find the set of 2-tuples whose sum of squares equals k
	forms = np.array([(a,b) for a in xrange(int(k)) for b in xrange(int(k)) if a**2+b**2 == int(k) ])
	print forms


if __name__ == '__main__':
	main(sys.argv[1])