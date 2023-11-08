import math


# determine if a number is prime
def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


# version 2 - more efficient.
def is_prime_v2(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True


# return a list of all primes up to n
def primes(n):
    return [i for i in range(1, n) if is_prime(i)]


# version 2 - more efficient of primes
def primes_v2(n):
    return [i for i in range(1, n) if is_prime_v2(i)]


print(primes(10001))
print(primes_v2(10001))
