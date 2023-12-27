
import sys

memo = {}


def fibo(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
        return n
    else:
        memo[n] = fibo(n-1) + fibo(n-2)
        return memo[n]


if __name__ == '__main__':
    if len(sys.argv) > 1:
        x = int(sys.argv[1])
    else:
        x = int(input("Enter a number: "))

    for i in range(x+1):
        print(fibo(i), end=" ")
