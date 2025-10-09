# 日本武士刀重铸模拟器
# 功能：允许用户重铸不完美的武士刀蓝图以匹配大师铁匠的完美设计
# 武士刀使用'#'表示刀刃，'='和'|'表示刀柄

import os
import sys
"""
japan.py

日本武士刀重铸模拟程序

程序比较相似度分数，接受或拒绝武士刀，并反复提示用户重铸刀刃，
直到它满足所需的相似度阈值。

使用方法：
    python3 japan.py <imperfect_blueprint.bp> <min_similarity>
"""


def get_katana(katana: str):
    """
    读取武士刀蓝图文件
    参数：katana - 蓝图文件名
    返回：文件内容的行列表（已去除空白）
    """
    with open(katana, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # 去除每行的首尾空白
    lines = [line.strip() for line in lines]

    return lines

def print_katana(bp: str):
    """
    打印武士刀蓝图文件的内容
    参数：bp - 蓝图文件名（.bp文件）
    """
    with open(bp, "r", encoding="utf-8") as f:
        content = f.read()
        print(content, end='')
    pass


def get_similarity_score(imperfect_bp: str) -> float:
    """
    比较不完美武士刀的刀刃与perfect_katana.bp中的完美武士刀
    
    计算并返回0到1之间的相似度分数，其中1表示完美匹配。
    相似度基于仅刀刃部分每行的'#'符号数量。
    
    参数：imperfect_bp - 不完美武士刀蓝图的文件名
    返回：float - 两个蓝图之间的平均行相似度
    """
    # 读取不完美的武士刀
    lines = get_katana(imperfect_bp)

    # 读取完美的武士刀
    lines_perfect = get_katana("perfect_katana.bp")

    temp = []

    # 从第4行开始比较（前4行是刀柄）
    for i in range(4, min(len(lines), len(lines_perfect))):
        # 计算每行的相似度：短度/长度
        big = max(len(lines[i]), len(lines_perfect[i]))
        small = min(len(lines[i]), len(lines_perfect[i]))
        t = small / big
        temp.append(t)

    # 返回平均相似度
    total = sum(temp)

    return total / len(temp)

    pass


def reforge_imperfect_katana(imperfect_bp: str):
    """
    提示用户通过输入每行的'#'符号数量来重塑不完美武士刀的刀刃
    
    更新不完美的蓝图，保持刀柄不变，使其尽可能接近perfect_katana.bp中的完美武士刀。
    
    参数：imperfect_bp - 不完美武士刀蓝图的文件名
    """
    # 读取当前的武士刀
    lines = get_katana(imperfect_bp)

    # 创建副本用于修改
    temp = lines.copy()

    # 读取完美的武士刀作为参考
    lines_perfect = get_katana("perfect_katana.bp")

    # 计算刀刃行数和最大宽度
    blade = len(lines_perfect) - 4  # 减去刀柄的4行
    max_width = len(lines_perfect[3]) - 2  # 最宽行减去边界
    now_blade = 1  # 当前正在重铸的刀刃行

    print_bol = False

    print(">> REFORGING KATANA.")
    print()
    print(f"Katana Details:\n- Blade (lines): {blade}\n- Maximum width: {max_width}\n")
    
    while True:
        # 如果所有刀刃行都重铸完成
        if now_blade == blade + 1:
            # 为每行添加空格（除了第3行）
            temp = [" " + item if i != 3 else item for i, item in enumerate(temp)]
            print()
            print(">> FORGING COMPLETE.")
            # 询问是否打印武士刀
            if input("Would you like to print the katana [yes/no]? ") == "yes":
                print()
                print_bol = True
            if print_bol:
                # 写入文件
                with open(imperfect_bp, "w", encoding="utf-8") as f:
                    f.writelines(line + "\n" for line in temp)
                print_katana(imperfect_bp)
            break
        
        # 提示用户输入当前行的'#'数量，并显示完美武士刀的参考
        inp_blade = input(f"Line ({now_blade}/{blade}) [{lines_perfect[now_blade + 3]}]: ")
        
        # 验证输入
        try:
            inp_blade = int(inp_blade)
        except ValueError:
            print("Error: Input must be an integer.")
            continue
        
        # 检查输入范围
        if not 0 < inp_blade <= max_width:
            print(f"Error: Input must be between 1 to {max_width} (inclusive).")
            continue

        # 更新当前行
        temp[now_blade + 3] = "#" * inp_blade
        now_blade += 1

    pass


def main():
    """
    运行从头到尾的完整武士刀锻造模拟
    
    处理命令行参数，加载蓝图，检查相似度分数，
    并反复提示用户重铸武士刀，直到满足所需阈值。
    """
    # 检查命令行参数数量
    if len(sys.argv) < 3:
        print("Error: Missing arguments.")
        print(
            "Usage: python3 japan.py <imperfect_blueprint.bp> <min_similarity>")
        sys.exit(1)

    # 获取文件名和相似度阈值
    filename = sys.argv[1]
    similarity_str = sys.argv[2]

    # 验证文件扩展名
    if not filename.endswith(".bp"):
        print(
            "Error: Invalid file extension. Expected a filename ending in .bp")
        sys.exit(1)

    # 验证相似度是否为浮点数
    try:
        similarity = float(similarity_str)
    except ValueError:
        print("Error: Invalid similarity score. Expected a float value.")
        sys.exit(1)

    # 检查文件是否存在
    if not os.path.isfile(filename):
        print(f"Error: File not found. Please check that {filename} exists.")
        sys.exit(1)

    # 验证相似度范围
    if not (0 <= similarity <= 1):
        print("Error: Similarity score must be between 0 and 1 (inclusive).")
        sys.exit(1)

    print(">> READING IN BLUEPRINTS.")
    print()
    
    # 主循环：持续重铸直到满足相似度要求
    while True:
        print(">> ANALYSING THEIR SIMILARITY.")
        # 计算当前相似度
        score = get_similarity_score(filename)
        print(f"Similarity score: {score:.2f}")
        
        # 检查是否达到要求
        if float(similarity) > score:
            print("Denied: You must reforge it.")
        else:
            print("Accepted: The blacksmith is satisfied.")
            break
        print()
        # 重铸武士刀
        reforge_imperfect_katana(filename)
        print()

    pass


# 程序入口
if __name__ == '__main__':
    main()
