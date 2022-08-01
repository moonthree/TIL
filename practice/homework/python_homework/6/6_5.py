def sum_of_digit(N):
    if N == 0:
        return 0
    else:
        return sum_of_digit(N//10) + (N%10)

if __name__ == "__main__":
    print(sum_of_digit(987))