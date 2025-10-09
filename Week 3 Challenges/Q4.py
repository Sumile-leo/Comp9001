# 数字比较程序
# 功能：比较两个命令行参数的大小

import sys

# 从命令行参数读取两个数字
a = int(sys.argv[1])
b = int(sys.argv[2])

# 比较两个数字并输出结果（小写的true/false）
print(f"Is {a} > {b}? {str(a>b).lower()}")
