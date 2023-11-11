# Binary Search implementation on a SORTED array:

def bin_search(arr, target):
    if not arr:
        return False
    middle = len(arr) // 2
    if arr[middle] == target:
        return True
    elif arr[middle] < target:
        return bin_search(arr[middle + 1:], target)
    else:
        return bin_search(arr[:middle], target)


# test it out:
print(bin_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
print(bin_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 10))
print(bin_search([1, 2, 3, 4, 5, 6, 7, 8, 9], -1))

# big tests:
from numpy import random

big_test = random.randint(1, 100_000_000, 100_000_000)
big_test.sort()
# convert list to array
big_test = big_test.tolist()
print(bin_search(big_test, 1000000))
print(bin_search(big_test, 1))
print(bin_search(big_test, 500000))
