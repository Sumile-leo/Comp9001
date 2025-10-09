# 曼哈顿移动游戏
# 功能：显示角色在棋盘上可以移动到的所有位置及剩余移动步数
import sys

def validate_input(args):
    """
    验证命令行参数的有效性
    参数：args - 命令行参数列表 [程序名, width, height, x, y, walk_limit]
    返回：验证成功返回(width, height, x, y, walk_limit)元组，失败返回None
    """
    # 检查参数数量（包括程序名在内应该有6个）
    if len(args) != 6: 
        print("Invalid Number Of Arguments")
        return None
    
    # 尝试将所有参数转换为整数
    try:
        width = int(args[1])       # 棋盘宽度
        height = int(args[2])      # 棋盘高度
        x = int(args[3])           # 角色x坐标
        y = int(args[4])           # 角色y坐标
        walk_limit = int(args[5])  # 移动步数限制
    except ValueError:
        # 如果转换失败，判断是哪个参数有问题
        try:
            int(args[1])
        except ValueError:
            print("Invalid Width")
            return None
        
        try:
            int(args[2])
        except ValueError:
            print("Invalid Height")
            return None
        # 如果width和height都有效，那么是角色属性有问题
        print("Invalid Character Properties")
        return None
    
    # 验证width必须大于0
    if width <= 0:
        print("Invalid Width")
        return None
    
    # 验证height必须大于0
    if height <= 0:
        print("Invalid Height")
        return None
    
    # 验证角色属性：x和y必须在棋盘范围内，walk_limit必须非负
    if x < 0 or x >= width or y < 0 or y >= height or walk_limit < 0:
        print("Invalid Character Properties")
        return None
    
    return width, height, x, y, walk_limit

def manhattan_distance(x1, y1, x2, y2):
    """
    计算两点之间的曼哈顿距离
    曼哈顿距离 = |x1-x2| + |y1-y2|
    参数：(x1, y1) - 第一个点的坐标
          (x2, y2) - 第二个点的坐标
    返回：曼哈顿距离（整数）
    """
    return abs(x1 - x2) + abs(y1 - y2)

def create_board(width, height, x, y, walk_limit):
    """
    创建游戏棋盘
    参数：width - 棋盘宽度
          height - 棋盘高度
          x, y - 角色起始位置
          walk_limit - 最大移动步数
    返回：二维列表表示的棋盘
    """
    board = []
    # 遍历棋盘的每一行
    for row in range(height):
        board_row = []
        # 遍历该行的每一列
        for col in range(width):
            # 计算该格子到角色位置的曼哈顿距离
            distance = manhattan_distance(col, row, x, y)
            # 如果距离在移动限制内
            if distance <= walk_limit:
                # 计算从该格子还能移动多少步
                remaining = walk_limit - distance
                board_row.append(str(remaining))
            else:
                # 无法到达的格子显示为空格
                board_row.append(' ')
        board.append(board_row)
    
    # 将角色起始位置标记为'C'
    board[y][x] = 'C'
    
    return board

def print_board(board, width):
    """
    打印棋盘及边框
    参数：board - 二维列表表示的棋盘
          width - 棋盘宽度
    """
    # 打印顶部边框
    print('+' + '-' * (width * 2 - 1) + '+')
    
    # 打印每一行的内容
    for row in board:
        print('|' + '|'.join(row) + '|')
    
    # 打印底部边框
    print('+' + '-' * (width * 2 - 1) + '+')

def main():
    """
    主函数：处理输入、创建棋盘并显示
    """
    # 验证输入参数
    result = validate_input(sys.argv)
    
    # 如果验证失败，直接返回
    if result is None:
        return
    
    # 解包参数
    width, height, x, y, walk_limit = result
    
    # 创建棋盘
    board = create_board(width, height, x, y, walk_limit)
    # 打印棋盘
    print_board(board, width)

# 程序入口
if __name__ == "__main__":
    main()
