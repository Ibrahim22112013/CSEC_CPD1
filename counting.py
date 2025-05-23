#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    new=99*[0]+[0]
    for i in arr:
        new[i]+=1
    return new

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)
    for j in result:
        print(j,end=" ")

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
