# 클린코드 작성하자!

n = int(input())

group_word = 0
for _ in range(n):
    word = input()
    group_check = 0
    for i in range(len(word)-1):                # 인덱스 범위 생성 : 0부터 단어개수 -1까지 
        if word[i] != word[i+1]:                # 연달은 두 문자가 다른 때,
            new_word = word[i+1:]               # 현재글자 이후 문자열을 새로운 단어로 생성
            if new_word.count(word[i]) > 0:     # 남은 문자열에서 현재글자가 있있다면
                group_check += 1                # group_check에 1씩 증가.
    if group_check == 0:  
        group_word += 1                         # group_check가 0이면 그룹단어
print(group_word)