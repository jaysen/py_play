# Question: Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
# Your solution should run in O(n) time complexity.
#
# For example, given [100, 4, 200, 1, 3, 2], the longest consecutive elements sequence is [1, 2, 3, 4].
# So the function should return 4.

def longest_seq(arr):
    num_set = set(arr)
    max_length = 0

    for el in arr:
        current_length = 0
        seq_max = el + 1
        if seq_max in num_set:
            current_length += 1
            while seq_max in num_set:
                seq_max += 1
                current_length += 1

            max_length = max(max_length, current_length)

    return max_length

test_arr = [100, 4, 200, 1, 3, 2, 101, 102, 103, 1]
print(longest_seq(test_arr))



## solve this using dynamic programming

def longest_seq_dp(arr):

    num_set = set(arr)
    max_length = 0
    memo = {}

