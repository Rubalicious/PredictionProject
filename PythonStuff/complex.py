from ast import literal_eval
import numpy as np 
import matplotlib.pyplot as plt 
import itertools, copy

def sizeof(z):		return np.sqrt(z.real**2 + z.imag**2)

def map_(z, c=0):	return (z)**2 + c

def to_complex(u):	return np.complex(u[0], u[1])

def in_M(z):
	c = copy.copy(z)
	count = 0
	while sizeof(z) <=2:
		if count > 200: return True
		z = map_(z, c)
		count+=1
	return False


def main():
	grid_size = 100
	# make a 400x400 grid that sits 
	# within the window [-2-2i, 2+2i]
	axis = [4*float(i)/grid_size - 2 for i in xrange(grid_size)]
	grid = [e for e in itertools.product(axis, axis)]

	# we start with z_0 = 0 and C to be a point on the grid
	# then z_1 = z_0^2 + C = C
	# convert each point in the grid into a complex number
	count, total = 0, len(grid)
	for u in grid:
		c = to_complex(u)
		if count %500 == 0: print 100*float(count)/total
		count+=1
		if in_M(c):
			plt.plot(u[0], u[1],'*k')


	plt.axis([-3,2,-2,2])
	plt.show()

def plot_data():
	try:
		f = open('data')
	except Exception, e:
		raise e
	data = f.read()

	if not f.closed:
		f.close()

	lines = data.split()
	l = [literal_eval(e) for e in lines]
	for u in l:
		plt.plot(u[0],u[1],'*k')
	plt.axis([-3,2,-2,2])
	plt.show()


if __name__ == '__main__':
	# main()
	plot_data()