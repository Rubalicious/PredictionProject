import numpy as np
import matplotlib.pyplot as plt
import sys

def triangular(n):
	return np.sum([i for i in xrange(n+1)])

def main(n=1):
	# generate the first n triangular numbers
	tris = np.array([triangular(i) for i in xrange(1,n+1)])

	# generate the first n square numbers
	squas = np.array([i*i for i in xrange(1,n+1)])
	
	tri_and_sq = []
	# while len(tri_and_sq) != 3:
		# tri_and_sq.append()
	# print tris , squas
	# print list(np.intersect1d(tris, squas))

	# Test theory: if the nth triangular number + (n-1)n/2 = n^2,
	# then nth triangular + (n-1)n/2 is a triangular number.

	# if triangular(n) + n*(n-1) == n**2:
	# 	print True
	# else:
	# 	print False

	# Generate the list m = sqrt(n(n+1)/2), for n in integers
	tri = [int(np.sqrt(i*(i+1)/2)) for i in xrange(1,n) if np.sqrt(i*(i+1)/2) - np.round(np.sqrt(i*(i+1)/2)) == 0]
	sq = [int(.5*(np.sqrt(8*m**2+1)-1)) for m in xrange(1,n) if .5*(np.sqrt(8*m**2+1)-1) - np.round(.5*(np.sqrt(8*m**2+1)-1)) == 0]
	# tri_list = [k for k in test_list if k - round(k) == 0]
	print tri
	print sq

	# plot the gradient between points in the list
	grad = [(sq[i]- sq[i-1])/(tri[i] - tri[i-1]) for i in xrange(len(tri))]

	plt.plot(tri, sq, 'ko')
	plt.axis([0, 10000, 0, 10000])

	plt.figure()
	plt.plot(grad, range(len(grad)), 'b-')
	plt.show()
	
	# print tri_list	


if __name__ == '__main__':
	p = int(sys.argv[1])
	main(p)