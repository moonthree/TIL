def is_user_data_valid(user_data):
    pass
    # 여기에 코드를 작성합니다.
    # if bool(user_data['id']) and bool(user_data['password']):
    #     return(True)
    # else:
    #     return(False)
    if user_data['id'] == '' or user_data['password'] == '':
        return False
    else :
        return True
    # print(len(user_data['id'].split()))
    
    # if len(user_data['id'].split()) > 1:
    #     return False
    # else :
    #     return True
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    user_data1 = {
        'id': '',
        'password': '1q2w3e4r',
    }
    print(is_user_data_valid(user_data1)) 
    # False 

    user_data2 = {
        'id': 'jungssafy',
        'password': '1q2w3e4r',
    }
    print(is_user_data_valid(user_data2)) 
    # True