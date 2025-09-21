import re


def ipv6_check(ipv6):
    temp = ipv6.split(':')
    if len(temp) != 8:
        return False

    hex_pattern = re.compile(r"^[0-9a-fA-F]{1,4}$")

    for part in temp:
        if not hex_pattern.match(part):
            return False
    return True

ip = input("Please enter an IP address: ")
if ipv6_check(ip):
    print("It is a valid IPv6 address.")
else:
    print("It is not a valid IPv6 address.")