#구구단 곱셈표 출력하기

for i in range(1, 10):                  # 행 루프
    for j in range(1, 10):                  # 열 루프
        print(f'{i * j:3}', end=' ')        # i * j : 3 -> i * j 를 3자리로 출력
    print()                             # 행 변경