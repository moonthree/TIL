letter = input()

upper_letter = letter.upper()                           # 모두 대문자로 변환
list_set_letter = list(map(str, set(upper_letter)))     # set()으로 중복 제거 후 list로 반환

dict_letter = {}
for spell in list_set_letter:                           # 중복 제거 한 리스트에 있는 알파벳으로 카운트하여 딕셔너리에 키, 값 형태로 배정
    dict_letter[spell] = upper_letter.count(spell)

sort_dict_letter = sorted(dict_letter.items(), key=lambda x: x[1], reverse=True) # 카운트로 sort

if len(letter) == 1:                                        # letter가 스펠링 하나일 때 index error 방지
    print(sort_dict_letter[0][0])
else:       
    if sort_dict_letter[0][1] == sort_dict_letter[1][1]:    # 카운트가 동일한 경우
        print('?')
    else:
        print(sort_dict_letter[0][0])