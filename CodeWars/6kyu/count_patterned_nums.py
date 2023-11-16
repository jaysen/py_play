
def count_nums(upper_limit, max_diff):
    """
    Return the number of integers between 0 and upper_limit
    - that have no repeated digits.
    - digits increase only (1234) not (453)
    - that have a difference no more than max_diff between their digits.
    """
    if upper_limit < 12:
        return 0
    if max_diff == 0:
        return 0

    count = 0
    for num in range(12, upper_limit+1):
        # split num into digits:
        digits = [int(x) for x in str(num)]

        # check for repeated digits: (nice pattern for that)
        if len(digits) != len(set(digits)):
            continue

        # check for increasing digits: (nice pattern for that)
        if digits != sorted(digits):
            continue

        # check for max_diff between digits:
        ok_diffs = True
        for i in range(0, len(digits)-1):
            if (digits[i+1] - digits[i]) > max_diff:
                ok_diffs = False
                break

        if ok_diffs:
            count += 1

    return count


print(count_nums(0, 1))
print(count_nums(12, 1))
print(count_nums(30, 2))
