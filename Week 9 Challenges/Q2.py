# Pig Latin 翻译器
# 功能：读取标准输入的每一行，将其转换为 Pig Latin 语言并输出
import sys

def pig_latin_word(word):
    """
    将单个单词转换为 Pig Latin
    规则：
    1. 以辅音开头：将开头的辅音移到末尾并加"ay" (如: dog -> ogday)
    2. 以元音开头：
       - 如果不以'w'结尾，加"way" (如: easy -> easyway)
       - 如果以'w'结尾，加"ay" (如: yellow -> yelloway)
    注意：y被视为元音
    """
    # 如果单词为空，直接返回
    if not word:
        return word
    
    # 定义元音字母（包括y）
    vowels = 'aeiuoy'
    
    # 检查单词首字母是否为元音
    if word[0] in vowels:
        # 以元音开头的处理
        if not word.endswith('w'):
            return word + 'way'  # 不以w结尾，加"way"
        else:
            return word + 'ay'   # 以w结尾，只加"ay"
    
    else:
        # 以辅音开头的处理
        # 找到第一个元音的位置
        first_vowel_index = 0
        for i, char in enumerate(word):
            if char in vowels:
                first_vowel_index = i
                break
        
        # 将开头的辅音移到末尾并加"ay"
        return word[first_vowel_index:] + word[:first_vowel_index] + 'ay'

def pig_latin_line(line):
    """
    将一整行文本转换为 Pig Latin
    参数：line - 输入的一行文本
    返回：转换后的文本
    """
    # 如果是空行，返回空字符串
    if not line.strip():
        return ''
    
    # 按空格分割单词
    words = line.split()
    # 转换每个单词
    translated_words = [pig_latin_word(word) for word in words]
    # 用空格连接所有单词
    return ' '.join(translated_words)

# 主程序：读取标准输入直到EOF
for line in sys.stdin:
    # 移除行尾的换行符
    line = line.rstrip('\n')
    # 翻译并输出结果
    print(pig_latin_line(line))
