# 矩阵乘法程序
# 功能：读取两个矩阵并执行矩阵乘法运算

def read_matrix(rows, cols):
    """
    读取矩阵数据
    参数：rows - 矩阵行数
          cols - 矩阵列数
    返回：二维列表表示的矩阵
    """
    matrix = []
    for i in range(rows):
        # 读取一行并转换为整数列表
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix

def matrix_multiply(A, B):
    """
    执行矩阵乘法：A × B
    参数：A - 第一个矩阵
          B - 第二个矩阵
    返回：乘积矩阵，如果无法相乘则返回None，如果两个矩阵都为空则返回0
    """
    # 如果两个矩阵都为空，返回0
    if len(A) == len(B) == 0:
        return 0
    # 检查矩阵乘法的条件：A的列数必须等于B的行数
    elif len(A[0]) != len(B):
        return None

    # 创建结果矩阵，初始化为0
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    # 矩阵乘法：result[i][j] = sum(A[i][k] * B[k][j])
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result

# 主程序
try:
    # 读取矩阵维度：c1(A的列数) r1(A的行数) c2(B的列数) r2(B的行数)
    c1, r1, c2, r2 = map(int, input().split())
    # 读取矩阵A和B
    A = read_matrix(r1, c1)
    B = read_matrix(r2, c2)
    # 执行矩阵乘法
    result = matrix_multiply(A, B)
    # 输出结果
    if result is None:
        print("Invalid input.")
    elif result == 0:
        print(result)
    else:
        # 打印结果矩阵
        for i in result:
            print(" ".join(map(str, i)))
except:
    # 捕获任何异常并输出错误信息
    print("Invalid input.")
