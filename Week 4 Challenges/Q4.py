import sys

def main():
    words = sys.argv[1:]
    if not words:
        print(0)
        return

    count = {}

    repetitions = 0

    for w in words:
        prev = count.get(w, 0)
        if prev >= 1:
            repetitions += 1
        count[w] = prev + 1

    print(repetitions)

if __name__ == "__main__":
    main()
