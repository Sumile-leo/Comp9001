# 家族树类 - Person类
# 功能：管理人物的家族关系和生存状态

class Person:
    """
    Person类用于表示一个人及其家族关系
    属性：
    - name: 人的名字
    - is_alive: 是否活着（布尔值）
    - children: 子女列表（Person对象列表）
    """
    
    def __init__(self, name: str):
        """
        初始化一个Person对象
        参数：name - 人的名字（字符串）
        """
        self.name = name
        self.is_alive = True  # 初始状态为活着
        self.children = []    # 初始没有子女
    
    def add_child(self, Person):
        """
        添加一个子女
        参数：Person - 要添加的子女（Person对象）
        """
        self.children.append(Person)
    
    def get_children_names(self):
        """
        获取所有直系子女的名字列表
        返回：包含所有子女名字的列表
        """
        temp = []
        for i in self.children:
            temp.append(i.name)
        return temp

    def dies(self):
        """
        标记该人死亡
        将is_alive设为False并输出死亡消息
        """
        self.is_alive = False
        print(f"{self.name} has died :(")
    
    def count_living_descendants(self):
        """
        递归计算所有活着的后代数量
        后代包括：子女、孙子女、曾孙子女等所有后代
        返回：活着的后代总数（整数）
        """
        total = 0
        # 遍历所有子女
        for child in self.children:
            # 如果子女还活着，计数加1
            if child.is_alive:
                total += 1
            # 递归计算该子女的后代数量（无论子女是否活着）
            total += child.count_living_descendants()
        return total
