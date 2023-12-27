# https://www.hackerrank.com/challenges/one-week-preparation-kit-diagonal-difference/

arr = [
    [1,2,3],
    [4,5,6],
    [9,8,9]
]

print(arr)

def diagonal_diff(arr):
    diag1 = 0
    diag2 = 0
    for i in range(len(arr)):
        diag1 = diag1 + arr[i][i]
        diag2 = diag2 + arr[i][len(arr)-i-1]
    return abs(diag1 - diag2)

print(diagonal_diff(arr))
