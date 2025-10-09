# IPv6地址验证程序
# 功能：验证输入的字符串是否为有效的IPv6地址

import re


def ipv6_check(ipv6):
    """
    检查输入是否为有效的IPv6地址
    IPv6地址格式：8组，每组1-4个十六进制数字，用冒号分隔
    参数：ipv6 - 待验证的IPv6地址字符串
    返回：True表示有效，False表示无效
    """
    # 按冒号分割地址
    temp = ipv6.split(':')
    # IPv6必须有8组
    if len(temp) != 8:
        return False

    # 正则表达式：匹配1-4个十六进制数字（0-9, a-f, A-F）
    hex_pattern = re.compile(r"^[0-9a-fA-F]{1,4}$")

    # 检查每一组是否符合格式
    for part in temp:
        if not hex_pattern.match(part):
            return False
    return True

# 主程序
ip = input("Please enter an IP address: ")
if ipv6_check(ip):
    print("It is a valid IPv6 address.")
else:
    print("It is not a valid IPv6 address.")
