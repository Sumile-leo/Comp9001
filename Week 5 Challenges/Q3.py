# 变位词（Anagram）检测程序
# 功能：判断两个字符串是否互为变位词（忽略标点符号、空格和大小写）

import string

def is_anagram(str1, str2):
    """
    判断两个字符串是否为变位词
    参数：str1, str2 - 待比较的两个字符串
    返回：True表示是变位词，False表示不是
    """
    # 创建转换器，移除所有标点符号和空格
    translator = str.maketrans('', '', string.punctuation + " ")
    # 清理字符串：移除标点和空格，转换为小写
    str1 = str1.translate(translator).lower()
    str2 = str2.translate(translator).lower()

    # 比较两个字符串排序后是否相同
    return sorted(str1) == sorted(str2)


# 主程序
s1 = input("Enter line: ")
s2 = input("Enter anagram: ")

# 判断并输出结果
if is_anagram(s1, s2):
    print("Anagram!")
else:
    print("Not an anagram.")
