'''
You are given a Python module, functions.py, which will contain three functions:

Summing numbers: Calculates the sum of a list of numbers.
String concatenation: Combines a list of strings into a single string.
Prefix check: Determines if a word starts with any character from a given list.
Your task is to write a program (main.py) that imports these functions and provides
 an interactive command-based interface for users.

The program should repeatedly prompt the user for a command and execute the
corresponding function:

SUM – The user enters numbers separated by spaces, and the program returns their sum.
CONCAT – The user enters words separated by spaces, and the program returns them
concatenated into a single string.
STARTS_WITH – The user provides a word and a set of characters, and the program
checks whether the word starts with any of them.
EXIT – The program terminates.
'''


def my_sum(ls: list) -> int:
    temp = 0
    for i in ls:
        temp += i
    return temp
    # copy over
    pass

def my_string_concatenation(ls: list) -> str:
    temp = ''
    for i in ls:
        temp += i
    return temp
    # copy over
    pass

def starts_with(word: str, chars: list) -> bool:
    if word == '':
        return False
    elif len(chars) == 0:
        return False
    else:
        if word[0] in chars:
            return True
        else:
            return False
    # fill this in...
    pass

def main():
    while True:
        temp = input("Enter command [SUM | CONCAT | STARTS_WITH | EXIT]: ")
        if temp == 'EXIT':
            break
        elif temp == 'SUM':
            ls = list(map(int, input("Enter numbers separated by spaces: ").split()))
            print(f"Sum: {my_sum(ls)}")
        elif temp == 'CONCAT':
            ls = list(map(str, input("Enter numbers separated by spaces: ").split()))
            print(f"Concatenated String: {my_string_concatenation(ls)}")
        elif temp == 'STARTS_WITH':
            words = input("Enter a word: ")
            chars = list(map(str, input("Enter characters separated by spaces: ").split()))
            print(f"Result: {starts_with(words, chars)}")
        print()
    pass

if __name__ == '__main__':
    main()