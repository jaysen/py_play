#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findMedian(arr):
    #sort array:
    arr.sort()
    #get middle index:
    middle = len(arr) // 2
    #since input array is odd, middle index is the median:
    return arr[middle]


if __name__ == '__main__':