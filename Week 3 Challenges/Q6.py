import sys

print("Secure System Login Program")
print()
bol = False

if len(sys.argv) == 3:
    if sys.argv[1].isdigit():
        if int(sys.argv[1]) > 0:
            for i in range(int(sys.argv[1])):
                pw = input(f"Enter password (attempt {i+1} of {sys.argv[1]}): ")
                if pw == sys.argv[2]:
                    bol = True
                    break
                else:
                    print("Incorrect password.")
            print()
            if bol:
                print("Password Accepted. Welcome!")
            else:
                print("Access denied. Goodbye.")
        else:
            print("Invalid arguments.")
    else:
        print("Invalid arguments.")
else:
    print("Invalid arguments.")