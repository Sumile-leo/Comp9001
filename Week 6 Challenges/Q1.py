import sys

pascal_list = []
def pascal(count: int):
    if count == 0:
        return
    temp1 = [1]
    if len(pascal_list) == 0:
        pascal_list.append(temp1)
    elif len(pascal_list) == 1:
        pascal_list.append([1,1])
    else:
        for i in range(len(pascal_list[-1])):
            if i == len(pascal_list[-1]) - 1:
                break
            temp1.append(pascal_list[-1][i] + pascal_list[-1][i + 1])
        temp1.append(1)
        pascal_list.append(temp1)
    pascal(count-1)


if len(sys.argv) == 1:
    print("Not enough arguments.")
elif len(sys.argv) > 2:
    print("Too many arguments.")
else:
    try:
        count = int(sys.argv[1]) + 1
        pascal(count)
        for i in pascal_list:
            print(" ".join(map(str, i)))
    except:
        print("Invalid argument.")