#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])
        
        maximum = 0 
        for x in range(1,n):
            for y in range(x+1,n+1):
                z = x&y
                if k > z > maximum:
                    maximum = z
        print(maximum)


# Alternative

t = int(input().strip())
for a0 in range(t):
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    print(k-1 if ((k-1) | k) <= n else k-2)

