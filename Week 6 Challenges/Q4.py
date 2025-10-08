def caesar_cipher(text, key):
    result = ""

    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - 65 + key) % 26 + 65)
        elif ch.islower():
            result += chr((ord(ch) - 97 + key) % 26 + 97)
        else:
            result += ch

    return result

key = int(input("Enter key: "))
if key < 0 or key > 26:
    print()
    print("Invalid key!")
else:
    text = input("Enter line: ")
    print()
    print(caesar_cipher(text, key))
