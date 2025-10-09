# 统计学计算程序
# 功能：计算数据集的均值、方差和标准差

import math
import sys


def mean(numbers):
    """
    计算均值
    参数：numbers - 数字列表
    返回：平均值
    """
    total = sum(numbers)
    return total / len(numbers)


def variance(numbers, mean):
    """
    计算方差
    方差 = Σ(xi - mean)² / n
    参数：numbers - 数字列表
          mean - 均值
    返回：方差
    """
    total = 0
    for i in numbers:
        temp = i - mean
        total += temp * temp
    return total / len(numbers)


def sd(variance):
    """
    计算标准差
    标准差 = √方差
    参数：variance - 方差
    返回：标准差
    """
    return math.sqrt(variance)


def main():
    """主函数：读取数据并计算统计量"""
    temp = []

    print("Enter data set:")
    # 从标准输入读取所有数据
    for line in sys.stdin:
        try:
            # 分割每行并转换为浮点数
            for i in line.strip().split():
                temp.append(float(i))
        except ValueError:
            # 忽略无效输入
            pass
    
    print()
    
    # 检查是否有数据
    if not temp:
        print("No data!")
        sys.exit()
    
    # 计算统计量
    m = mean(temp)
    v = variance(temp, m)
    s = sd(v)
    
    # 输出结果（保留4位小数）
    print(f"Mean = {m:.4f}")
    print(f"Variance = {v:.4f}")
    print(f"Standard deviation = {s:.4f}")


if __name__ == '__main__':
    main()
