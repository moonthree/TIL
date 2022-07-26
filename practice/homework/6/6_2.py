def price_king(grain_lst):
    price_king = 0
    price_master = ''

    for i in range(len(grain_lst)):
        if grain_lst[i][1] > price_king:
            price_king = grain_lst[i][1]
            price_master = grain_lst[i][0]
    return price_master



if __name__ == "__main__":
    grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]
    print(price_king(grain_lst))