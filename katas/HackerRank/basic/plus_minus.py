#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plus_minus_v1(arr):

    arr_neg = [x for x in arr if x < 0]
    arr_pos = [x for x in arr if x > 0]
    arr_zero = [x for x in arr if x == 0]

    ratio_neg = len(arr_neg) / len(arr)
    ratio_pos = len(arr_pos) / len(arr)
    ratio_zero = len(arr_zero) / len(arr)

    print(f"{ratio_pos:.6f}")
    print(f"{ratio_neg:.6f}")
    print(f"{ratio_zero:.6f}")


# an optimised version of plusMinus:
def plus_minus(arr):
    arr_neg = 0
    arr_pos = 0
    arr_zero = 0

    for x in arr:
        if x < 0:
            arr_neg += 1
        elif x > 0:
            arr_pos += 1
        else:
            arr_zero += 1

    ratio_neg = arr_neg / len(arr)
    ratio_pos = arr_pos / len(arr)
    ratio_zero = arr_zero / len(arr)

    print(f"{ratio_pos:.6f}")
    print(f"{ratio_neg:.6f}")
    print(f"{ratio_zero:.6f}")


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plus_minus(arr)


