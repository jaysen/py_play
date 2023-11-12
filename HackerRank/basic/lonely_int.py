# Given an array of integers, where all elements but one occur twice, find the unique element
# https://www.hackerrank.com/challenges/one-week-preparation-kit-lonely-integer


def find_lone_int(a):
    counter = {}
    for i in range(len(a)):
        #add count for arr[i]
        if a[i] in counter:
            counter[a[i]] += 1
        else:
            counter[a[i]] = 1

    # return the key with value == 1
    key_list = list(counter.keys())
    val_list = list(counter.values())
    ind = val_list.index(1)
    return key_list[ind]


arr = [1,2,3,4,3,2,1]
print(find_lone_int(arr))





