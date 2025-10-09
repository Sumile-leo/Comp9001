# 最长字符串查找程序
# 功能：从三个输入的字符串中找出最长的那个

print("Input 3 strings and find what string is the longest")

# 读取三个字符串
str1 = input()
str2 = input()
str3 = input()

# 检查三个字符串是否长度相同
if len(str1) == len(str2) and len(str1) == len(str3):
    # 如果都是空字符串
    if str1 == '':
        print("All strings are empty")
    else:
        print("All strings are the same length")
else:
    # 找出最长字符串的长度
    a = max(len(str1), len(str2), len(str3))
    # 判断哪个字符串最长并输出
    if a == len(str1):
        print(f'"{str1}" is the longest string')
    elif a == len(str2):
        print(f'"{str2}" is the longest string')
    elif a == len(str3):
        print(f'"{str3}" is the longest string')
