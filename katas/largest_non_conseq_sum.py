###
# Problem Statement:
# "You are given an array of integers. Write a function that returns the largest sum of non-adjacent numbers.
# Numbers can be 0 or negative.
#
# For example:
#
#    For the array [3, 2, 7, 10], the function should return 13 (sum of 3 and 10).
#    For the array [3, 2, 5, 10, 7], the function should return 15 (sum of 3, 5, and 7).
#
# Clarifications:
#
#    Non-adjacent numbers mean any numbers in the array that are not next to each other.
#    You need to find the subset of numbers that gives the maximum sum under this condition."

def largest_non_adjacent_sum__not_working(arr):
    max_sum = 0

    # [3, 2, 7, 10]
    inc_sum = arr[1]  # = 3
    exc_sum = arr[0]  # = 2
    for e in arr[2:]:  # e=10
        exc_sum, inc_sum = inc_sum, exc_sum  # swap them -> inc = 2, exc = 10
        inc_sum += e  # 2 + 10 = 12
        max_sum = max(exc_sum, inc_sum)  # max (10, 12) = 12
    return max_sum


test_arr = [3, 2, 7, 10]
print(largest_non_adjacent_sum__not_working(test_arr))
test_arr = [3, 2, 5, 10, 7]
print(largest_non_adjacent_sum__not_working(test_arr))


def largest_non_adjacent_sum(arr):

    # [3, 2, 7, 10]
    incl_sum = max(arr[0], 0)  # = 3
    excl_sum = 0
    for e in arr[1:]:  #
        new_excl_sum = max(excl_sum, incl_sum)
        incl_sum = excl_sum + e
        excl_sum = new_excl_sum
    return max(incl_sum, excl_sum)


test_arr = [3, 2, 7, 10]
print(largest_non_adjacent_sum(test_arr))
test_arr = [3, 2, 5, 10, 7]
print(largest_non_adjacent_sum(test_arr))


# using dynamic programming:

def largest_non_adjacent_sum_dp(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    dp = [0] * len(nums) # create a list of 0s the same length as nums
    dp[0] = nums[0] # set the first element of dp to the first element of nums
    dp[1] = max(nums[0], nums[1]) # set the second element of dp to the max of the first two elements of nums
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], nums[i] + dp[i-2]) # set the current element of dp to the max of the previous element of dp and the current element of nums plus the element two indices back in dp
    return dp[-1] # return the last element of dp