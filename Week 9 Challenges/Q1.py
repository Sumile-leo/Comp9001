def read_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix

def matrix_multiply(A, B):
    if len(A) == len(B) == 0:
        return 0
    elif len(A[0]) != len(B):
        return None

    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result

try:
    c1, r1, c2, r2 = map(int, input().split())
    A = read_matrix(r1, c1)
    B = read_matrix(r2, c2)
    result = matrix_multiply(A, B)
    if result is None:
        print("Invalid input.")
    elif result == 0:
        print(result)
    else:
        for i in result:
            print(" ".join(map(str, i)))
except:
    print("Invalid input.")
