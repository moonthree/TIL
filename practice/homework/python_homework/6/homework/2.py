# 파이썬에서 리스트에 새로운 원소를 추가하는 방법에는
# append(x)와 extend(iterable)이 있고 두 함수의 차이점을 알아보겠습니다.
# (참고로 insert(i, x)함수도 있으며 위치 i에 x를 추가합니다.)

# list.append(x)는 리스트 끝에 x 1개를 그대로 넣습니다.
# list.extend(iterable)는 리스트 끝에 가장 바깥쪽 iterable의 모든 항목을 넣습니다.

# 실습
x = ['a', 'b', 'c']
y = ['d', 'e']
x.append(y)
print('x.append(y) : ', x)  # ['a', 'b', 'c', ['d', 'e']]
# append는 x 그 자체를 원소로 넣고

x.extend(y)
print('x.extend(y) : ', x)  # ['a', 'b', 'c', 'd', 'e']
# extend는 iterable의 각 항목들을 넣습니다.

# 리스트안에 리스트의 경우
a = ['Tick', 'Tock', 'Song']
b = [['Ping', 'Pong'], ['abcd', 'abcd']]
a.extend(b)
print('a : ', a)
# ['Tick', 'Tock', 'Song', ['Ping', 'Pong'], ['abcd', 'abcd']]
# extend는 가장 바깥 쪽 iterable을 넣습니다.

# 문자열일 경우
# extend는 문자열의 각 알파벳을 넣습니다.

# 결론
# ​list.append(x)는 리스트 끝에 x 1개를 그대로 넣습니다.
# list.extend(iterable)는 리스트 끝에 가장 바깥쪽 iterable의 모든 항목을 넣습니다.
