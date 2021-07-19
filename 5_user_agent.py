import requests
headers= {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
# headers: 나의 user-Agent정보(크롬)

url='http://nadocoding.tistory.com'
res = requests.get(url, headers=headers)
res.raise_for_status()

with open('nadocoding.html','w', encoding='utf8') as f:
    f.write(res.text)