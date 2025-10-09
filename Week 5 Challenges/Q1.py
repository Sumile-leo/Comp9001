# Triforce（三角力量）图形绘制程序
# 功能：根据给定的高度绘制Triforce图案（塞尔达传说中的标志性图形）

def triforce(height):
    """
    绘制Triforce图案
    参数：height - 三角形的高度
    """
    # 计算矩阵尺寸
    rows = height * 2
    cols = height * 4
    # 创建填充空格的矩阵
    matrix = [[" " for _ in range(cols)] for _ in range(rows)]
    
    # 绘制外部大三角形的左右斜边
    for i in range(len(matrix)):
        matrix[i][i] = "/"                    # 左斜边
        matrix[i][cols - i - 1] = "\\"        # 右斜边

    # 绘制顶部三角形的底边（用下划线）
    for i in range(len(matrix[0])):
        if matrix[0][i] == " ":
            matrix[0][i] = "_"

    # 绘制中间的水平分割线
    for i in range(cols):
        if height + 1 <= i <= cols - height - 2:
            matrix[height][i] = "_"

    # 绘制底部两个小三角形的内侧斜边
    temp1 = height
    temp2 = height * 4 - height - 1
    for i in range(height - 1, -1, -1):
        matrix[i][temp1] = '\\'
        matrix[i][temp2] = '/'
        temp1 += 1
        temp2 -= 1

    print()
    
    # 移除每行末尾多余的空格
    for i in range(len(matrix) - 1, -1, -1):
        for j in range(len(matrix[i]) - 1, -1, -1):
            if matrix[i][j] == "\\":
                break
            else:
                matrix[i][j] = ''

    # 打印整个图形
    for i in range(len(matrix) - 1, -1, -1):
        for j in matrix[i]:
            print(j, end='')
        print()


# 主程序
height = input("Enter height: ")
print()

# 验证输入：必须是2-20之间的整数
if height.isdigit():
    temp = int(height)
    if 2 <= temp <= 20:
        triforce(temp)
    else:
        print("Invalid height.")
else:
    print("Invalid height.")
