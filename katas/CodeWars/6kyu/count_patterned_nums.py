# CodeWars 6kyu
# https://www.codewars.com/kata/55d8aa568dec9fb9e200004a/

def count_nums(upper_limit, max_diff):
    """
    Return the number of integers between 0 and upper_limit
    - that have no repeated digits.
    - digits increase only (1234) not (453)
    - that have a difference no more than max_diff between their digits.
    """
    if upper_limit < 12:
        return 0
    if max_diff <= 0:
        return 0

    count = 0
    for i in range(12, upper_limit+1):
        if is_valid(i, max_diff):
            count += 1
    return count


def is_valid(num, max_diff):
    """
    Return True if num has no repeated digits and the difference between
    each digit is no more than max_diff.
    """
    # convert num to an array of digits
    digits = [int(x) for x in str(num)]

    # check for repeated digits
    if len(digits) != len(set(digits)):
        return False

    # check for increasing digits
    if digits != sorted(digits):
        return False

    # check for max_diff
    for i in range(0, len(digits)-1):
        if (digits[i+1] - digits[i]) > max_diff:
            return False
    return True



print(count_nums(0, 1))
print(count_nums(12, 1))
print(count_nums(30, 2))
print(count_nums(50, 3))


