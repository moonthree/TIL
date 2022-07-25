H, M = map(int, input().split())

if M < 45 :
    if H == 0 :	# 0 시이면
        H = 23
        M += 60
    else :
        H -= 1	
        M += 60
        
print(H, M-45)