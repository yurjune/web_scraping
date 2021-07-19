from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.maximize_window()

# 페이지 이동
url = 'https://play.google.com/store/movies/top'
browser.get(url)

# # 해상도 높이인 1080위치로 스크롤 내리기
# browser.execute_script('window.scrollTo(0,1080)')

# # 화면 가장 아래로 스크롤내리기
# browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')

# 현재 문서 높이를 저장
prev_height = browser.execute_script('return document.body.scrollHeight')

while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

    # 페이지 로딩 대기
    time.sleep(2)

    # 현재 문서 높이를 저장
    curr_height = browser.execute_script('return document.body.scrollHeight')

    if curr_height == prev_height:
        break

    prev_height = curr_height

print('스크롤 완료')

# 이제 스크래핑

import requests
from bs4 import BeautifulSoup
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Accept-Language':'ko-KR,ko'
    }

soup = BeautifulSoup(browser.page_source, 'lxml')

# 영화 정보 검색
movies = soup.find_all('div', attrs={'class':['Vpfmgd']})
print(len(movies))

# 영화 출력
for movie in movies:
    # 제목
    title = movie.find('div', attrs={'class':'WsMG1c nnK0zc'}).get_text()
    
    # 할인 전 금액 / 할인정보 없으면 탈출
    original_price = movie.find('span', attrs={'class':'SUZt4c djCuy'})
    if original_price:
        original_price = original_price.get_text()
    else:
        continue

    # 할인 후 금액
    price = movie.find('span', attrs={'class':'VfPpfd ZdBevf i5DZme'}).get_text()

    # 영화 링크
    link = movie.a['href']

    # 출력
    print('제목:', title)
    print('할인 전 금액:', original_price)
    print('할인 후 금액:', price)
    print('링크:', 'https://play.google.com' + link)
    print('-'*60)

browser.quit()