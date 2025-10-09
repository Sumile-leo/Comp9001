# 自动售货机库存管理系统 (VMIM - Vending Machine Inventory Management)
# 功能：管理自动售货机的零食库存，支持添加、删除、查看操作

class machine:
    """自动售货机类"""
    
    def __init__(self):
        """初始化售货机，创建空的商品和数量列表"""
        self.data = []    # 存储零食名称
        self.count = []   # 存储对应的数量

    def welcome(self):
        """显示欢迎信息"""
        print("Welcome to the VMIM System!\n")

    def hp(self):
        """显示帮助信息，列出所有可用命令"""
        print("ADD <snack> <quantity>\nREMOVE <index>\nPRINT\nHELP\nEXIT")

    def add(self, snack, quantity):
        """
        添加零食到售货机
        参数：snack - 零食名称
              quantity - 数量
        """
        if snack in self.data:
            # 如果零食已存在，提示错误
            print("You already have this snack!")
        elif quantity <= 0:
            # 数量必须为正数
            print("Quantity must be positive!")
        else:
            # 添加零食和数量
            self.data.append(snack)
            self.count.append(quantity)
            print(f"Added: {snack} [{quantity}]")

    def remove(self, index):
        """
        根据索引删除零食
        参数：index - 零食在列表中的位置（从1开始）
        """
        if index > len(self.data) or index <= 0:
            # 索引无效
            print("Invalid index!")
        else:
            # 删除指定索引的零食
            name = self.data.pop(index - 1)
            self.count.pop(index - 1)
            print(f"Removed: {name}")

    def pr(self):
        """打印当前所有零食及其数量"""
        if len(self.data) == 0:
            print("Your vending machine is empty!")
        else:
            # 显示所有零食：索引、名称、数量
            for i in range(len(self.data)):
                print(f"{i + 1}: {self.data[i]} [{self.count[i]}]")

    def exit(self):
        """显示退出信息"""
        print("Exiting VMIM System.")


def main():
    """主函数：处理用户命令"""
    mc = machine()
    mc.welcome()
    
    while True:
        # 读取并解析命令
        command = input("Enter command: ")
        # 将数字字符串转换为整数，其他保持为字符串
        parsed = list(map(lambda x: int(x) if x.isdigit() else x, command.split()))
        temp = False  # 标记命令是否有效
        
        if len(parsed) == 1:
            # 单参数命令
            if parsed[0] == "HELP":
                mc.hp()
            elif parsed[0] == "PRINT":
                mc.pr()
            elif parsed[0] == "EXIT":
                mc.exit()
                break
            else:
                temp = True
        elif len(parsed) == 2:
            # 双参数命令：REMOVE <index>
            if parsed[0] == 'REMOVE' and isinstance(parsed[1], int):
                mc.remove(parsed[1])
            else:
                temp = True
        elif len(parsed) == 3:
            # 三参数命令：ADD <snack> <quantity>
            if (parsed[0] == 'ADD' and isinstance(parsed[1], str)):
                mc.add(parsed[1], parsed[2])
            else:
                temp = True
        else:
            temp = True
        
        # 如果命令无效，输出错误信息
        if temp:
            print("Invalid command!")
        print()


if __name__ == '__main__':
    main()
