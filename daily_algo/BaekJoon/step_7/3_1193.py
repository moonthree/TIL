#분수찾기

# 혼자 풀 떄 최초 접근을 행 혹은 열에서 규칙찾는식으로 가서 꼬임
# 대각선에 들어있는 숫자의 양이 1, 2, 3, 4, 5 순으로 커지는 방향으로 접근했어야 함

# 구글링
n = int(input())
line = 0
end = 0
while n > end:
    line += 1
    end += line

chai = end - n
if line % 2 == 0: # 짝수 일때
    top = line - chai
    bottom = chai + 1
else:
    top = chai + 1
    bottom = line - chai
print(f'{top}/{bottom}')



# self 풀이 포기
# x = int(input('a'))
# n = 0
# a = 0
# line = 0
# c = 0
# while True:
#     if x < a:
#         line = n-1
#         break
#     else:
#         a = a + n
#         n += 1

# first = 0
# for i in range(line):
#     if i%2 != 0:
#         first += 1
#     else :
#         first += 2*i

# print(first, 'first')

# result = 0
# if line%2 == 0:
#     result = x - first
#     print(f'{1+result}/{line-result} 짝수')
# else:
#     result = first - x
#     print(f'{1+result}/{line-result} 홀수')