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
for row in range(0, len(vector)-1):
    for i in range(row+1, len(vector)):
        factor = matrix[i][row] / matrix[row][row]
        for j in range(row, len(vector)):
            matrix[i][j] = matrix[i][j] - factor * matrix[row][j]

        vector[i] = vector[i] - factor * vector[row]

    pprint(matrix, vector)

pprint(matrix, vector)
