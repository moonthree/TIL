def group_anagrams(words):
    from collections import defaultdict

    result = defaultdict(list)
    for i in words:
        result[''.join((sorted(list(i))))].append(i)

    values_list = list(result.values())
    return values_list


if __name__ == "__main__":
    words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    print(group_anagrams(words))