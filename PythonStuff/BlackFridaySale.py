# This script is inpired by the following question
# 
# N people are standing in a single file line before a Black Friday sale. How many of them, on
# average, would be taller than everyone in front of them?

# I will tackle this by permuting the first N natural numbers
# and counting the number of integers greater than all integers before it
# repeat experiment 50 times and take average of results
import numpy as np 
import itertools
# import factorial as f
import matplotlib.pyplot as plt

# this will iterate through a list of tuples
# and count the number of "peak" integers
# for each list and return the list of
# number of "peak" integers
# Note:	a "peak" integer is one that is greater
# than every integer before it
def tall_count(permutations):
	peaks = np.array([])
	M = len(permutations[0])
	for perm in permutations:
		peak = perm[0] 		# the first element of a permutation is a peak
		count = 1			# count number of peak integers
		for k in perm:
			if k > peak:
				count +=1
				peak = k
		peaks = np.append(peaks,count)
	return peaks

def main(N):
	first_N = np.array([i for i in xrange(1, N+1)])
	permutations = list(itertools.permutations(first_N))
	count = tall_count(permutations)
	average = np.average(count)
	# M = f.factorial(N)
	return average

def plot(N):
	averages = np.array([main(i) for i in xrange(1, N+1)])
	plt.plot([i for i in xrange(1, N+1)], averages)
	plt.title("Average number of people who are taller than everyone in front of them in N people")
	plt.xlabel("for N people")
	plt.ylabel("Average number of taller-than-everyone-people")
	plt.show()

if __name__ == '__main__':
	main()