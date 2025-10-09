# 安全登录系统
# 功能：实现一个带有尝试次数限制的密码验证系统

import sys

print("Secure System Login Program")
print()
bol = False  # 用于标记是否登录成功

# 检查命令行参数数量是否正确（需要2个参数：尝试次数和密码）
if len(sys.argv) == 3:
    # 检查尝试次数是否为数字
    if sys.argv[1].isdigit():
        # 检查尝试次数是否大于0
        if int(sys.argv[1]) > 0:
            # 允许用户尝试指定次数
            for i in range(int(sys.argv[1])):
                # 提示用户输入密码
                pw = input(f"Enter password (attempt {i+1} of {sys.argv[1]}): ")
                # 检查密码是否正确
                if pw == sys.argv[2]:
                    bol = True
                    break
                else:
                    print("Incorrect password.")
            print()
            # 根据登录结果输出相应信息
            if bol:
                print("Password Accepted. Welcome!")
            else:
                print("Access denied. Goodbye.")
        else:
            print("Invalid arguments.")
    else:
        print("Invalid arguments.")
else:
    print("Invalid arguments.")
