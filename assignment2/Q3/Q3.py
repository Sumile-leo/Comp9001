# 约旦铁路建设模拟器
# 功能：确定最便宜的建设九个火车站的顺序，使总建设成本不超过给定预算

# jordan.py

"""
约旦铁路编年史模拟器

在这个作业中，您将模拟1916年约旦铁路网络的建设。

您的任务：
-----------
确定建造九个火车站的最便宜顺序，使总建设成本不超过给定预算。

规则：
------
1. 每个车站都有基础建设成本（见STATION_COSTS字典）
2. 建造车站的最终成本取决于：
   - 之前建造的车站
   - 您学生ID的最后一位数字

车站成本公式：
    最终成本 = 当前站基础成本 +
               前一站基础成本 * (SID + 1)^1.3 *
               (1 + 0.07 * (当前站索引 % 3))

完成步骤：
------------------
- 按照文档字符串中的描述实现每个函数
- 使用循环或排列来探索可能的站点顺序
- 返回预算内最便宜的有效顺序

注意：
-----
如果您的解决方案在预算内找到*一个有效*顺序，
即使它不是绝对最便宜的，也会获得部分分数。
"""

# -------------------- 第1部分：全局变量 -------------------- #

STATION_COSTS = {
    # 九个车站及其基础成本
    "Amman": 12,      # 安曼（首都）
    "Petra": 8,       # 佩特拉（古城）
    "Karak": 10,      # 卡拉克
    "Irbid": 7,       # 伊尔比德
    "Salt": 6,        # 萨尔特
    "Aqaba": 9,       # 亚喀巴（港口城市）
    "Jerash": 11,     # 杰拉什（古罗马城市）
    "Madaba": 7,      # 马代巴
    "Mafraq": 8       # 马夫拉克
}


# -------------------- 第2部分：函数 -------------------- #

def is_valid_sid(sid: str) -> bool:
    """
    检查提供的学生ID（SID）是否有效
    
    有效的SID必须：
    - 是数字
    - 恰好包含9个字符
    
    参数：
        sid (str): 要验证的学生ID
    
    返回：
        bool: 如果SID有效返回True，否则返回False
    """
    if sid.isdigit() and len(sid) == 9:
        return True
    else:
        return False


def calculate_station_cost(current_station: str, previous_station: str, sid_last_digit: int) -> float:
    """
    根据动态定价机制计算建造车站的最终成本
    
    公式：
        最终成本 = 当前站基础成本 +
                   前一站基础成本 * (SID + 1)^1.3 *
                   (1 + 0.07 * (当前站索引 % 3))
    
    参数：
        current_station (str): 当前车站的名称
        previous_station (str): 之前建造的车站的名称
        sid_last_digit (int): 学生ID的最后一位数字（0-9）
    
    返回：
        float: 建造当前车站的最终计算成本
    """
    # 获取所有车站名称列表
    temp = list(STATION_COSTS.keys())
    # 找到当前车站的索引
    idx = temp.index(current_station)
    # 应用成本公式
    final_cost = (STATION_COSTS[current_station] + STATION_COSTS[previous_station] *
                  ((sid_last_digit + 1) ** 1.3) * (1 + 0.07 * (idx % 3)))
    return final_cost


def calculate_total_order_cost(order: list[str], sid_last_digit: int) -> float:
    """
    计算建造完整车站序列的总成本
    
    每个车站的成本根据其在顺序中的位置计算：
    - 第一个车站使用其基础成本
    - 所有其他车站使用calculate_station_cost()与之前建造的车站
    
    参数：
        order (list[str]): 按建设顺序排列的车站列表
        sid_last_digit (int): 学生ID的最后一位数字（0-9）
    
    返回：
        float: 建造整个铁路的总成本
    """
    total_cost = 0
    # 遍历建设顺序中的每个车站
    for i in range(len(order)):
        if i == 0:
            # 第一个车站只需基础成本
            total_cost += STATION_COSTS[order[i]]
            continue
        # 后续车站需要考虑前一个车站的影响
        total_cost += calculate_station_cost(order[i], order[i - 1], sid_last_digit)
    return total_cost


def build_railway(stations: list[str], sid_last_digit: int, budget: int) -> list[str]:
    """
    探索每种可能的建造车站顺序，并返回不超过预算的最低总成本序列
    
    如果返回的有效顺序不是绝对最便宜但仍在预算内，可以获得部分分数。
    
    参数：
        stations (list[str]): 待建造的车站列表
        sid_last_digit (int): 学生ID的最后一位数字
        budget (int): 最大允许的总建设成本
    
    返回：
        list[str]: 要建造的车站顺序，如果不可能则返回空列表
    """

    def random_list(lst):
        """
        生成列表的所有排列（递归实现）
        参数：lst - 要排列的列表
        返回：所有可能排列的列表
        """
        if len(lst) == 1:
            return [lst]

        result = []
        # 对于列表中的每个元素
        for i in range(len(lst)):
            current = lst[i]
            # 获取除当前元素外的其余元素
            remaining = lst[:i] + lst[i + 1:]
            # 递归生成剩余元素的排列
            for p in random_list(remaining):
                result.append([current] + p)
        return result

    # 生成所有可能的车站建设顺序
    temp = random_list(stations)

    min_order = []   # 最便宜的顺序
    min_cost = 0     # 最低成本
    
    # 遍历所有可能的顺序
    for i in temp:
        # 计算当前顺序的成本
        cost = calculate_total_order_cost(i, sid_last_digit)
        # 如果超出预算，跳过
        if cost >= budget:
            continue

        # 如果这是第一个有效顺序，记录它
        if min_cost == 0:
            min_cost = cost
            min_order = i
            continue

        # 如果成本不低于当前最低成本，跳过
        if cost >= min_cost:
            continue
        else:
            # 找到更便宜的顺序，更新记录
            min_cost = cost
            min_order = i
            continue
    
    return min_order


def find_affordable_railway(stations: list[str], sid_last_digit: int, budgets: list[int]) -> list[str]:
    """
    通过测试多个预算来尝试找到有效的铁路建设顺序
    
    该函数应该：
      - 按给定顺序遍历`budgets`
      - 使用`continue`跳过明显太低的预算
      - 使用`break`在找到第一个允许完整有效铁路顺序的预算后停止搜索
      - 返回为该第一个充足预算找到的有效顺序
      - 如果没有预算允许完整的铁路，返回空列表
    
    参数：
        stations (list[str]): 要考虑的车站名称列表
        sid_last_digit (int): 学生ID的最后一位数字（0-9）
        budgets (list[int]): 要尝试的预算列表（例如[100, 150, 200]）
    
    返回：
        list[str]: 在预算内找到的第一个有效铁路顺序，
                   如果没有足够的预算则返回空列表
    
    学生注意事项：
        - 不要硬编码预算阈值；您可以计算启发式最小值
          （例如，基础成本之和）并使用它来决定是否`continue`
        - 确保在循环逻辑中应用高级控制流（这些结构正在被评估）
    """
    # 遍历所有预算
    for i in budgets:
        # 尝试用当前预算建造铁路
        min_order = build_railway(stations, sid_last_digit, i)
        # 如果找到有效顺序，立即返回
        if min_order:
            return min_order
    # 如果所有预算都不够，返回空列表
    return []

# -------------------- 第3部分：示例执行 -------------------- #

if __name__ == "__main__":
    # 测试的示例占位符
    sid = "123456789"
    sid_last_digit = int(sid[0]) if sid.isnumeric() and len(sid) >= 1 else 0
    budgets = [100, 200, 500]
    stations = list(STATION_COSTS.keys())

    # TODO: 实现函数后取消注释并测试
    # if not is_valid_sid(sid):
    #     print("Invalid student ID!")
    # else:
    #     order = find_affordable_railway(stations, sid_last_digit, budgets)
    #     if order:
    #         total_cost = calculate_total_order_cost(order, sid_last_digit)
    #         print("Cheapest order:", order)
    #         print("Total cost:", round(total_cost, 2))
    #     else:
    #         print("No valid order found for any budget.")
