# Given a number, return its primefactors
import sys
import numpy as np
from prime_numbers import get_primes

def get_prime_factors(num):
	if num < 2:		raise Exception('not decomposable into prime factors')
	primes = [np.asscalar(p) for p in get_primes(num) if p < num]
	composite = np.asscalar(np.copy(num))
	factors = []
	index = 0
	while index < len(primes):
		primf = primes[index]
		# check if the composite number is factorable
		# by a primefactor
		while composite%primf == 0:
			composite /= primf
			factors.append(primf)
		index += 1
	
	if not [int(k) for k in factors]: return [1, num]
	else: 	return [int(k) for k in factors]
	# print('\n'.join('{}: {}'.format(*k) for k in enumerate(factors)))

# returns an ordered list of multiplicity of each prime number
# for a given set of prime factors of a number
def exp_representaion(factors):
	uniq_primes = np.unique(factors)
	num = 1
	for f in factors:	num*=f
	primes = [np.asscalar(p) for p in get_primes(num) if p < num]

	exp_repr = []
	for p in primes:
		count = 0
		for f in factors:
			if p == f:
				count+=1
		exp_repr.append(count)
	return exp_repr

def main(num):
	sums = []
	for i in xrange(2,num):
		factors = get_prime_factors(i)
		exp_rep = exp_representaion(factors)
		print exp_rep
		sums.append(np.sum(exp_rep))
	
	print '\n',sums

if __name__ == '__main__':
	print get_prime_factors(int(sys.argv[1]))
