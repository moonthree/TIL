def low_and_up(word):
    new_str = ''
    # word를 enumerate 순회 한다.
    # 인덱스와 객체를 쌍으로 담은 열거형(enumerate) 객체 반환
    # ex) apple
    # 0 a
    # 1 p -> P
    # 2 p
    # 3 l -> L
    # 4 e
    for idx, char in enumerate(word):
        if idx % 2 == 1:
            new_str += char.upper()
        else:
            new_str += char.lower()
    return new_str

print(low_and_up('apple'))
print(low_and_up('banana'))