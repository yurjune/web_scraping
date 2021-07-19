import requests
from bs4 import BeautifulSoup

url = 'https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0'
res = requests.get(url)
res.raise_for_status
soup = BeautifulSoup(res.text, 'lxml')

items = soup.find('div', attrs={'class':'wrap_tbl tbl_trade'}).find('tbody').find_all('tr')
for idx, item in enumerate(items):
    i = item.find_all('td')
    print(f'=========== 매물 {idx+1} ===========')
    print('거래 :', i[0].get_text().strip())
    print('면적 :', i[1].get_text().strip(), '(공급/전용)')
    print('가격 :', i[2].get_text().strip(), '(만원)')
    print('동 :', i[3].get_text().strip())
    print('층 :', i[4].get_text().strip())
