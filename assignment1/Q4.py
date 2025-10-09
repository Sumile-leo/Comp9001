# 悉尼大学课程注册系统
# 功能：管理学生的课程注册、退课、查询课程信息等操作

class student:
    """学生类"""
    
    def __init__(self, sid):
        """
        初始化学生对象
        参数：sid - 学生ID（9位数字）
        """
        self.sid = sid

    def tut(self):
        """
        根据学生ID计算所属的辅导班（Tutorial）编号
        规则：ID的最后两位数字 // 25 + 1
        返回：辅导班编号
        """
        return int(self.sid[-2:]) // 25 + 1

    def sid_check(self):
        """
        验证学生ID是否有效
        有效ID：必须是9位数字
        返回：True表示无效，False表示有效
        """
        if len(self.sid) == 9 and self.sid.isdigit():
            return False
        else:
            return True

    def dt(self):
        """
        生成学生的字典表示
        返回：包含ID和辅导班编号的字典
        """
        dict_temp = {'id': self.sid, 'tutorial_group': self.tut()}
        return dict_temp


class system:
    """课程注册系统类"""
    
    def __init__(self):
        """初始化系统，设置课程容量和学生列表"""
        # 课程及其最大容量
        self.courses = {'COMP9001': 2, 'COMP9003': 3, 'COMP9017': 2}
        # 每门课程的注册学生列表
        self.COMP9001 = []
        self.COMP9003 = []
        self.COMP9017 = []

    def welcome(self):
        """显示欢迎信息"""
        print(
            "Welcome to the University of Sydney Course Registration System!\n")

    def exit(self):
        """显示退出信息"""
        print("Goodbye!")

    def register(self, course, st: student):
        """
        注册学生到指定课程
        参数：course - 课程代码
              st - 学生对象
        """
        # 获取课程的学生列表
        temp = getattr(self, course)
        # 检查课程是否已满
        if len(temp) == self.courses.get(course):
            print(
                f"Course {course} is full. Student {st.sid} could not be "
                f"registered.")
        else:
            tt = st.tut()
            dict_temp = st.dt()
            # 检查学生是否已注册
            if dict_temp in temp:
                print(f"Student {st.sid} is already registered in"
                      f" {course}.")
            else:
                # 添加学生到课程
                temp.append(dict_temp)
                print(
                    f"Student {st.sid} has been registered in {course} ("
                    f"Tutorial {tt}).")

    def drop(self, course, st: student):
        """
        从指定课程中退课
        参数：course - 课程代码
              st - 学生对象
        """
        temp = getattr(self, course)
        dict_temp = st.dt()
        # 检查学生是否已注册该课程
        if dict_temp not in temp:
            print(f"Student {st.sid} is not registered in {course}.")
        else:
            # 从课程中移除学生
            temp.remove(dict_temp)
            print(f"Student {st.sid} has been dropped from {course}.")

    def schedule(self, st: student):
        """
        查询学生的课程表
        参数：st - 学生对象
        """
        temp = []
        tt = st.tut()
        dict_temp = st.dt()
        # 遍历所有课程，查找学生已注册的课程
        for i in self.courses.keys():
            if dict_temp in getattr(self, i):
                temp.append(f'{i} (Tutorial {tt})')
        # 输出结果
        if len(temp) == 0:
            print("No courses registered.")
        else:
            print(f"Student {st.sid} is enrolled in: {temp}")

    def listcourses(self):
        """列出所有课程及其注册情况"""
        for i in self.courses.keys():
            temp = getattr(self, i)
            print(f"{i}: {len(temp)}/{self.courses.get(i)}")

    def courseinfo(self, course):
        """
        显示指定课程的详细信息
        参数：course - 课程代码
        """
        temp = getattr(self, course)
        print(f"Course: {course}")
        print(f"Capacity: {self.courses.get(course)}")
        print(f"Enrolled: {temp}")

    def hp(self):
        """显示帮助信息"""
        print(
            "Supported commands:\n REGISTER <student_id> <course>\n DROP "
            "<student_id> "
            "<course>\n SCHEDULE <student_id>\n COURSEINFO "
            "<course>\n LISTCOURSES\n HELP\n EXIT")


def main():
    """主函数：处理用户交互"""
    sy = system()
    sy.welcome()
    
    while True:
        # 读取并解析命令
        command = input("Enter command: ")
        temp = False
        parsed = list(map(str, command.split()))
        
        if parsed[0].upper() == "HELP":
            sy.hp()
        elif parsed[0].upper() == "EXIT":
            sy.exit()
            break
        elif parsed[0].upper() == "LISTCOURSES":
            sy.listcourses()
        elif parsed[0].upper() == "COURSEINFO":
            if len(parsed) != 2:
                print("Usage: COURSEINFO <course>")
            else:
                sy.courseinfo(parsed[1])
        elif parsed[0].upper() == "SCHEDULE":
            if len(parsed) != 2:
                print("Usage: SCHEDULE <student_id>")
            else:
                st = student(parsed[1])
                if st.sid_check():
                    print("Invalid student ID. Must be 9 digits.")
                else:
                    sy.schedule(st)
        elif parsed[0].upper() == "REGISTER":
            if len(parsed) != 3:
                print("Usage: REGISTER <student_id> <course>")
            else:
                st = student(parsed[1])
                if st.sid_check():
                    print("Invalid student ID. Must be 9 digits.")
                elif parsed[2].upper() not in ['COMP9001', 'COMP9003', 'COMP9017']:
                    print(f"Course {parsed[2].upper()} does not exist.")
                else:
                    sy.register(parsed[2].upper(), st)
        elif parsed[0].upper() == "DROP":
            if len(parsed) != 3:
                print("Usage: DROP <student_id> <course>")
            else:
                st = student(parsed[1])
                if st.sid_check():
                    print("Invalid student ID. Must be 9 digits.")
                elif parsed[2].upper() not in ['COMP9001', 'COMP9003', 'COMP9017']:
                    print(f"Course {parsed[2].upper()} does not exist.")
                else:
                    sy.drop(parsed[2].upper(), st)
        else:
            temp = True
        
        # 如果命令未知，提示用户
        if temp:
            print("Unknown command. Type HELP for commands.")


if __name__ == '__main__':
    main()
