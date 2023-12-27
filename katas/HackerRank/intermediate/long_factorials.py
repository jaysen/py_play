# extra long factorials
# https://www.hackerrank.com/challenges/extra-long-factorials/problem

# recursive implementation:
def factorials(n):
    if n == 1:
        return 1
    else:
        return n * factorials(n - 1)

# iterative implementation:
def long_factorials(n):
    total = 1
    while n > 1:
        total = total * n
        n -= 1
    return total

# iterative implementation v2:
def long_factorials_v2(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


if __name__ == '__main__':
    n = 5
    print(long_factorials(n))
    print(factorials(n))
    print(long_factorials_v2(n))

