import requests

# 요청을 보내는 주소
url = 'https://www.naver.com/'

# 요청을 보내고 받음
response = requests.get(url).text
print(response)