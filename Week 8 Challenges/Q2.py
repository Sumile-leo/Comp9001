# DNA互补链生成程序
# 功能：根据DNA链生成其互补链

def dna(strand):
    """
    生成DNA互补链
    DNA碱基配对规则：A-T, T-A, G-C, C-G
    参数：strand - 原始DNA链
    返回：互补DNA链
    """
    # 定义碱基配对映射（支持大小写）
    mapping = {'A': 'T',
               'T': 'A',
               'G': 'C',
               'C': 'G',
               'a': 't',
               't': 'a',
               'g': 'c',
               'c': 'g'}
    # 将每个碱基转换为其互补碱基，无效字符转换为'x'
    return ''.join(mapping.get(b, 'x') for b in strand)

# 主程序
strand = input("Enter strand: ")
print()

# 检查是否输入为空
if strand == '':
    print("No strand provided.")
else:
    # 生成并输出互补链
    complementary = dna(strand)
    print(f"Complementary strand is {dna(strand)}")
