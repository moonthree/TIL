def low_and_up(word):
    new_str = ''
    for idx, char in enumerate(word):
        if idx % 2 == 1:
            new_str += char.upper()
        else:
            new_str += char.lower()
    return new_str

print(low_and_up('apple'))
print(low_and_up('banana'))