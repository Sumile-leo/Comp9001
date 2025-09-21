'''
Part 1: Sum Again

Implement the function my_sum() which takes in a list and returns the sum of all
 numbers in the list.

Ensure that your function will work with any amount of numbers in the list!

Avoid using the built-in function sum() as we want you to implement your own!

Part 2: String Concatenation

Implement the function my_string_concatentation which takes in a list and returns
 the concatenation of all strings in the list.

Part 3: Simple String Search

Implement the function starts_with(word, chars) that returns True or False depending
 on whether the string word begins with one of the characters in the list chars.
'''


def my_sum(ls: list[int]) -> int:
    temp = 0
    for i in ls:
        temp += i
    return temp
    pass

print(my_sum([1, 2, 3, 4, 5]))  # 15
print(my_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # 55








def my_string_concatenation(ls: list[str]) -> str:
    # fill this in...
    temp = ""
    for i in ls:
        temp += i
    return temp
    pass

list_of_strings = [
    'abc',
    'def',
    'ghi',
    'jkl',
    'mno',
    'pqr',
    'stu',
    'vwx',
    'yz'
]
# Prints: abcdefghijklmnopqrstuvwxyz
print(my_string_concatenation(list_of_strings))







def starts_with(word: str, chars: list[str]) -> bool:
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

print(starts_with('beer', ['a', 'b', 'c']))  # True
print(starts_with('deer', ['a', 'b', 'c']))  # False

print(starts_with('', ['a', 'b', 'c']))  # False
print(starts_with('starts_with', []))  # False