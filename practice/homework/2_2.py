s = input("입력하세요 : ")
s2 = s.strip('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]') #앞 뒤 특수문자 제거
s3 = s2.lower()              # 대문자를 소문자로
s4 = s3.capitalize()        # 첫문자를 대문자로
print(s4)