def fib(n):
	if n == 0:
		return 1
	if n == 1:
		return 1
	else:
		return fib(n-1)+fib(n-2)

for i in range(31):
	print "the %s th term of the fibonacci sequence is %s" %(i,fib(i))
