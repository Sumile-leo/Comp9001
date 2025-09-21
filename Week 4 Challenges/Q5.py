import sys
def future_month(x, y):
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    current = months[x - 1]
    future = months[(x - 1 + y) % 12]
    print(f"It's currently {current}, in {y} months it will be {future}.")

current = int(sys.argv[1])
later = int(sys.argv[2])

future = future_month(current, later)

