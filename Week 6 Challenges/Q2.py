# 星号矩形绘制程序
# 功能：根据给定的宽度和高度绘制由星号组成的矩形

import sys

def box(x, y):
    """
    绘制星号矩形
    参数：x - 宽度（每行星号的数量）
          y - 高度（行数）
    """
    temp = "*" * x  # 生成一行星号
    
    if y == 0:
        # 高度为0，输出空行
        print("")
    elif y == 1:
        # 高度为1，输出一行
        print(temp)
    else:
        # 高度大于1，输出多行
        for i in range(y):
            print(temp)


# 主程序：处理命令行参数
if len(sys.argv) == 1:
    print("No arguments")
elif len(sys.argv) == 2:
    print("Too few arguments")
elif len(sys.argv) > 3:
    print("Too many arguments")
else:
    try:
        x = int(sys.argv[1])  # 宽度
        y = int(sys.argv[2])  # 高度
        
        # 检查是否有负数
        if x < 0:
            if y < 0:
                print("Negative dimensions")
            else:
                print("Negative width")
        elif y < 0:
            print("Negative height")
        else:
            # 绘制矩形
            box(x, y)
    except:
        pass
