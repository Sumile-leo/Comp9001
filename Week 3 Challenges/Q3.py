rain = input("Is it currently raining? ")
if rain.lower() == "yes":
    print("You should take the bus.")
else:
    far = int(input("How far in km do you need to travel? "))
    if far > 10:
        print("You should take the bus.")
    elif 2 <= far <= 10:
        print("You should ride your bike.")
    else:
        print("You should walk.")
