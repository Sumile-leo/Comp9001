def tictactoe(side, x, y, draw):
    draw[y * 2][x * 2] = side
    for row in [0, 2, 4]:
        if draw[row][0] == draw[row][2] == draw[row][4] != " ":
            return draw[row][0]

    for col in [0, 2, 4]:
        if draw[0][col] == draw[2][col] == draw[4][col] != " ":
            return draw[0][col]

    if draw[0][0] == draw[2][2] == draw[4][4] != " ":
        return draw[0][0]
    if draw[0][4] == draw[2][2] == draw[4][0] != " ":
        return draw[0][4]

    for row in [0, 2, 4]:
        for col in [0, 2, 4]:
            if draw[row][col] == " ":
                return "Continue"

    return "Draw"



draw = [
    [" ","|"," ","|"," "],
    ["-"]*5,
    [" ","|"," ","|"," "],
    ["-"]*5,
    [" ","|"," ","|"," "]
]
first = True
while True:
    side = ''
    if first:
        side = "X"
        first = False
    else:
        side = "O"
        first = True
    x, y = input().split()
    x, y = int(x), int(y)
    temp = tictactoe(side, x, y, draw)
    if temp == 'Draw':
        print("Draw")
        print()
        for i in draw:
            for j in i:
                print(j, end="")
            print()
        print()
        break
    elif temp == 'Continue':
        print()
        for i in draw:
            for j in i:
                print(j, end="")
            print()
        print()
    else:
        print(f"{side} wins!")
        print()
        for i in draw:
            for j in i:
                print(j, end="")
            print()
        print()
        break