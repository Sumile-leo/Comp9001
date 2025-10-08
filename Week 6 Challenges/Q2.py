import sys

def box(x, y):
    temp = "*" * x
    if y == 0:
        print("")
    elif y == 1:
        print(temp)
    else:
        for i in range(y):
            print(temp)



if len(sys.argv) == 1:
    print("No arguments")
elif len(sys.argv) == 2:
    print("Too few arguments")
elif len(sys.argv) > 3:
    print("Too many arguments")
else:
    try:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        if x < 0:
            if y < 0:
                print("Negative dimensions")
            else:
                print("Negative width")
        elif y < 0:
            print("Negative height")
        else:
            box(x, y)
    except:
        pass