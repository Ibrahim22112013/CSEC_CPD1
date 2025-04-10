#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    mat=[]
    for elements in range(len(arr)-1):
        ind=len(arr)-1-elements
        last=arr[ind]
        before=arr[ind-1]
        if last<before:
            new=[]
            new.extend(arr)
            new[ind]=new[ind-1]
            arr[ind],arr[ind-1]=arr[ind-1],arr[ind]
            mat.append(new)
    else:
        mat.append(arr)
        
    return mat
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    odd=insertionSort1(n, arr)
    for i in odd:
        for j in i:
            print(j,end=" ")
        print()
    
    
    
    
    
