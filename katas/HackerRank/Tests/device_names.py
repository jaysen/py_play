#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'deviceNamesSystem' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY devicenames as parameter.
#

def deviceNamesSystem2(devicenames):
    # create a dict to store names and counts:
    name_counts = {}
    result = []

    for device in devicenames:
        if device not in name_counts:
            # create a entry for the device and set its count to 1, then use the device name as is.
            name_counts[device] = 0
            result.append(device)
        else:
            # get the current count, add 1 to it, then append the count to the device name and use it in result
            count = name_counts[device]
            count = count + 1
            name_counts[device] = count
            name = device + str(count)
            result.append(name)

    return result


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # devicenames_count = int(input().strip())
    #
    # devicenames = []
    #
    # for _ in range(devicenames_count):
    #     devicenames_item = input()
    #     devicenames.append(devicenames_item)
    #
    # result = deviceNamesSystem(devicenames)
    #
    # fptr.write('\n'.join(result))
    # fptr.write('\n')
    #
    # fptr.close()


    devicenames = ['switch','tv','switch','tv','switch','tv']
    print(deviceNamesSystem2(devicenames))