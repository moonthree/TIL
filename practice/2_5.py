crop = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]

price_king = 0
price_master = ''

for i in range(len(crop)):
    if crop[i][1] > price_king:
        price_king = crop[i][1]
        price_master = crop[i][0]

print(price_master)