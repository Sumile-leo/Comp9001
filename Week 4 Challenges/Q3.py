# 字符串反转程序
# 功能：读取多行输入，反转每一行并输出，直到EOF

def main():
    """主函数：持续读取输入并反转字符串"""
    while True:
        try:
            # 读取一行输入
            line = input()
            # 使用切片[::-1]反转字符串并输出
            print(line[::-1])
        except EOFError:
            # 遇到EOF时退出循环
            break

if __name__ == "__main__":
    main()
