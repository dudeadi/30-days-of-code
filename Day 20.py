#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
swaps = 0
for x in range(n):
    cswap = 0
    for y in range (n-1):
        if a[y] > a[y+1]:
            a[y],a[y+1] = a[y+1],a[y]
            swaps += 1
            cswap += 1
    if cswap == 0:
        break
print('Array is sorted in '+str(swaps)+' swaps.')
print('First Element: '+str(a[0]))
print('Last Element: '+str(a[n-1]))