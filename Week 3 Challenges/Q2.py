print("Input 3 strings and find what string is the longest")
str1 = input()
str2 = input()
str3 = input()

if len(str1) == len(str2) and len(str1) == len(str3):
    if str1 == '':
        print("All strings are empty")
    else:
        print("All strings are the same length")
else:
    a = max(len(str1), len(str2), len(str3))
    if a == len(str1):
        print(f'"{str1}" is the longest string')
    elif a == len(str2):
        print(f'"{str2}" is the longest string')
    elif a == len(str3):
        print(f'"{str3}" is the longest string')
