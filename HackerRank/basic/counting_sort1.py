# HackerRank: Counting Sort 1
# https://www.hackerrank.com/challenges/one-week-preparation-kit-countingsort1/
# Once you have this count_array, sorting is essentially done
# - just walk through count_arr and for each index i output count_arr[i] number of i

def counting_sort(arr):
    """
    Given an array arr as input, return the count_array where the index represents the number of times that index number
     exists in the input array
    The max value in arr is 100
    :param arr: the array to be represented in the count array
    :return: the count-array, size 100 - with counts of each num in count_arr[num
    """

    count_arr = [0] * 100
    for i in arr:
        count_arr[i] += 1
    return count_arr


if __name__ == '__main__':

    array1 = [63, 25, 73, 1, 98, 73, 56, 84, 86, 57, 16, 83, 8, 25, 81, 56, 9, 53, 98, 67, 99, 12, 83, 89, 80, 91, 39, 86,
              76, 85, 74, 39, 25, 90, 59, 10, 94, 32, 44, 3, 89, 30, 27, 79, 46, 96, 27, 32, 18, 21, 92, 69, 81, 40, 40, 34,
              68, 78, 24, 87, 42, 69, 23, 41, 78, 22, 6, 90, 99, 89, 50, 30, 20, 1, 43, 3, 70, 95, 33, 46, 44, 9, 69, 48,
              33, 60, 65, 16, 82, 67, 61, 32, 21, 79, 75, 75, 13, 87, 70, 33]

    count_arr1 = counting_sort(array1)
    print(count_arr1)

    sorted_array1 = []
    for i in range(0, len(count_arr1)-1):
        #print(count_arr1[i]*[i])
        sorted_array1.extend(count_arr1[i]*[i])
    print(sorted_array1)
    print(sorted(array1))

