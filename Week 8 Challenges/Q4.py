# 许可证密钥格式化程序
# 功能：将许可证密钥格式化为指定格式（每k个字符用'-'分隔）

import re


def license_key_formatter(license, k):
    """
    格式化许可证密钥（方法1：手动分组）
    参数：license - 原始许可证字符串
          k - 每组的字符数
    返回：格式化后的许可证密钥
    """
    # 移除所有连字符并转换为大写
    clean = license.replace("-", "").upper()

    groups = []
    # 从右向左每k个字符分为一组
    while clean:
        groups.insert(0, clean[-k:])  # 取最后k个字符
        clean = clean[:-k]            # 移除已处理的字符

    # 用连字符连接所有组
    return "-".join(groups)

def license_key_formatter2(license, k):
    """
    格式化许可证密钥（方法2：使用正则表达式）
    参数：license - 原始许可证字符串
          k - 每组的字符数
    返回：格式化后的许可证密钥
    """
    # 移除所有非字母数字字符并转换为大写
    s = re.sub(r'[^A-Za-z0-9]', '', license).upper()
    # 使用正则表达式按k个字符分组
    pattern = f"(?=(?:.{{{k}}})+$)"
    groups = re.split(pattern, s)

    return "-".join(groups)
