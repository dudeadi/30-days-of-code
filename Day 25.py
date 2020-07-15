
import math
def IsPrime(p):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i is 0:
            return False
    return True


T = int(input())
for _ in range(T):
    n = int(input())
    
    if n >= 2 and IsPrime(n):
        print("Prime")
    else:
        print("Not prime")


