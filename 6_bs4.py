import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekday.nhn'
res = requests.get(url)
res.raise_for_status
soup = BeautifulSoup(res.text, 'lxml')  # 가져온 html문서(res.text)를 'lxml'파서를 통해서 Beautifulsoup객체로 만든 것

print(soup.title)   # soup객체를 통해 element에 접근
print(soup.title.get_text())

print(soup.a)   # soup에서 '처음'발견되는 a element 출력
print(soup.a.attrs)  # a element의 속성 출력
print(soup.a['href'])   # a element의 속성 '값' 출력

print(soup.find('a', attrs={'class': 'Nbtn_upload'}))    # class='Nbtn_upload'인 첫 a element 찾기
print(soup.find_all('a', attrs={'class': 'Nbtn_upload'}))    # class='Nbtn_upload'인 모든 a element 찾기
print(soup.find('a', text='프리드로우-제388화 태준 그룹 (3)'))

# 부모,자식,형제
# 인기급상승 만화 순위 찾기
rank1 = soup.find('li', attrs={'class': 'rank01'})
print(rank1.parent)  # 부모 출력
print(rank1.a)  # 자식 출력
print(rank1.next_sibling)   # 형제 출력
print(rank1.next_sibling.next_sibling)  # 안나오면 한번 더

# 변수로 지정
rank2 = rank1.next_sibling.next_sibling
rank3 = rank2.next_sibling.next_sibling
print(rank3.a.get_text())
rank2 = rank3.previous_sibling.previous_sibling
print(rank2.a.get_text())

# next_sibling 2번 안쓰는 법
rank2 = rank1.find_next_sibling('li')
print(rank2.a.get_text())

# 형제 한번에 불러오기
print(rank1.find_next_siblings('li'))
