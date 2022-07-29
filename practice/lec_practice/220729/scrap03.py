#94cfb0b050444c186251cd8dee48a17d

#https://api.themoviedb.org/3/movie/popular?api_key=<<api_key>>&language=en-US&page=1

# 기본 주소
# https://api.themoviedb.org/3

# 추가 주소
# /movie/popular

# 추가 변수
# ?api_key=<<api_key>>&language=en-US&page=1

from urllib import response
import requests

# 1. URL 정보 설정
BASE_URL = 'https://api.themoviedb.org/3'
path = '/movie/popular'
params = {
    'api_key': '94cfb0b050444c186251cd8dee48a17d',
    'language': 'ko',
    'region': 'KR',
}

# 2. 요청 및 응답
response = requests.get(BASE_URL + path, params=params).json()
result = response.get('results')
print(result)