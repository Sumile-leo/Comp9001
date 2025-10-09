# 未来月份计算程序
# 功能：根据当前月份和月数差，计算未来是哪个月份

import sys

def future_month(x, y):
    """
    计算从当前月份开始，经过y个月后是哪个月份
    参数：x - 当前月份（1-12）
          y - 经过的月份数
    """
    # 月份名称列表
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    # 获取当前月份名称（x-1是因为数组索引从0开始）
    current = months[x - 1]
    # 计算未来月份（使用取模运算处理跨年情况）
    future = months[(x - 1 + y) % 12]
    # 输出结果
    print(f"It's currently {current}, in {y} months it will be {future}.")

# 从命令行参数读取当前月份和月数差
current = int(sys.argv[1])
later = int(sys.argv[2])

# 调用函数计算并输出结果
future = future_month(current, later)
