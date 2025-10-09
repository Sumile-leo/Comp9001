# 奇偶数判断程序
# 功能：判断输入的数字是奇数还是偶数

# 提示用户输入一个数字
temp = int(input("Enter a number: "))

# 判断数字是否为偶数（能被2整除）
if temp % 2 == 0:
    print(f"The number {temp} is even.")
else:
    print(f"The number {temp} is odd.")
