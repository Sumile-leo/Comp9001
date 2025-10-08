# Returns the mean of the given data set.
import math
import sys


def mean(numbers):
    total = sum(numbers)
    return total / len(numbers)

# Returns the variance of the given data set.
def variance(numbers, mean):
    total = 0
    for i in numbers:
        temp = i - mean
        total += temp * temp
    return total / len(numbers)

# Returns the standard deviation of the given data set.
def sd(variance):
    return math.sqrt(variance)
    pass


def main():
    temp = []

    print("Enter data set:")
    for line in sys.stdin:
        try:
            for i in line.strip().split():
                temp.append(float(i))
        except ValueError:
            pass
    print()
    if not temp:
        print("No data!")
        sys.exit()
    m = mean(temp)
    v = variance(temp,m)
    s = sd(v)
    print(f"Mean = {m:.4f}")
    print(f"Variance = {v:.4f}")
    print(f"Standard deviation = {s:.4f}")



if __name__ == '__main__':
    main()