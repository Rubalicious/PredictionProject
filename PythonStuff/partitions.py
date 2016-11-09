import numpy as np 
import sys

def sub_partition(S):
	types = np.unique(S)
	tuple_number = choose(len(types),2)
	sub_partitions = []
	for i in types:
		for j in types:
			if i != j:
				# remove the first ith and jth elements
				S = [e for e in S]
				# add (i+j)th element
		sub_partitions = np.append(sub_partitions, new_p)

def get_partitions_of(num):
	p = np.array([1 for i in xrange(num)])
	types = np.unique(p)
	while len(p) > 1:
		if len(types) == 1: 
			p = np.append(p[:-2], sum(p[-2:]))
		else:
			# get the number of new elements that can be made
			tuple_number = choose(len(types),2)
			for i in xrange(tuple_number):
				p = 

def choose(n,k):
	return factorial(n)/(factorial(n-k)*factorial(k))

def factorial(n):
	if n == 1:	return 1
	else: return n*factorial(n-1)

if __name__ == '__main__':
	main(int(sys.argv[1]))