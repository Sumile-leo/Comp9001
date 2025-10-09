# 重复单词计数程序
# 功能：统计命令行参数中重复出现的单词数量

import sys

def main():
    """主函数：计算重复单词的数量"""
    # 获取所有命令行参数（排除程序名）
    words = sys.argv[1:]
    # 如果没有参数，输出0
    if not words:
        print(0)
        return

    # 使用字典记录每个单词的出现次数
    count = {}

    # 重复次数计数器
    repetitions = 0

    # 遍历所有单词
    for w in words:
        # 获取该单词之前出现的次数
        prev = count.get(w, 0)
        # 如果之前已经出现过，增加重复计数
        if prev >= 1:
            repetitions += 1
        # 更新单词出现次数
        count[w] = prev + 1

    # 输出重复单词的总数
    print(repetitions)

if __name__ == "__main__":
    main()
