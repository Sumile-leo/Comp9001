temp = input()
count = [0]*10
for i in temp:
    count[int(i)] += 1

for i in range(10):
    print(f"{i}: {count[i]}")