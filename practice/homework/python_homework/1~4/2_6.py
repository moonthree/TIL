orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'

order_split = orders.split(',')
order_num = len(order_split)
print(f'총 주문 : {order_num}')

order_set = set(order_split)
order_list = list(order_set)
order_list_desc = sorted(order_list, reverse=True)
print(order_list_desc)