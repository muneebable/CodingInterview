#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    min = 0
    max = 0
    all_sum = []
    if len(arr) == 0:
        print(min, max)
        return
    arr = sorted(arr)
    arr_mx = arr[-4:]
    arr_min = arr[0:4]
    print(sum(arr_min), sum(arr_mx))
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
