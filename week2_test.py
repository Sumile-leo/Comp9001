#
#
# print('Santa\nClaus')
#
#
#
# print('\n\n\n')

# print()
# print('\n\n\n', end='\n')
# print()

# pi = 3.14159
# print('pi:\t', pi)


# TEMPERATURE_LIMIT = 37.5
# TIME_CURFEW = 10
#
# hoarse_voice = True
# itchy_throat = False
# my_temperature = 38.5
# current_hour = 8
#
# has_bad_throat = hoarse_voice or itchy_throat
# has_fever = my_temperature > TEMPERATURE_LIMIT
# has_sore_throat = has_bad_throat and has_fever
# should_go_out = current_hour < TIME_CURFEW and not has_sore_throat
# 
# print(should_go_out)

# grid = [
#     ['_', '_', 'x'],
#     ['_', '_', '_'],
#     ['_', 'x', 'x']
# ]
#
# # write code below
# print(grid[0], grid[1], grid[2], sep='\n')
# print()
#
# target = input("Enter target coordinates: ")
# print()
# temp = target.split()
# print(temp)
# if (int(temp[0]) not in [0,1,2]) or (int(temp[1]) not in [0,1,2]):
#     print("Out of bounds!")
# elif grid[int(temp[0])][int(temp[1])] == 'x':
#     print("Already hit!")
# else:
#     grid[int(temp[0])][int(temp[1])] = 'x'
#     print("Attack successful!")
#     print(grid[0],grid[1],grid[2], sep='\n')

marks = {'Matthew': 84, 'Tim': 49, 'Jasmine': 98, 'N/A': 0}
marks.pop('N/A')
marks['matthew'] = 50
marks['peter'] = 74
print(marks)