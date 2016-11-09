# print out the first n primes
import numpy as np 
import matplotlib.pyplot as plt 
import sys
import math

if len(sys.argv) < 3:
    n = 1000
else:
    n = sys.argv[1]

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def get_primes(n, lower=2):
    primes = np.array([])
    number = lower
    i = 0
    while i < int(n):
        if is_prime(number):
            primes = np.append(primes, number)
            i+=1
        number+=1
    return primes

def main(n=1000,lower=2):

    # primes = get_primes(n, lower)

    # one_list = [i for i in primes if i%10 == 1 ]
    # three_list = [i for i in primes if i%10 == 3 ]
    # seven_list = [i for i in primes if i%10 == 7 ]
    # nine_list = [i for i in primes if i%10 == 9 ]

    # print len(one_list), len(three_list), len(seven_list), len(nine_list)
    # Idea: plot length of 1's list versus n as n grows
    # repeat for 3's, 7's and 9's list
    for m in xrange(int(n)):

        primes = get_primes(m)

        one_list = np.array([i for i in primes if i%10 == 1 ])
        three_list = np.array([i for i in primes if i%10 == 3 ])
        seven_list = np.array([i for i in primes if i%10 == 7 ])
        nine_list = np.array([i for i in primes if i%10 == 9 ])

        plt.plot(m, len(one_list), 'b.', m, len(three_list), 'r.', m, len(seven_list), 'g.', m, len(nine_list), 'c.')
    # Line of best fit
    # least squares method
    plt.xlabel('natural numbers')
    plt.ylabel('number of primes ending in 1,3,7, and 9')
    plt.title('Number of primes ending in 1,3,7 or 9 \n in a list of the first n natural numbers')
    plt.show()
    # Conclusion: number of primes ending in 1,3,7, and 9 remain about the same as
    # the list of primes grow.

    # Other things to look at:
    #  - sparsity of primes
    #  - distribution of primes as n list grows
    #  - ...




if __name__ == '__main__':
    main(n)
    # print get_primes(sys.argv[1])