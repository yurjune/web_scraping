import requests
from bs4 import BeautifulSoup
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Accept-Language':'ko-KR,ko'
    }
url = 'https://play.google.com/store/movies/top'
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

# 영화 정보 검색
movies = soup.find_all('div', attrs={'class':'ImZGtf mpg5gc'})
print(len(movies))  # 0으로 뜬다?

# # html 확인해보기: 영어임
# with open('movie.html', 'w', encoding='utf8') as f:
#     f.write(soup.prettify())

# 유저에이전트로 한글페이지 반환, 코드다시실행
# 동적페이지므로 영화 10개밖에안뜸
# 셀레늄을 쓰자

# 영화 제목 출력
for movie in movies:
    title = movie.find('div', attrs={'class':'WsMG1c nnK0zc'}).get_text()
    print(title)