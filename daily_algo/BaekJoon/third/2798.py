# 블랙잭

n, m = map(int, input().split())

card_list = list(map(int, input().split()))

card_num = len(card_list)

new_list = []
for i in range(card_num):
    for j in range(i+1, card_num):
        for k in range(j+1, card_num):
            if card_list[i] + card_list[j] + card_list[k] <= m:
                new_list.append(card_list[i] + card_list[j] + card_list[k])
            else:
                continue
print(max(new_list))


