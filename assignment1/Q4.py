class student:
    def __init__(self, sid):
        self.sid = sid

    def tut(self):
        return int(self.sid[-2:]) // 25 + 1

    def sid_check(self):
        if len(self.sid) == 9 and self.sid.isdigit():
            return False
        else:
            return True

    def dt(self):
        dict_temp = {'id': self.sid, 'tutorial_group': self.tut()}
        return dict_temp


class system:
    def __init__(self):
        self.courses = {'COMP9001': 2, 'COMP9003': 3, 'COMP9017': 2}
        self.COMP9001 = []
        self.COMP9003 = []
        self.COMP9017 = []

    def welcome(self):
        print(
            "Welcome to the University of Sydney Course Registration System!\n")

    def exit(self):
        print("Goodbye!")

    def register(self, course, st: student):
        temp = getattr(self, course)
        if len(temp) == self.courses.get(course):
            print(
                f"Course {course} is full. Student {st.sid} could not be "
                f"registered.")
        else:
            tt = st.tut()
            dict_temp = st.dt()
            if dict_temp in temp:
                print(f"Student {st.sid} is already registered in"
                      f" {course}.")
            else:
                temp.append(dict_temp)
                print(
                    f"Student {st.sid} has been registered in {course} ("
                    f"Tutorial {tt}).")

    def drop(self, course, st: student):
        temp = getattr(self, course)
        dict_temp = st.dt()
        if dict_temp not in temp:
            print(f"Student {st.sid} is not registered in {course}.")
        else:
            temp.remove(dict_temp)
            print(f"Student {st.sid} has been dropped from {course}.")

    def schedule(self, st: student):
        temp = []
        tt = st.tut()
        dict_temp = st.dt()
        for i in self.courses.keys():
            if dict_temp in getattr(self, i):
                temp.append(f'{i} (Tutorial {tt})')
        if len(temp) == 0:
            print("No courses registered.")
        else:
            print(f"Student {st.sid} is enrolled in: {temp}")

    def listcourses(self):
        for i in self.courses.keys():
            temp = getattr(self, i)
            print(f"{i}: {len(temp)}/{self.courses.get(i)}")

    def courseinfo(self, course):
        temp = getattr(self, course)
        print(f"Course: {course}")
        print(f"Capacity: {self.courses.get(course)}")
        print(f"Enrolled: {temp}")

    def hp(self):
        print(
            "Supported commands:\n REGISTER <student_id> <course>\n DROP "
            "<student_id> "
            "<course>\n SCHEDULE <student_id>\n COURSEINFO "
            "<course>\n LISTCOURSES\n HELP\n EXIT")


def     main():
    sy = system()
    sy.welcome()
    while True:
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
                elif parsed[2].upper() not in ['COMP9001', 'COMP9003','COMP9017']:
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
                elif parsed[2].upper() not in ['COMP9001', 'COMP9003','COMP9017']:
                    print(f"Course {parsed[2].upper()} does not exist.")
                else:
                    sy.drop(parsed[2].upper(), st)
        else:
            temp = True
        if temp:
            print("Unknown command. Type HELP for commands.")


if __name__ == '__main__':
    main()