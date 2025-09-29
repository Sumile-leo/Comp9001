import string

def is_anagram(str1, str2):
    translator = str.maketrans('', '', string.punctuation + " ")
    str1 = str1.translate(translator).lower()
    str2 = str2.translate(translator).lower()

    return sorted(str1) == sorted(str2)


s1 = input("Enter line: ")
s2 = input("Enter anagram: ")

if is_anagram(s1, s2):
    print("Anagram!")
else:
    print("Not an anagram.")
