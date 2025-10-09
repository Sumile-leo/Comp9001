# 凯撒密码加密程序
# 功能：使用凯撒密码对文本进行加密

def caesar_cipher(text, key):
    """
    使用凯撒密码加密文本
    原理：将每个字母按字母表顺序移动key位
    参数：text - 待加密的文本
          key - 移位数量（0-26）
    返回：加密后的文本
    """
    result = ""

    for ch in text:
        if ch.isupper():
            # 处理大写字母：A-Z的ASCII码是65-90
            result += chr((ord(ch) - 65 + key) % 26 + 65)
        elif ch.islower():
            # 处理小写字母：a-z的ASCII码是97-122
            result += chr((ord(ch) - 97 + key) % 26 + 97)
        else:
            # 非字母字符保持不变
            result += ch

    return result

# 主程序
key = int(input("Enter key: "))

# 验证密钥范围
if key < 0 or key > 26:
    print()
    print("Invalid key!")
else:
    # 读取待加密文本
    text = input("Enter line: ")
    print()
    # 输出加密结果
    print(caesar_cipher(text, key))
