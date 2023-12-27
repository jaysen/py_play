#Question: Given a list of non-negative integers, arrange them such that they form the largest number.
# For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

#Note: The result may be very large, so you need to return a string instead of an integer.

def largest_number_string(nums):
    # convert nums to strings:
    nums = [str(x) for x in nums]

    # Sort the strings using custom sort key:
    nums.sort(reverse=True, key=sort_key)

    # join the strings:
    return "".join(nums)


# Custom sort key
# This works because "33" > "300"
# i.e. string comparison is done character by character
def sort_key(x):
    return x*10  # Extend the string to ensure proper comparison


nums = [3, 300, 34, 5, 9, 91]
print(largest_number_string(nums))
