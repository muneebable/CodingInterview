#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'mostActive' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY customers as parameter.
#

def mostActive(customers):
    # Write your code here
    dictionary = {}
    for cust in customers:
        dictionary[cust] = dictionary.get(cust, 0) + 1
    
    print(dictionary)
    percent = {k: (v / len(customers) *100) for k, v in dictionary.items()}
    print(percent)
    filter_less = {k: v for (k, v) in percent.items() if v >=5}
    print(filter_less)
    sorting = sorted(filter_less.keys(), key=lambda x:x) #, key=lambda x: x[1], reverse=False
    print(sorting)
    #result = [x[0] for x in sorting]
    return sorting
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    customers_count = int(input().strip())

    customers = []

    for _ in range(customers_count):
        customers_item = input()
        customers.append(customers_item)

    result = mostActive(customers)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
