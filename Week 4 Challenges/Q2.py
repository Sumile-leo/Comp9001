# 数字统计程序
# 功能：统计输入字符串中每个数字（0-9）出现的次数

# 读取输入
temp = input()
# 创建计数器数组，索引0-9对应数字0-9
count = [0] * 10

# 统计每个数字的出现次数
for i in temp:
    count[int(i)] += 1

# 输出每个数字的统计结果
for i in range(10):
    print(f"{i}: {count[i]}")
