import csv
import requests
from bs4 import BeautifulSoup

# csv작성
filename = '시가총액 1-200.csv'
f = open(filename, 'w', encoding='utf-8-sig', newline='')
writer = csv.writer(f)

# 네이버금융 코스피 시가총액
lst = []
for page in range(1, 5):
    url = 'https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page='
    res = requests.get(url+str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    # 타이틀 달기(종목명,현재가...)
    if not lst:
        titles = soup.find('table', attrs={'class':'type_2'}).find('thead').find_all('th')
        lst = [title.get_text() for title in titles]
        writer.writerow(lst)

    # 시가총액
    rows = soup.find('table', attrs={'class':'type_2'}).find('tbody').find_all('tr')  # tr만 find_all; tr이 종목이다
    for row in rows:
        columns = row.find_all('td')
        data = [column.get_text().strip() for column in columns]
        if len(columns) <= 1:   # 의미없는거 스킵
            continue
        # print(data)
        writer.writerow(data)    # 데이터 쓰기
        # 닫기 왜안할까?
    