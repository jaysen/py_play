# https://www.hackerrank.com/test/4nahpm20m33/questions/di1dm3kpigj
from numpy import array

def flipping_matrix(matrix):
    """
    Using only row and col reverse moves, return the maximum sum of the upper left quadrant...
    :param arr: a 2d array of int
    :return: max sum of upper left quadrant
    """

    quad_size = len(matrix)//2
    end = len(matrix) - 1

    # insight: for each value in the quadrant, use the maximum of the values symmetrically opposite in other quadrants:

    # loop through each element of upper left quadrant:
    quad_sum = 0
    for i in range(0, quad_size):
        for j in range(0, quad_size):
            #print()
            #print(i, j)

            # for each [i,j] in upper left quad, get the symmetrically opposite value in the other 3 quadrants:
            upper_left = matrix[i, j]
            #print(f"upper_left = {upper_left}")

            upper_right = matrix[i, end-j]
            #print(f"upper_right = {upper_right}")

            lower_left = matrix[end-i, j]
            #print(f"lower_left = {lower_left}")

            lower_right = matrix[end-i, end-j]
            #print(f"lower_right = {lower_right}")

            #print(max(upper_left, upper_right, lower_left, lower_right))
            quad_sum += max(upper_left, upper_right, lower_left, lower_right)

    return quad_sum


a = [[112, 42,  83,  119],
     [56,  125, 56,  49],
     [15,  78,  101, 43],
     [62,  98,  114, 108]]

m = array(a)
print()
print(flipping_matrix(m))



