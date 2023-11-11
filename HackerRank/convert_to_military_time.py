#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    #expect time in format: hh:mm:ssAM or hh:mm:ssPM
    #split string into list:
    time_list = s.split(':')
    #get AM or PM:
    am_pm = time_list[-1][-2:]
    #get hours:
    hours = int(time_list[0])
    if am_pm == 'PM':
        if hours < 12:
            hours += 12
    else:
        if hours == 12:
            hours = 0
    #convert hours to string:
    hours = str(hours)
    #add leading zero if needed:
    if len(hours) == 1:
        hours = '0' + hours
    #replace hours in list:
    time_list[0] = hours
    #remove AM or PM:
    time_list[-1] = time_list[-1][:-2]
    #join list into string:
    time = ':'.join(time_list)
    return time



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
