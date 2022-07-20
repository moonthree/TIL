# 3-1 start
from functools import partial


def a():
    fruit = input('과일을 입력하세요.(형식 : apple,banana,rottenOrange,Orange) : ')
    fruit_lower = fruit.lower()
    fruit_split = fruit_lower.split(',')
    
    for i in range(len(fruit_split)):
        fruit_split[i] = fruit_split[i].replace('rotten','')
    print(fruit_split)
# 3-1 end

# 3-2 start
def b():
    strb = input('문자열을 입력하세용 : ')
    len_strb = len(strb)
    if len_strb % 2 != 0:
        print(strb[int(len_strb/2): int(len_strb/2)+1])
    else :
        print(strb[int(len_strb/2)-1: int(len_strb/2)+1])
# 3-2 end

# 3-3 start
def c():
    infos = [{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]
    age = list(_['age'] for _ in infos)
    print(sum(age))
# 3-3 end

# 3-4 start
def d():
    blood_types = [ 'A','A','O', 'B', 'A', 'O', 'AB','O', 'A', 'B', 'O', 'B', 'AB']
    count_blood = {}

    for i in blood_types:               # blood_types 리스트를 처음부터 꺼내서
        try: count_blood[i] += 1        # count_blood 빈 딕셔너리에 넣는다.
        except: count_blood[i] = 1      # 이때 count_blood에 이미 존재하면 try문이 실행되어 value에 +1을 하고 
                                        # count_blood에 없는 값이라면 except가 실행되어 value는 1로 저장된다.
    print(count_blood)
# 3-4 end

# 3-5 start
def e():
    salt_water = []
    salt = []
    n = 0
    while n < 5:
        done = input('종료하려면 "Done"을 계속하려면 아무키나 입력하세요. : ')
        if done != 'Done':
            salt_water_input = float(input('소금물의 양을 입력하세요. : '))
            per = float(input('소금물의 농도를 입력하세요. : '))
            salt_water.append(salt_water_input)
            salt.append(per/100*salt_water_input)
            n += 1
        elif done == 'Done':
            break
    mix_water = sum(salt_water) + sum(salt)
    mix_per = sum(salt)/sum(salt_water)*100

    print(f'소금물의 퍼센트 농도는 {round(mix_per, 2)}%, 소금물의 양은 {round(mix_water, 2)}g 입니다.')
# 3-5 end

# 3-6 start
def f():
    year = int(input("연도를 입력하세용 : "))
    if((year % 4 == 0) and (year % 100 != 0)) or year % 400 == 0:
        print("윤년입니다.")
    else:
        print("윤년이 아닙니다.")
# 3-6 end

# 3-7 start
def g():
    s_triangle = input('각 변의 길이를 콤마로 구분하여 입력하시오. ex)2,3,4 입력 : ')
    s_triangle1 = s_triangle.split(',')
    s_triangle1.sort()
    a = int(s_triangle1[0])
    b = int(s_triangle1[1])
    c = int(s_triangle1[2])

    tri = ""
    if a==b==c:
        tri = '정삼각형'
    elif a==b or b==c:
        tri = '이등변삼각형'
    elif a**2 + b**2 == c**2:
        tri = '직각삼각형'
    elif a + b <= c:
        tri = '삼각형이 아님'
    else:
        tri = '삼각형'
    print(tri)
# 3-7 end

# a()
# b()
# c()
# d()
# e()
# f()
# g()