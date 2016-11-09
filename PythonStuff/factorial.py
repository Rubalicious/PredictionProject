import sys

def factorial(n):
	if n<0:	return "factorial not defined for negative numbers"
	elif n == 1 or n==0: return 1
	else:
		return n*factorial(n-1)

if __name__ == '__main__':
	print factorial(int(sys.argv[1]))