from re import A


def duplicated_letters(words):
    # duplicates = []
    # for word in words:
    #     if words.count(word) > 1 and word not in duplicates:
    #         duplicates.append(word)
    # return duplicates

    return list({word for word in words if words.count(word) > 1})

print(duplicated_letters('apple'))
print(duplicated_letters('banana'))