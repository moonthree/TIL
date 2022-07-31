#0층 = 01 02 03 04           
#1층 = 01 03 06 10       
#2층 = 01 04 10 20

# i층의 j번째 호실 = i층의 j-1번째 호실 + i-1층의 j번째 호실        
# ex) 1층 3호실 = 1층 2호실(03) + 0층 3호실(03)

test_case = int(input())

for _ in range(test_case):
    floor = int(input())
    door = int(input())


    floor0 = [resident for resident in range(1, door+1)]    # 0층 거주자 리스트
                                                            # floor0 = [1, 2, 3, 4, 5...]

    for _ in range(floor):                      # 층수만큼 반복
        for i in range(1, door):                # 호수만큼 반복
            floor0[i] += floor0[i-1]            # floor0[i] = floor0[i] + floor0[i-1]
                                                # 0층 리스트 생성 후 1호실 제외하고 계속하여 리스트를 갱신
                                                # 1층 -> [floor0[0] == 1, 
                                                # floor0[1]=2 + floor0[0]=1 ... floor0[1] == 3 , 
                                                # floor0[2]=3 + floor0[1]=3 ... floor0[2] == 6 ,
                                                # floor0[3]=4 + floor0[2]=6 ... floor0[3] == 10 ,
                                                # ...]
                                                            
    print(floor0[-1])
