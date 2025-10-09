# 阿波罗11号发射倒计时程序
# 功能：模拟阿波罗11号火箭发射的倒计时过程

def apollo(count):
    """
    执行发射倒计时
    参数：count - 倒计时起始数字
    """
    print("Guidance is internal.")
    
    # 从count倒数到0
    for i in range(count, -1, -1):
        if i == 6:
            # 倒数到6时，点火序列开始
            print("Ignition sequence start.")
        if i == 0:
            # 倒数到0时，发射！
            print("All engine running.\nLift off on Apollo 11!")
            break
        # 输出当前倒计时数字
        print(f"{i}...")

# 从12开始倒计时
apollo(12)
