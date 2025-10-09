# RNA剪接程序
# 功能：从RNA链中移除内含子序列（GUGU到AGAG之间的部分）

import re

def splice_rna(rna):
    """
    剪接RNA链，移除内含子
    内含子定义：从GUGU开始到AGAG结束的序列
    参数：rna - 原始RNA链
    返回：剪接后的RNA链
    """
    # 使用正则表达式移除GUGU到AGAG之间的所有序列（非贪婪匹配）
    return re.sub(r'GUGU.*?AGAG', '', rna)


# 主程序
strand = input("Input strand: ")
print()

# 检查是否输入为空
if strand == '':
    print("No strand provided.")
else:
    # 输出剪接后的结果
    print(f"Output is {splice_rna(strand)}")
