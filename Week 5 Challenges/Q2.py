# 黄金比例检测程序
# 功能：检查两个输入数字是否符合黄金比例关系

try:
    # 读取两个数字（用空格分隔）
    a, b = input("Enter two numbers: ").split()
    print()
    # 转换为浮点数
    a, b = float(a), float(b)
    
    # 检查黄金比例关系：(a+b)/a ≈ a/b 或 (a+b)/b ≈ b/a
    if (a + b) // a == a // b or (a + b) // b == b // a:
        print("Golden ratio!")
    else:
        print("Maybe next time.")
except ValueError:
    # 处理输入无效的情况
    print("Invalid input.")
