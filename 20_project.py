import requests
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}

# 날씨
url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty\
    &fbm=0&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8'
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

info = soup.find('div', attrs={'class': 'main_info'})
whether = info.find('p', attrs={'class': 'cast_txt'}).get_text()
temp = info.find('span', attrs={'class': 'todaytemp'}).get_text()
min = info.find('span', attrs={'class': 'min'}).get_text()
max = info.find('span', attrs={'class': 'max'}).get_text()

rain_1 = soup.find('span', attrs={'class': 'point_time morning'})\
    .find('span', attrs={'class': 'num'}).get_text()
rain_2 = soup.find('span', attrs={'class': 'point_time afternoon'})\
    .find('span', attrs={'class': 'num'}).get_text()

indi = soup.find('dl', attrs={'class': 'indicator'}).find_all('dd')
large = indi[0].get_text()
small = indi[1].get_text()

print('[오늘의 날씨]')
print(whether)
print(f'현재: {temp}℃  (최저: {min}℃  / 최고: {max}℃)')
print(f'오전 강수확률 {rain_1}% / 오후 강수확률 {rain_2}%')
print()
print(f'미세먼지 {large}')
print(f'초미세먼지 {small}')
print()

# 헤드라인 뉴스
url = 'https://news.naver.com/'
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

heads = soup.find('ul', attrs={'class': 'hdline_article_list'}).find_all('li')

print('[헤드라인 뉴스]')
for idx, head in enumerate(heads):
    name = head.find('a').get_text().strip()
    link = head.find('a')['href']
    print(f'{idx+1}. {name}')
    print(f' (링크 : https://www.news.naver.com{link} ')
    if idx == 2:
        break
print()

# IT뉴스
heads = soup.find('ul', attrs={'class': 'mlist2 no_bg'}).find_all('li')

print('[IT 뉴스]')
for idx, head in enumerate(heads):
    name = head.find('a').get_text().strip()
    link = head.find('a')['href']
    print(f'{idx+1}. {name}')
    print(f' (링크 : {link} ')
    if idx == 2:
        break
print()

# 영어회화
url = 'https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english\
    &logger_kw=haceng_submain_lnb_eng_I_others_english'
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

print('[오늘의 영어 회화]')
texts_eng = soup.find('div', attrs={'class': 'conv_container'})\
    .find_all('div', attrs={'class': 'conv_txtBox'})[1]\
    .find('div', attrs={'class': 'conv_txt'}).find_all('div')
texts_kor = soup.find('div', attrs={'class': 'conv_container'})\
    .find_all('div', attrs={'class': 'conv_txtBox'})[0]\
    .find('div', attrs={'class': 'conv_txt'}).find_all('div')

print('(영어 지문)')
for text in texts_eng:
    conversation = text.get_text().strip()
    print(conversation)
print()

print('(한글 지문)')
for text in texts_kor:
    conversation = text.get_text().strip()
    print(conversation)
