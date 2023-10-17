# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec
# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence,
# which is the number of times you must multiply the digits in num until you reach a single digit.

# 39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
def digit_count(n):
    return len(str(n))


def multiply_digits(n):
    n_str = str(n)
    product = 1
    for digit in n_str:
        product = int(digit) * product
    return product


def persistence(n):
    if digit_count(n) == 1:
        return 0
    n_mult = multiply_digits(n)
    if digit_count(n_mult) == 1:
        return 1
    else:
        return persistence(n_mult) + 1


print(multiply_digits(39))

print(digit_count(14))
print(digit_count(12345))
print(digit_count(12345689324618934638476189346731289346))

print(persistence(39))

