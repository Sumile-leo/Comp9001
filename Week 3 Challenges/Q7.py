import sys


class tomatoes:
    def __init__(self, review):
        self.review = review

    def welcome(self):
        print(
            "Hello, welcome to Fresh Tomatoes! For a list of commands, enter 'help'. To exit, enter 'exit'")

    def exit(self):
        print("\nExiting. Goodbye!")

    def help(self):
        print("\nEnter the corresponding number to access that command."
              "\n1 : Print all reviews"
              "\n2 : Choose a review by index and print the full review"
              "\n3 : Add a review"
              "\n4 : Delete a review")

    def special_case(self, enter='empty input'):
        print(f"Sorry, {enter} is not a valid command.")

    def print_reviews(self):
        print("Printing all reviews...")
        print("Index    Title    Rating    Reviewer")
        for i in range(len(self.review)):
            print(
                f"{i + 1}    {self.review[i][0]}    {self.review[i][1]}    {self.review[i][2]}")

    def command(self, enter):
        if enter == '1':
            if len(self.review) == 0:
                print("No reviews found.")
                self.help()
            else:
                print()
                self.print_reviews()
                self.help()
        elif enter == '2':
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
            print()
            print("Review add mode...")
            title = input("Please enter the title of the movie: ")
            while not title.strip():
                title = input(
                    "Invalid title. Please enter the title of the movie: ")
            rating = input("Please enter the rating of the movie out of 10: ")
            while (not rating.isdigit()) or (not 0 <= int(rating) <= 10):
                rating = input(
                    "Invalid rating. Please enter the rating of the movie out of 10: ")
            reviewer = input("Please enter the name of the reviewer: ")
            while not reviewer.strip():
                reviewer = input(
                    "Invalid reviewer name. Please enter the name of the reviewer: ")
            text = input("Please enter the textual review: ")
            while not text.strip():
                text = input(
                    "Invalid textual review. Please enter the textual review: ")
            print("Printing input review...")
            print(f"{title} {rating}/10")
            print(f"Reviewer: {reviewer}")
            print(f"Review: {text}")
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
    review = []
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
    tm = tomatoes(review)

    tm.welcome()

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
