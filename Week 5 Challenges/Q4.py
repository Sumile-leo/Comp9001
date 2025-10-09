# 井字棋（Tic-Tac-Toe）游戏
# 功能：实现完整的井字棋游戏逻辑，支持双人对战

def tictactoe(side, x, y, draw):
    """
    处理一步棋并检查游戏状态
    参数：side - 当前玩家标记（'X'或'O'）
          x, y - 下棋位置的坐标
          draw - 游戏棋盘（二维列表）
    返回：游戏状态 - 'X'/'O'（某方获胜）, 'Draw'（平局）, 'Continue'（继续游戏）
    """
    # 在指定位置放置棋子
    draw[y * 2][x * 2] = side
    
    # 检查所有横排是否有获胜者
    for row in [0, 2, 4]:
        if draw[row][0] == draw[row][2] == draw[row][4] != " ":
            return draw[row][0]

    # 检查所有竖列是否有获胜者
    for col in [0, 2, 4]:
        if draw[0][col] == draw[2][col] == draw[4][col] != " ":
            return draw[0][col]

    # 检查主对角线（左上到右下）
    if draw[0][0] == draw[2][2] == draw[4][4] != " ":
        return draw[0][0]
    # 检查副对角线（右上到左下）
    if draw[0][4] == draw[2][2] == draw[4][0] != " ":
        return draw[0][4]

    # 检查是否还有空位
    for row in [0, 2, 4]:
        for col in [0, 2, 4]:
            if draw[row][col] == " ":
                return "Continue"  # 还有空位，继续游戏

    # 没有空位且没有获胜者，平局
    return "Draw"


# 初始化游戏棋盘
draw = [
    [" ", "|", " ", "|", " "],
    ["-"] * 5,
    [" ", "|", " ", "|", " "],
    ["-"] * 5,
    [" ", "|", " ", "|", " "]
]

first = True  # 标记当前是否是X的回合

# 游戏主循环
while True:
    # 确定当前玩家
    side = ''
    if first:
        side = "X"
        first = False
    else:
        side = "O"
        first = True
    
    # 读取玩家输入的坐标
    x, y = input().split()
    x, y = int(x), int(y)
    
    # 执行一步棋并获取游戏状态
    temp = tictactoe(side, x, y, draw)
    
    # 根据游戏状态处理
    if temp == 'Draw':
        # 平局
        print("Draw")
        print()
        for i in draw:
            for j in i:
                print(j, end="")
            print()
        print()
        break
    elif temp == 'Continue':
        # 继续游戏，显示当前棋盘
        print()
        for i in draw:
            for j in i:
                print(j, end="")
            print()
        print()
    else:
        # 有玩家获胜
        print(f"{side} wins!")
        print()
        for i in draw:
            for j in i:
                print(j, end="")
            print()
        print()
        break
