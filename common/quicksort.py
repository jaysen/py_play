
# katas implementation of quicksort:
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()
        lesser = [x for x in arr if x <= pivot]
        greater = [x for x in arr if x > pivot]
        return quicksort(lesser) + [pivot] + quicksort(greater)


# test it out:
print(quicksort([1, 3, 17, 2, 5, 4, 38]))
print(quicksort([1, 3, 17, 2, 5, 4, 38, 1, 90, 38]))