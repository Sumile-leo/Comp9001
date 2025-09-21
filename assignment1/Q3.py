class machine:

    def __init__(self):
        self.data = []
        self.count = []

    def welcome(self):
        print("Welcome to the VMIM System!\n")

    def hp(self):
        print("ADD <snack> <quantity>\nREMOVE <index>\nPRINT\nHELP\nEXIT")

    def add(self, snack, quantity):
        if snack in self.data:
            print("You already have this snack!")
        elif quantity <= 0:
            print("Quantity must be positive!")
        else:
            self.data.append(snack)
            self.count.append(quantity)
            print(f"Added: {snack} [{quantity}]")

    def remove(self, index):
        if index > len(self.data) or index <= 0:
            print("Invalid index!")
        else:
            name = self.data.pop(index - 1)
            self.count.pop(index - 1)
            print(f"Removed: {name}")

    def pr(self):
        if len(self.data) == 0:
            print("Your vending machine is empty!")
        else:
            for i in range(len(self.data)):
                print(f"{i + 1}: {self.data[i]} [{self.count[i]}]")

    def exit(self):
        print("Exiting VMIM System.")


def main():
    mc = machine()
    mc.welcome()
    while True:
        command = input("Enter command: ")
        parsed = list(map(lambda x: int(x) if x.isdigit() else x, command.split()))
        temp = False
        if len(parsed) == 1:
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
            if parsed[0] == 'REMOVE' and isinstance(parsed[1],int):
                mc.remove(parsed[1])
            else:
                temp = True
        elif len(parsed) == 3:
            if (parsed[0] == 'ADD' and isinstance(parsed[1],str)):
                mc.add(parsed[1], parsed[2])
            else:
                temp = True
        else:
            temp = True
        if temp:
            print("Invalid command!")
        print()


if __name__ == '__main__':
    main()