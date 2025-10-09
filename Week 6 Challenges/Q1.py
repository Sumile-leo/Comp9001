# 帕斯卡三角形生成程序
# 功能：生成指定行数的帕斯卡三角形

import sys

pascal_list = []  # 存储帕斯卡三角形的全局列表

def pascal(count: int):
    """
    递归生成帕斯卡三角形
    参数：count - 还需要生成的行数
    """
    if count == 0:
        return
    
    temp1 = [1]  # 每行都以1开头
    
    if len(pascal_list) == 0:
        # 第一行：只有一个1
        pascal_list.append(temp1)
    elif len(pascal_list) == 1:
        # 第二行：[1, 1]
        pascal_list.append([1, 1])
    else:
        # 后续行：每个数字是上一行相邻两数之和
        for i in range(len(pascal_list[-1])):
            if i == len(pascal_list[-1]) - 1:
                break
            # 相邻两数相加
            temp1.append(pascal_list[-1][i] + pascal_list[-1][i + 1])
        temp1.append(1)  # 每行以1结尾
        pascal_list.append(temp1)
    
    # 递归生成下一行
    pascal(count - 1)


# 主程序：处理命令行参数
if len(sys.argv) == 1:
    print("Not enough arguments.")
elif len(sys.argv) > 2:
    print("Too many arguments.")
else:
    try:
        # 生成指定行数的帕斯卡三角形（+1是因为索引从0开始）
        count = int(sys.argv[1]) + 1
        pascal(count)
        # 打印每一行
        for i in pascal_list:
            print(" ".join(map(str, i)))
    except:
        print("Invalid argument.")
