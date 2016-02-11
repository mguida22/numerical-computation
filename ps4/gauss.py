vector = [18, -3.0, 5.0]

matrix = [
    [-11.0, 3.0, 3.0],
    [-2.0, -5.0, 1.0],
    [1.0, -10.0, 8.0]
]

def pprint(m, v):
    for i, row in enumerate(m):
        row.append(v[i])
        print(row)
        row.pop()

    print()

pprint(matrix, vector)

# Check if zeros on diagonal b/c that'll mean we need to divide by zero
for i, row in enumerate(matrix):
    if (row[i] == 0):
        raise ZeroDivisionError('Zero along the diagonal.')

# forward eliminate
# current row, used for diagonal element
for i in range(0, len(vector)-1):
    # current element(s) below diagonal
    for j in range(i+1, len(vector)):
        # what we need to make [j,i] go to zero
        fraction = matrix[j][i] / matrix[i][i]

        # apply fraction to the row below the diagonal element
        for k in range(i, len(vector)):
            matrix[j][k] = matrix[j][k] - fraction * matrix[i][k]

        # apply fraction to the element in the same row of the vector
        vector[j] = vector[j] - fraction * vector[i]
        pprint(matrix, vector)
