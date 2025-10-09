# 交通方式建议程序
# 功能：根据天气和距离推荐合适的交通方式

# 询问是否正在下雨
rain = input("Is it currently raining? ")

# 如果正在下雨，建议乘公交
if rain.lower() == "yes":
    print("You should take the bus.")
else:
    # 如果没下雨，询问距离
    far = int(input("How far in km do you need to travel? "))
    
    # 根据距离推荐交通方式
    if far > 10:
        # 超过10公里，建议乘公交
        print("You should take the bus.")
    elif 2 <= far <= 10:
        # 2-10公里，建议骑自行车
        print("You should ride your bike.")
    else:
        # 小于2公里，建议步行
        print("You should walk.")
