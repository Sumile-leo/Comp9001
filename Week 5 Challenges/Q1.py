def triforce(height):
    rows = height * 2
    cols = height * 4
    matrix = [[" " for _ in range(cols)] for _ in range(rows)]
    for i in range(len(matrix)):
        matrix[i][i] = "/"
        matrix[i][cols-i-1] = "\\"

    for i in range(len(matrix[0])):
        if matrix[0][i] == " ":
            matrix[0][i] = "_"

    for i in range(cols):
        if height + 1 <= i <= cols - height - 2:
            matrix[height][i] = "_"

    temp1 = height
    temp2 = height  * 4 - height - 1
    for i in range(height - 1 , -1 , -1):
        matrix[i][temp1] = '\\'
        matrix[i][temp2] = '/'
        temp1 += 1
        temp2 -= 1

    print()
    for i in range(len(matrix)-1,-1,-1):
        for j in range(len(matrix[i])-1,-1,-1):
            if matrix[i][j] == "\\":
                break
            else:
                matrix[i][j] = ''

    for i in range(len(matrix)-1,-1,-1):
        for j in matrix[i]:
            print(j,end='')
        print()


height = input("Enter height: ")
print()
if height.isdigit():
    temp = int(height)
    if 2 <= temp <= 20:
        triforce(temp)
    else:
        print("Invalid height.")
else:
    print("Invalid height.")