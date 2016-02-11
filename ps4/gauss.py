vector = [18, -3.0, 5.0]

matrix = [
    [-11.0, 3.0, 3.0],
    [-2.0, -5.0, 1.0],
    [1.0, -10.0, 8.0]
]

def pprint(m, v):
    for i, row in enumerate(m):
        row.append(vector[i])
        print(row)
        row.pop()

    print()

pprint(matrix, vector)
