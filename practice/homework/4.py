# 4-1 start
# 맞는 비밀번호를 입력할 때까지 반복하는 코드 작성
# 비밀번호 3번 이상 틀릴 시 종료
def a():
    pw = 'abcd'
    n = 0
    while n < 3:
        pw_input = input('비밀번호를 입력하세요. : ')
        if pw_input == pw:
            print('로그인')
            break
        else:
            print('비밀번호가 다릅니다.')
            n += 1
            continue
    if n == 3:
        print('비밀번호를 3번 틀렸습니다.')
#a()
# 4-1 end

# 4-2 start
def b():
    # 주어진 리스트에서 득표가 많은 순서대로 출력
    # 딕셔너리를 사용할 것
    students = ['박해피', '이영희', '조민지', '조민지', 
            '김철수', '이영희', '이영희', '김해킹',
            '박해피', '김철수', '한케이', '강디티',
            '조민지', '박해피', '김철수', '이영희',
            '박해피', '김해킹', '박해피', '한케이','강디티']
    candidate = list(set(students)) #후보자만 나오도록 리스트 생성
    candidate_dict = {}

    # candidate_dict에 '후보자' : 0 의 딕셔너리 형태로 담기
    for i in candidate:
        candidate_dict[f'{i}'] = 0
    # 투표하기
    for i in students:
        candidate_dict[i] = candidate_dict[i] + 1

    # 밸류로 정렬해서 출력하기?
    print(dict(sorted(candidate_dict.items(), key=lambda x:x[1], reverse=True)))

#b()
# 4-2 end

# 4-3 start
def c():
    num = list(map(int, input('0~9 사이의 숫자 리스트를 입력하세요. ex(1 3 1 2 3 4 5 6) : ').split()))
    answer = []
    tmp = num[0]
    answer.append(tmp)
    
    for i in num:
        if i != tmp:
            tmp = i
            answer.append(i)
    print(answer)
#c()
# 4-3 end

# 4-4 start
def d():
    word1 = input('첫 번째 이름을 입력하세요 : ')
    word2 = input('두 번째 이름을 입력하세요 : ')

    a = list(word1)
    b = list(word2)
    a_sum = 0
    b_sum = 0

    for i in range(len(a)):
        a_sum += ord(a[i])
    for i in range(len(b)):
        b_sum += ord(b[i])
    
    if a_sum > b_sum :
        print(word1)
    elif a_sum < b_sum :
        print(word2)
    else:
        print('samesame')
#d()
# 4-4 end

# 4-5 start
def e():
    words_dict = {'proper' : '적절한',
        'possible' : '가능한',
        'moral' : '도덕적인',
        'patient' : '참을성 있는',
        'balance' : '균형',
        'perfect' : '완벽한',
        'logical' : '논리적인',
        'legal' : '합법적인',
        'relevant' : '관련 있는',
        'responsible' : '책임감 있는',
        'regular' : '규칙적인'}
    
    antonyms = []
    for key in words_dict:
        if key[0] in ['b', 'm', 'p'] :
            key = 'im'+key
        elif key[0] in 'l':
            key = 'il'+key
        elif key[0] in 'r':
            key = 'ir'+key
        antonyms.append(key)
    print(sorted(antonyms))
#e()
# 4-5 end

# 4-6 start
def f():
    num = 0
    last_spell_relay = []
    abcd = True
    while abcd:
        words = input('끝말잇기 단어를 입력하세요. 끝내려면 Done을 입력하세요. : ')
        if words == 'Done':
            break
        last_spell_relay.append(words)
        if len(last_spell_relay) > 1:
            if last_spell_relay[num][-1] != words[0]:
                print(f'{num+2}번째 사람이 탈락했습니다.')
                abcd = False
                break
            for i in range(num):
                if words == last_spell_relay[i]:
                    print(f'{num+2}번째 사람이 탈락했습니다.')
                    abcd = False
            num += 1
#f()
# 4-6 end

# 4-7 start
def g():
    from collections import defaultdict
    words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

    # 구글의 손길
    # result = defaultdict(list)
    # for i in words:
    #     result[''.join((sorted(list(i))))].append(i)
    #     print(result)
    # print(result.values())

    # 나의 손길
    a = []
    for i in words:
        split_words = []
        for j in range(3):
            split_words.append(i[j])
            split_words.sort()
        a.append([i, split_words])
    print(a)
    
    aet = ['a', 'e', 't']
    ant = ['a', 'n', 't']
    abt = ['a', 'b', 't']

    aet2 = []
    ant2 = []
    abt2 = []
    for i in a:
        if i[1] == aet:
            aet2.append(i[0])
        elif i[1] == ant:
            ant2.append(i[0])
        elif i[1] == abt:
            abt2.append(i[0])
    
    print(aet2)
    print(ant2)
    print(abt2)
    #print(a)
g()
# 4-7 end