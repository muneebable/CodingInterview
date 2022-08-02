#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(sam_start, sam_end, apple_pos, orange_pos, apples, oranges):
    # Write your code here
    # For apples
    sam_house = [sam_start, sam_end]
    new_apple = [i + apple_pos for i in apples]
    new_orange = [i + orange_pos for i in oranges]
    
    count_apple = 0
    count_orange = 0
    for i in new_apple:
        if i in range(sam_start, sam_end+1):
            count_apple+=1
        continue
    
    for i in new_orange:
        #print(i)
        if i in range(sam_start, sam_end+1):
            count_orange+=1
        continue
    print(count_apple)
    print(count_orange)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    sam_start = int(first_multiple_input[0])

    sam_end = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    apple_pos = int(second_multiple_input[0])

    orange_pos = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(sam_start, sam_end, apple_pos, orange_pos, apples, oranges)
