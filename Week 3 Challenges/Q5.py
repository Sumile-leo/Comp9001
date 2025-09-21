a = "Fizz"
b = "Buzz"
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print(a+b)
    elif i % 3 == 0:
        print(a)
    elif i % 5 == 0:
        print(b)
    else:
        print(i)