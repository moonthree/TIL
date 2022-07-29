import requests
from bs4 import BeautifulSoup

# 요청을 보내는 주소
url = 'https://finance.naver.com/sise/'

# 요청을 보내고 받음 (텍스트 데이터를 받음)
response = requests.get(url).text

# BeautifulSoup를 이용해 텍스트 데이터를 html 구조로 변환
data = BeautifulSoup(response)

#print(data)

# 원하는 정보 뽑아서 출력
kospi = data.select_one('#popularItemList')
print(kospi.text)
