#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    global count
    count=0
    for num in range(len(a)):
        for heg in range(len(a)-num-1):
            if a[heg]>a[heg+1]:
                a[heg],a[heg+1]=a[heg+1],a[heg]
                count+=1
    return a
                
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    k=countSwaps(a)
    print(f"Array is sorted in {count} swaps.")
    print(f"First Element: {k[0]}")
    print(f"Last Element: {k[-1]}")
