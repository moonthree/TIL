def three(sentence):
    
    s2 = sentence.strip('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]') #앞 뒤 특수문자 제거
    s3 = s2.lower()              # 대문자를 소문자로
    s4 = s3.capitalize()        # 첫문자를 대문자로
    return s4

print(three('!@#@#@#qweqweqweqw,qweqQEWEDqw!@#!@'))