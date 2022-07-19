orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'

order_split = orders.split(',')
ice_count = 0

for i in range(len(order_split)):
    if "아이스" in order_split[i]:
        ice_count += 1
print(f'아이스 음료 주문은 {ice_count}개 입니다.')

count_dict = {}

for i in order_split:               # order_split 리스트를 처음부터 꺼내서
    try: count_dict[i] += 1         # count_dict이라는 빈 딕셔너리에 넣는다.
    except: count_dict[i] = 1       # 이때 count_dict에 이미 존재하면 try문이 실행되어 value에 +1을 하고 
                                    # count_dict에 없는 값이라면 except가 실행되어 value는 1로 저장된다.


print(count_dict)