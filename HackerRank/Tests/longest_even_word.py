#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'longestEvenWord' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#


# function to return the FIRST longest even word in a sentence:
def longestEvenWord(sentence):
    words = sentence.split()
    even_words = []

    for word in words:
        # if word length is even add it to list of even_words:
        if len(word) % 2 == 0:
            even_words.append(word)

    if len(even_words) == 0:
        return "00"
    else:
        # sort even_words list by length in descending order:
        even_words.sort(key=len, reverse=True)
        # return the longest word that is first in list -
        # because Python's sort is stable the first largest is at start of list:
        return even_words[0]


def longestEvenWord2(sentence):
    words = sentence.split()
    longest_even_word = "00"
    max_length = 0

    # iterate through sentence and compare in place:
    for word in words:
        if len(word) % 2 == 0 and len(word) > max_length:
            max_length = len(word)
            longest_even_word = word

    return longest_even_word


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # sentence = input()
    #
    # result = longestEvenWord(sentence)
    #
    # fptr.write(result + '\n')
    #
    # fptr.close()

    sentence = "time to write great code"
    print(longestEvenWord2(sentence))
