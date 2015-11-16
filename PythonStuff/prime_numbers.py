#finding factors of numbers
#testing and proving the fundamental theorem of arithmetic

def find_factors(n):
    factors = []
    for i in range(1,n+1):
        if n%i == 0:
            factors.append(i)
    return factors

def isPrime(n):
    number = find_factors(n)
    if len(number) == 2:
        return True
    else:
        return False

def primes_less_than(n):
    #TO-DO
    #complete this

        
        
find_factors(144)
isPrime(144)
isPrime(2)
isPrime(7)
isPrime(1807)
