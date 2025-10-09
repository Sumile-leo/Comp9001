# 澳大利亚动物迁移模拟器
# 功能：模拟澳大利亚动物跨州迁移，确保每个动物都远离其威胁

import csv
'''
australia.py

澳大利亚动物迁移模拟程序

模拟澳大利亚动物跨州迁移。每个动物都有一个已知的威胁需要避免。
目标是在确保没有动物靠近其威胁的情况下，迁移尽可能多的动物——
并且没有两个动物共享同一个州。

该程序涉及从文件读取动物数据，构建对象表示每个动物，
并实施迁移逻辑以确保动物被安全放置。
'''

# 澳大利亚各州的相邻关系
ADJACENT_STATES = {
    "NSW": ["VIC", "SA", "QLD"],     # 新南威尔士州
    "QLD": ["NT", "SA", "NSW"],      # 昆士兰州
    "VIC": ["SA", "NSW"],            # 维多利亚州
    "TAS": [],                       # 塔斯马尼亚州（岛屿，无相邻州）
    "SA": ["WA", "NT", "QLD", "NSW", "VIC"],  # 南澳大利亚州
    "NT": ["WA", "SA", "QLD"],       # 北领地
    "WA": ["SA", "NT"]               # 西澳大利亚州
}


class FictionalAnimal:
    '''
    代表迁移模拟中使用的虚构澳大利亚动物
    
    每个动物都有名字、栖息地、威胁和当前州。
    '''

    def __init__(self, name: str, habitat: str, threat: str, state="ACT"):
        '''
        初始化一个新的FictionalAnimal对象
        
        参数：
            name (str): 动物的名字
            habitat (str): 动物偏好的栖息地
            threat (str): 构成威胁的另一种动物的名字
            state (str): 起始州，默认为'ACT'（首都领地）
        '''
        self.name = name
        self.habitat = habitat
        self.threat = threat
        self.state = state
        pass

    def get_state(self) -> str:
        '''
        返回该动物当前所在的州
        返回：str - 当前州
        '''
        return self.state
        pass

    def set_state(self, state: str):
        '''
        如果新州有效，则更新动物的州
        
        有效州是指在已定义州列表中存在的州。
        如果州无效，位置不会改变。
        
        参数：
            state (str): 要分配给动物的新州
        '''
        if state not in ADJACENT_STATES.keys():
            return None
        else:
            self.state = state
        pass

    def __str__(self) -> str:
        '''
        返回表示动物详细信息的格式化字符串
        格式：
        <name>
           Habitat : <habitat>
           Threat  : <threat>
           State   : <state>
        '''
        return f"{self.name}\n   Habitat : {self.habitat}\n   Threat  : {self.threat}\n   State   : {self.state}"
        pass

    def load_dataset() -> list['FictionalAnimal']:
        '''
        从animals.csv加载动物数据并返回FictionalAnimal对象列表
        
        行必须遵循格式：<name>,<habitat>,<threat>
        
        缺少或多余字段的行将被跳过。
        如果文件不存在，返回空列表。
        
        返回：
            list[FictionalAnimal]: 有效动物对象列表
        '''
        list_fictional_animals = []
        try:
            with open("animals.csv", "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                # 逐行读取
                for row in reader:
                    # 检查行是否有3个字段
                    if len(row) != 3:
                        continue
                    # 创建FictionalAnimal对象
                    fa = FictionalAnimal(row[0], row[1], row[2])
                    list_fictional_animals.append(fa)
            return list_fictional_animals
        except FileNotFoundError:
            # 文件不存在，返回空列表
            return list_fictional_animals
        pass


def relocate_animals(animals: list[FictionalAnimal]):
    '''
    模拟澳大利亚动物的迁移
    
    没有两个动物可以共享同一个州，并且没有动物可以靠近其威胁。
    
    迁移遵循以下固定的州顺序：
    NSW → QLD → VIC → TAS → SA → NT → WA
    
    动物按照它们在列表中出现的顺序逐个考虑迁移。
    如果动物无法被放置在某个州，其州保持为'ACT'。
    
    参数：
        animals (list[FictionalAnimal]): FictionalAnimal对象列表
    
    返回：
        tuple: (成功迁移的动物数量, 迁移摘要列表)
    '''
    # 创建字典跟踪每个州的占用情况
    # 值格式："动物名字|威胁名字"
    temp = {
        "NSW": None,
        "QLD": None,
        "VIC": None,
        "TAS": None,
        "SA": None,
        "NT": None,
        "WA": None
    }
    count = 0  # 成功迁移的动物计数
    temp_locate = ["NSW", "QLD", "VIC", "TAS", "SA", "NT", "WA"]  # 迁移顺序
    temp_summary = []  # 迁移摘要
    
    # 遍历每个动物
    for i in animals:
        b = True  # 标记是否找到合适的州
        # 尝试将动物放置在每个州
        for j in temp_locate:
            bol = True  # 标记当前州是否安全
            # 如果当前州为空
            if temp[j] is None:
                # 检查所有相邻州
                for k in ADJACENT_STATES[j]:
                    if temp[k] is not None:
                        # 解析相邻州的动物信息
                        sp = temp[k].split("|")
                        # 检查冲突：当前动物是相邻动物的威胁 或 相邻动物是当前动物的威胁
                        if i.name == sp[1] or i.threat == sp[0]:
                            bol = False
                            break
                # 如果当前州安全
                if bol:
                    i.set_state(j)
                    temp[j] = i.name + "|" + i.threat
                    temp_summary.append(f"{i.name}: {i.state}")
                    count += 1
                    b = False
                    break
        # 如果没有找到合适的州，动物保持在ACT
        if b:
            temp_summary.append(f"{i.name}: {i.state}")
    
    return count, temp_summary


def main():
    '''
    运行从头到尾的完整迁移模拟
    
    该函数应该：
    - 从animals.csv加载虚构动物数据
    - 打印每个动物迁移前的详细信息
    - 使用relocate_animals()迁移动物
    - 打印每个动物迁移后的更新详细信息
    '''
    print(">> READING IN ANIMALS.")
    # 加载动物数据
    fa = FictionalAnimal.load_dataset()
    print(f"Loaded {len(fa)} animals from animals.csv.")
    print()
    
    # 显示迁移前的动物信息
    print(">> BEFORE RELOCATION.")
    for i in fa:
        print(i.__str__())
        print()
    
    # 执行迁移
    count, summary = relocate_animals(fa)
    
    # 显示迁移结果
    print(">> RELOCATING ANIMALS.")
    print(f"Animals relocated: {count}/{len(fa)}")
    print()
    
    # 显示摘要
    print(">> SUMMARY.")
    for i in summary:
        print(i)
    pass


# 程序入口
if __name__ == '__main__':
    main()
