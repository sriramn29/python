import math

def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s * s == x

def isFibonacci(n):
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)

Start = int(input())
End = int(input())
for i in range(Start, End):
    if(isFibonacci(i) == True):
        print(i, "is a fibonacci number")
    else:
        print(i, "is not a fibonacci number")