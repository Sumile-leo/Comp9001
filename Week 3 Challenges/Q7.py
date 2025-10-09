# Fresh Tomatoes 电影评论系统
# 功能：一个完整的电影评论管理系统，支持查看、添加、删除评论

import sys


class tomatoes:
    """电影评论管理类"""
    
    def __init__(self, review):
        """
        初始化评论系统
        参数：review - 评论列表，每个评论包含[标题, 评分, 评论者, 评论内容]
        """
        self.review = review

    def welcome(self):
        """显示欢迎信息"""
        print(
            "Hello, welcome to Fresh Tomatoes! For a list of commands, enter 'help'. To exit, enter 'exit'")

    def exit(self):
        """显示退出信息"""
        print("\nExiting. Goodbye!")

    def help(self):
        """显示帮助信息，列出所有可用命令"""
        print("\nEnter the corresponding number to access that command."
              "\n1 : Print all reviews"
              "\n2 : Choose a review by index and print the full review"
              "\n3 : Add a review"
              "\n4 : Delete a review")

    def special_case(self, enter='empty input'):
        """处理无效命令"""
        print(f"Sorry, {enter} is not a valid command.")

    def print_reviews(self):
        """打印所有评论的简要信息"""
        print("Printing all reviews...")
        print("Index    Title    Rating    Reviewer")
        for i in range(len(self.review)):
            print(
                f"{i + 1}    {self.review[i][0]}    {self.review[i][1]}    {self.review[i][2]}")

    def command(self, enter):
        """
        处理用户命令
        参数：enter - 用户输入的命令（1/2/3/4）
        """
        if enter == '1':
            # 命令1：打印所有评论
            if len(self.review) == 0:
                print("No reviews found.")
                self.help()
            else:
                print()
                self.print_reviews()
                self.help()
                
        elif enter == '2':
            # 命令2：选择并打印完整评论
            if len(self.review) == 0:
                print("No reviews found.")
                self.help()
            else:
                print()
                print("Select a review by index to print the full review!")
                self.print_reviews()
                while True:
                    index = int(input())
                    if 1 <= index <= len(self.review):
                        print("\nPrinting selected review...")
                        print(
                            f"{self.review[index - 1][0]} {self.review[index - 1][1]}")
                        print(f"Reviewer: {self.review[index - 1][2]}")
                        print(f"Review: {self.review[index - 1][3]}")
                        self.help()
                        break
                    else:
                        print("Invalid index, try again!")
                        
        elif enter == '3':
            # 命令3：添加新评论
            print()
            print("Review add mode...")
            # 输入并验证电影标题
            title = input("Please enter the title of the movie: ")
            while not title.strip():
                title = input(
                    "Invalid title. Please enter the title of the movie: ")
            # 输入并验证评分（0-10）
            rating = input("Please enter the rating of the movie out of 10: ")
            while (not rating.isdigit()) or (not 0 <= int(rating) <= 10):
                rating = input(
                    "Invalid rating. Please enter the rating of the movie out of 10: ")
            # 输入并验证评论者名字
            reviewer = input("Please enter the name of the reviewer: ")
            while not reviewer.strip():
                reviewer = input(
                    "Invalid reviewer name. Please enter the name of the reviewer: ")
            # 输入并验证评论内容
            text = input("Please enter the textual review: ")
            while not text.strip():
                text = input(
                    "Invalid textual review. Please enter the textual review: ")
            # 显示输入的评论
            print("Printing input review...")
            print(f"{title} {rating}/10")
            print(f"Reviewer: {reviewer}")
            print(f"Review: {text}")
            # 确认是否添加
            check = input("Do you want to add the following review to the "
                          "database? y/n ")
            while True:
                if check == 'y':
                    print("Review added!")
                    rw = [title, f"{rating}/10", reviewer, text]
                    self.review.append(rw)
                    break
                elif check == 'n':
                    print("Review dumped")
                    break
                else:
                    check = input(
                        "Invalid input: Do you want to add the following review to the database? y/n ")
            print("Exiting review add mode...")
            self.help()
            
        elif enter == '4':
            # 命令4：删除评论
            if len(self.review) == 0:
                print("No reviews found.")
                self.help()
            else:
                print()
                print(
                    "Review delete mode...\nSelect a review by index to delete it.")
                self.print_reviews()
                while True:
                    index = int(input())
                    if 1 <= index <= len(self.review):
                        print()
                        print("Delete the selected review? y/n")
                        print(
                            f"{self.review[index - 1][0]} {self.review[index - 1][1]}")
                        print(f"Reviewer: {self.review[index - 1][2]}")
                        print(f"Review: {self.review[index - 1][3]}")
                        bol = input()
                        while True:
                            if bol == 'y':
                                print("Review deleted.")
                                self.review.pop(index - 1)
                                break
                            elif bol == 'n':
                                print("Review not deleted.")
                                break
                            else:
                                bol = input(
                                    "Invalid input: Do you want to delete the selected review? y/n ")
                        break
                    else:
                        print("Invalid index, try again!")
                print("Exiting review delete mode...")
                self.help()


def main():
    """主函数：初始化系统并处理用户交互"""
    review = []
    # 如果提供了'demo'参数，加载演示数据
    if len(sys.argv) == 2:
        if sys.argv[1] == 'demo':
            review.append(['The Boys', '10/10', 'Knopp B',
                           'Hallmark of our generation, perfect film in every way.'])
            review.append(['Adult Driver', '10/10', 'Gio P',
                           'Great movie with fast cars, starring Adult Driver Adam Driver.'])
            review.append(['End Of Neon Genesis', '10/10', 'Michael Pod',
                           'Gorgeous, deep plot, trippy visuals.'])
            review.append(['Samurai Shampoo', '10/10', 'Niruth B',
                           'Great soundtrack, even better plot and fight choreography.'])
    
    # 创建评论系统实例
    tm = tomatoes(review)

    # 显示欢迎信息
    tm.welcome()

    # 主循环：持续接收用户命令
    while True:
        enter = input()
        if enter == 'exit':
            tm.exit()
            break
        elif enter == 'help':
            tm.help()
        elif enter in ['1', '2', '3', '4']:
            tm.command(enter)
        else:
            if enter == '':
                tm.special_case()
            else:
                tm.special_case(enter)


if __name__ == '__main__':
    main()
