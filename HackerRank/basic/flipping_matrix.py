# https://www.hackerrank.com/test/4nahpm20m33/questions/di1dm3kpigj
import numpy as np

def flipping_matrix(arr):
    """
    Using only row and col reverse moves, return the maximum sum of the upper left quadrant...
    :param arr: a 2d array of int
    :return: max sum of upper left quadrant
    """
    matrix = np.array(arr)
    quad_size = len(matrix)//2

    #column loop
    for i in range(0, len(matrix)):
        # check if quadrant portion is bigger after reverse
        if sum(matrix[:quad_size, i]) < sum(matrix[quad_size:, i]):
            matrix[:, i] = matrix[::-1, i]

    # row loop
    for i in range(0, len(matrix)):
        # check if quadrant portion is bigger after reverse
        if sum(matrix[i, :quad_size]) < sum(matrix[i, quad_size:]):
            matrix[i, :] = matrix[i, ::-1]

    print(matrix)
    print()
    return sum(sum(matrix[:quad_size,:quad_size]))


m = [[112, 42,  83, 119],
     [56,  125, 56, 49],
     [15,  78,  101, 43],
     [62,  98,  114, 108]]

print(np.array(m))
print()
print(flipping_matrix(m))



