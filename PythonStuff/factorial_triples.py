import numpy as np 

def fact(n):
	if n == 0:	return 1
	return n*fact(n-1)

def power_of_2(n):
	i = 0
	while 2**i < n:	i+=1
	if 2**i == n:
		return 1
	else:	return 0

def main():
	n = 40
	triples = np.array([(a, b, c) for a in xrange(1,n) for b in xrange(1,n) for c in xrange(1,n) if power_of_2(fact(a)+fact(b)+fact(c)) and a>=b>=c])
	print triples

if __name__ == '__main__':
	main()