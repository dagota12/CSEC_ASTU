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
    count =0
    for i in range(len(a)):
        for j in range(0,len(a)-1-i):
            if(a[j] > a[j+1]):
                count+=1
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
    print("Array is sorted in %d swaps."%(count))
    print("First Element: %d"%(a[0]))
    print("Last Element: %d"%(a[-1]))
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
