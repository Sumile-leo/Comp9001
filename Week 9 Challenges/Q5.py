import sys


def is_valid_key(key):
    """
    检查密钥是否有效
    密钥必须至少有1个字符，且只包含字母字符
    """
    return len(key) > 0 and key.isalpha()


def get_key():
    """
    获取有效的密钥
    如果密钥无效，会持续提示用户输入
    """
    while True:
        key = input("Enter the key: ")
        if is_valid_key(key):
            return key.lower()
        else:
            print("Error: Keys must be at least 1 character, and consist only of alphabetic characters.")
            print()


def char_to_num(char):
    """
    将字母字符转换为数字 (a/A=0, b/B=1, ..., z/Z=25)
    """
    return ord(char.lower()) - ord('a')


def num_to_char(num, is_upper):
    """
    将数字转换回字母字符
    保持原始的大小写
    """
    char = chr(num % 26 + ord('a'))
    return char.upper() if is_upper else char


def encrypt_char(plain_char, key_char):
    """
    使用Vigenère密码加密单个字符
    """
    if not plain_char.isalpha():
        return plain_char
    
    is_upper = plain_char.isupper()
    p = char_to_num(plain_char)
    k = char_to_num(key_char)
    c = (p + k) % 26
    
    return num_to_char(c, is_upper)


def decrypt_char(cipher_char, key_char):
    """
    使用Vigenère密码解密单个字符
    """
    if not cipher_char.isalpha():
        return cipher_char
    
    is_upper = cipher_char.isupper()
    c = char_to_num(cipher_char)
    k = char_to_num(key_char)
    p = (c - k) % 26
    
    return num_to_char(p, is_upper)


def process_text(text, key, encrypt=True):
    """
    加密或解密文本
    """
    result = []
    key_index = 0
    
    for char in text:
        if char.isalpha():
            key_char = key[key_index % len(key)]
            if encrypt:
                result.append(encrypt_char(char, key_char))
            else:
                result.append(decrypt_char(char, key_char))
            key_index += 1
        else:
            result.append(char)
    
    return ''.join(result)


def group_text(text, group_size):
    """
    将文本分组
    移除所有非字母字符，转换为大写，并按指定大小分组
    """
    # 只保留字母字符并转换为大写
    alpha_only = ''.join(char.upper() for char in text if char.isalpha())
    
    # 如果分组大小为0或大于文本长度，返回不带空格的文本
    if group_size == 0 or group_size >= len(alpha_only):
        return alpha_only
    
    # 按指定大小分组
    groups = []
    for i in range(0, len(alpha_only), group_size):
        groups.append(alpha_only[i:i + group_size])
    
    return ' '.join(groups)


def parse_arguments():
    """
    解析命令行参数
    返回: (mode, group_size) 其中 mode 是 'encrypt', 'decrypt' 或 None
    """
    args = sys.argv[1:]
    mode = None
    group_size = None
    
    # 第一遍：检查程序模式错误（优先级最高）
    has_encrypt = False
    has_decrypt = False
    
    for arg in args:
        if arg == '-e':
            has_encrypt = True
        elif arg == '-d':
            has_decrypt = True
    
    if has_encrypt and has_decrypt:
        print("Error: Cannot have both encrypt and decrypt mode.")
        sys.exit(1)
    
    # 第二遍：检查是否指定了程序模式
    if not has_encrypt and not has_decrypt:
        print("Error: Program mode was not specified. Use -e for encrypt and -d for decrypt.")
        sys.exit(1)
    
    # 第三遍：检查分组错误（优先级第三）
    i = 0
    while i < len(args):
        arg = args[i]
        
        if arg == '-g':
            # 检查是否有下一个参数
            if i + 1 >= len(args):
                print("Error: You must supply an integer of at least zero with the grouping flag.")
                sys.exit(1)
            
            try:
                group_size = int(args[i + 1])
                if group_size < 0:
                    print("Error: You must supply an integer of at least zero with the grouping flag.")
                    sys.exit(1)
            except ValueError:
                print("Error: You must supply an integer of at least zero with the grouping flag.")
                sys.exit(1)
            
            i += 2
        else:
            i += 1
    
    # 第四遍：解析模式
    for arg in args:
        if arg == '-e':
            mode = 'encrypt'
            break
        elif arg == '-d':
            mode = 'decrypt'
            break
    
    return mode, group_size


def main():
    # 解析命令行参数
    mode, group_size = parse_arguments()
    
    # 获取密钥
    key = get_key()
    
    # 获取输入文本
    if mode == 'encrypt':
        text = input("Enter the plaintext: ")
        result = process_text(text, key, encrypt=True)
        
        # 如果需要分组
        if group_size is not None:
            result = group_text(result, group_size)
        
        print(f"\nCiphertext is: {result}")
    else:  # decrypt
        text = input("Enter the ciphertext: ")
        result = process_text(text, key, encrypt=False)
        
        # 如果需要分组
        if group_size is not None:
            result = group_text(result, group_size)
        
        print(f"\nPlaintext is: {result}")


if __name__ == '__main__':
    main()

