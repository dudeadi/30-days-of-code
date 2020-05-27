import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
arr_max = -10000

for rows in range(len(arr)-2):
    for col in range(len(arr[rows])-2):
        top_left = arr[rows][col]
        top_centre = arr[rows][col+1]
        top_right = arr[rows][col+2]
        middle = arr[rows+1][col+1]
        bottom_left=arr[rows+2][col]
        bottom_centre = arr[rows+2][col+1]
        bottom_right = arr[rows+2][col+2]
        summ = top_left+top_centre+top_right+middle+bottom_left+bottom_right+bottom_centre
        arr_max = max(arr_max,summ)

print(arr_max)
