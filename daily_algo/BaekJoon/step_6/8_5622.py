letter = input()

call_time = 0

for i in range(len(letter)):
    if letter[i] == 'A' or letter[i] == 'B' or letter[i] == 'C':
        call_time += 3
    elif letter[i] == 'D' or letter[i] == 'E' or letter[i] == 'F':
        call_time += 4
    elif letter[i] == 'G' or letter[i] == 'H' or letter[i] == 'I':
        call_time += 5
    elif letter[i] == 'J' or letter[i] == 'K' or letter[i] == 'L':
        call_time += 6
    elif letter[i] == 'M' or letter[i] == 'N' or letter[i] == 'O':
        call_time += 7
    elif letter[i] == 'P' or letter[i] == 'Q' or letter[i] == 'R' or letter[i] == 'S':
        call_time += 8
    elif letter[i] == 'T' or letter[i] == 'U' or letter[i] == 'V':
        call_time += 9
    elif letter[i] == 'W' or letter[i] == 'X' or letter[i] == 'Y' or letter[i] == 'Z':
        call_time += 10
print(call_time)