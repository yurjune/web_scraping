import requests
from bs4 import BeautifulSoup
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
url = 'https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=recent&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=4&backgroundColor='
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

# 쿠팡 노트북 1페이지 제품 정보 스크래핑
items = soup.find_all('li', attrs={'class': re.compile('^search-product')})

for i in items:
    # 광고 상품 제외
    ad_badge = i.find('span', attrs={'class': 'ad-badge-text'})
    if ad_badge:
        print(' <광고 상품 제외합니다>')
        continue

    name = i.find('div', attrs={'class': 'name'}).get_text()
    # 애플 제품 제외
    if 'Apple' in name:
        print(' <Apple상품 제외합니다>')
        continue

    price = i.find('strong', attrs={'class': 'price-value'}).get_text()

    rate = i.find('em', attrs={'class': 'rating'})  # 평점이 없는 제품은 텍스트 없음
    if rate:
        rate = rate.get_text()
    else:
        print(' <평점 없는 상품 제외합니다>')
        continue

    # 평점이 있으면 평점수도 존재: get_text() 바로 사용 가능
    rate_cnt = i.find('span', attrs={'class': 'rating-total-count'}).get_text()[1:-1]   # float 사용할 수 있게 괄호 제거

    # 평점 4.5이상, 리뷰 100개이상만 조회
    if float(rate) >= 4.5 and float(rate_cnt) >= 100:
        print(name, price, rate, rate_cnt)
