# GCD calculator
import sys

def gcd(a,b):
    while a%b != 0:
        r = a%b
        p = (a-r)/b
        a = b
        b = r
    return b

def main(a,b):
    print gcd(a,b)

main(int(sys.argv[1]), int(sys.argv[2]))
