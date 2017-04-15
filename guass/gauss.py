# vector = [18, -3.0, 5.0]
#
# matrix = [
#     [-11.0, 3.0, 3.0],
#     [-2.0, -5.0, 1.0],
#     [1.0, -10.0, 8.0]
# ]
# vector = [1.75, -0.21, 0.27]
#
# matrix = [
#     [1.03, 5.46, 1.77],
#     [-0.25, -1.5, 0.50],
#     [0.16, 0.85, 0.34]
# ]
vector = [-5, -2, 1]

matrix = [
    [-2, 1, 4],
    [7, -3, 1],
    [3, -1, -7]
]

LEN = len(vector);

def pprint(m, v, x=None):
    for i, row in enumerate(m):
        row.append(v[i])
        print(row)
        row.pop()

    if (x != None):
        print()
        print(x)

    print('----------------------------------')

pprint(matrix, vector)

# Check if zeros on diagonal b/c that'll mean we need to divide by zero
for i, row in enumerate(matrix):
    if (row[i] == 0):
        raise ZeroDivisionError('Zero along the diagonal.')

print()
print('Forward eliminate')
print()

# forward eliminate
# current row, used for diagonal element
for i in range(0, LEN-1):
    # current element(s) below diagonal
    for j in range(i+1, LEN):
        # what we need to make [j,i] go to zero
        fraction = matrix[j][i] / matrix[i][i]

        # apply fraction to the row below the diagonal element
        for k in range(i, LEN):
            matrix[j][k] = matrix[j][k] - fraction * matrix[i][k]

        # apply fraction to the element in the same row of the vector
        vector[j] = vector[j] - fraction * vector[i]
        pprint(matrix, vector)

print()
print('Back substitute')
print()

# back substitute
# setup result array
result = [0] * LEN
# iterate through the rest backwards to find remaining results
for i in range(LEN-1, -1, -1):
    # calculate the result for each row using the matrix entries
    sums = vector[i]
    for j in range(i+1, LEN):
        sums = sums - matrix[i][j] * result[j]
    result[i] = sums / matrix[i][i]
    pprint(matrix, vector, result)

# print out results nicely
print()
print('Final Result:')
print()
print('Of the form [A | b]:')
for i, row in enumerate(matrix):
    row.append(vector[i])
    print(row)
    row.pop()
print()
print('x:')
print(result)
