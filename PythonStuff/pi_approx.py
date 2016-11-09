import numpy as np 
import matplotlib.pyplot as plt

def main(num_of_pnts=100000):
	# generate a random points inside the axes [0, 1, 0, 1]
	x_pnts = np.random.uniform(0, 1, num_of_pnts)
	y_pnts = np.random.uniform(0, 1, num_of_pnts)

	plt.figure()
	plt.axis([0, 1, 0, 1])
	circle = plt.Circle((0,0),1, fill=False)
	ax = plt.gca()
	ax.add_artist(circle)

	# simulation plot
	step_size = 16 # plotting subplot of total number of points
	for x, y in zip(x_pnts[0:-1:step_size],y_pnts[0:-1:step_size]):
		if x**2+y**2 > 1:
			plt.plot(x,y, 'r.')
		else:
			plt.plot(x,y,'b.')

	# counting number of points within quarter circle
	pnts = zip(x_pnts,y_pnts)
	count = 0.0 
	for x,y in pnts:
		if np.power(x,2)+np.power(y,2) <= 1:
			count+=1
	
	# Approximation of pi
	pi = 4*count/num_of_pnts
	plt.title('pi is approximately %.5f'%pi)
	plt.xlabel('x-axis')
	plt.ylabel('y-axis')

	# Error calculation
	error = np.absolute(np.pi - pi)
	print 'error as absolute distance from numpy\'s pi is %.5f'%error
	plt.show()


if __name__ == '__main__':
	main()