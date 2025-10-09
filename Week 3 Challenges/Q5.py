# FizzBuzz程序
# 功能：打印1-100的数字，但有特殊规则：
#       - 3的倍数输出"Fizz"
#       - 5的倍数输出"Buzz"
#       - 既是3又是5的倍数输出"FizzBuzz"

a = "Fizz"
b = "Buzz"

# 遍历1到100
for i in range(1, 101):
    # 检查是否同时是3和5的倍数
    if i % 3 == 0 and i % 5 == 0:
        print(a + b)
    # 检查是否是3的倍数
    elif i % 3 == 0:
        print(a)
    # 检查是否是5的倍数
    elif i % 5 == 0:
        print(b)
    # 其他情况输出数字本身
    else:
        print(i)
