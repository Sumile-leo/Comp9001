# Armin wrote a function times_two that takes in a list and multiplies each number
# by 2. Since mutable arguments are passed by reference, this will modify the same
# list outside the function. This is a side effect. Run the program and observe
# how nums is modified after the function executes.
#
# Armin needs to run off to a lecture and has tasked you with the following:
# Modify the function times_two(nums) to make sure that the function has no side
# effects - the list nums after execution should not be changed, however still
# returns a new list with each number multiplied by 2.

def times_two(ls: list[int]) -> list[int]:
    temp = ls.copy()
    for i in range(len(temp)):
        temp[i] *= 2
    return temp

nums = [1, 2, 3]
result = times_two(nums)
print('nums:', nums)     # Prints: [1, 2, 3]
print('result:', result) # Prints: [2, 4, 6]