import requests
from bs4 import BeautifulSoup 

url = 'https://comic.naver.com/webtoon/list.nhn?titleId=675554' #가우스전자
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text,'lxml')

# # 가우스전자 제목,링크 가져오기
# cartoons = soup.find_all('td', attrs={'class':'title'})
# title = cartoons[0].a.get_text()
# link = cartoons[0].a['href']
# print(title)
# print('https://comic.naver.com'+link)

# # 여러회차 제목,링크 가져오기
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = 'https://comic.naver.com' + cartoon.a['href']
#     print(title,link)

# 평점 정보 빼오기: 평균평점계산
cartoons = soup.find_all('div',attrs={'class':'rating_type'})
total_rates = 0
for cartoon in cartoons:
    rate = cartoon.find('strong').get_text()
    print(rate)
    total_rates += float(rate)

print('평균 점수:', round(total_rates / len(cartoons), 3))
