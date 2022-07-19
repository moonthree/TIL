list_a = list(map(str, input('입력하세용 : ').split()))

len_a = len(list_a)
for i in range(len_a-1):
    if(list_a[i][-1:] == list_a[i+1][:1]):
        if len_a == i+2:
            print("pass")
        else:
            continue
    elif(list_a[i][-1:] != list_a[i+1][:1]):
        print("Fail")
        break