# 가로, 세로 길이가 정수이고 넓이가 area인 직사각형에서 변의 길이 나열하기

area = int(input('직사각형의 넓이를 입력하세요. : '))

for i in range(1, area + 1):        # 1부터 area까지 1씩 증가하며 실행
    if i * i > area:                # i * i가 area를 초과하면 for문을 강제로 종료.. why? 가각형의 최대 넓이를 초과하면서 가장 긴 변의 길이가 되므로
        break
    if area % i:                    # area가 i로 나누어 떨어지지 않으면 i는 변의 길이(약수)가 될 수 없음
        continue                    # 따라서 출력할 필요가 없음
    print(f'{i} x {area // i}')     
