def is_id_valid(user_data):
    pass
    # 여기에 코드를 작성합니다.
    boolean = True
    print(user_data['id'][-1:])
    for i in range(0, 10):
        if user_data['id'][-1:] == str(i):
            boolean = True
            break
        else:
            boolean = False
    return boolean

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    user_data1 = {
        'id': 'jungssafy5',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data1)) 
    # True
    
    user_data2 = {
        'id': 'kimssafy!',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data2)) 
    # False