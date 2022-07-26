def only_square_area(a, b):
    #print(a, b)
    square = []
    for i in a:
        for j in b:
            if i == j:
                square.append(i*j)
    return square

if __name__ == "__main__":
    print(only_square_area([32, 55, 63], [13, 32, 40, 55]))