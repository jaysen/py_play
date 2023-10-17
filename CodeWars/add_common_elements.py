# Common array elements
# https://www.codewars.com/kata/5a6225e5d8e145b540000127/train/python
# Given three arrays of integers, return the sum of elements that are common in all three arrays.


from collections import Counter


def common(arr1, arr2, arr3):
    # Count the elements in each array
    counter1 = Counter(arr1)
    counter2 = Counter(arr2)
    counter3 = Counter(arr3)

    # Find the intersection of the three arrays (i.e., elements common to all arrays)
    common_elements = list((counter1 & counter2 & counter3).elements())

    # Return the sum of the common elements
    return sum(common_elements)


a = range(1, 10000)
b = range(50, 150000)
c = range(0, 20000)

print(common(a, b, c))
