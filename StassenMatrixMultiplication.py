def smm(a, b):
    n = len(a)
    if n == 1:
        return [[a[0][0] * b[0][0]]]

    mid = n // 2

    a11, a12, a21, a22 = [row[:mid] for row in a[:mid]], [row[mid:] for row in a[:mid]], [row[:mid] for row in a[mid:]], [row[mid:] for row in a[mid:]]
    b11, b12, b21, b22 = [row[:mid] for row in b[:mid]], [row[mid:] for row in b[:mid]], [row[:mid] for row in b[mid:]], [row[mid:] for row in b[mid:]]

    p1 = smm(a11, sub(b12, b22))
    p2 = smm(add(a11, a12), b22)
    p3 = smm(add(a21, a22), b11)
    p4 = smm(a22, sub(b21, b11))
    p5 = smm(add(a11, a22), add(b11, b22))
    p6 = smm(sub(a12, a22), add(b21, b22))
    p7 = smm(sub(a11, a21), add(b11, b12))

    c11 = add(sub(add(p5, p4), p2), p6)
    c12 = add(p1, p2)
    c21 = add(p3, p4)
    c22 = sub(sub(add(p5, p1), p3), p7)

    return [[c11[i][j] for j in range(mid)] + [c12[i][j] for j in range(mid)] for i in range(mid)] + \
           [[c21[i][j] for j in range(mid)] + [c22[i][j] for j in range(mid)] for i in range(mid)]


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def sub(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

matrix_a = [[1, 2], [3, 4]]
matrix_b = [[5, 6], [7, 8]]
result_matrix = smm(matrix_a, matrix_b)
print("Result Matrix:")
for row in result_matrix:
    print(row)
