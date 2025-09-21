def main():
    while True:
        try:
            line = input()          
            print(line[::-1])
        except EOFError:
            break

if __name__ == "__main__":
    main()
