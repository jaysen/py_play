
def find_number(arr, k):
    return 'YES' if k in arr else 'NO'

def print_odd_numbers(l, r):
    odd_arr = [i for i in range(l, r+1) if i % 2 != 0]
    return odd_arr