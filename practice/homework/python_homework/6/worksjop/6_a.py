from re import A


def duplicated_letters(words):
    # duplicates = []
    # for word in words:
    #     if words.count(word) > 1 and word not in duplicates:
    #         duplicates.append(word)
    # return duplicates

    # List Comprehension 리스트 컴프리헨션
    # word // word를 반환한다.
    # for word in words // words의 길이만큼 words[i]를 word에 할당하면서
    # if words.count(word) // 만약 words에 있는 word의 숫자가 1보다 크다면
    # 
    print (list({i+'a' for i in words if words.count(i) > 1}))
    return list({word for word in words if words.count(word) > 1})

print(duplicated_letters('apple'))
print(duplicated_letters('banana'))