
try:
    a, b = input("Enter two numbers: ").split()
    print()
    a, b = float(a), float(b)
    if (a+b)//a == a//b or (a+b)//b == b//a:
        print("Golden ratio!")
    else:
        print("Maybe next time.")
except ValueError:
    print("Invalid input.")