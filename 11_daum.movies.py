import requests
from bs4 import BeautifulSoup
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}

# 다음 영화 이미지 다운로드: 15~19년 top5
for year in range(2015, 2020):
    url = 'https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR'.format(year)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    images = soup.find_all('img', attrs={'class': 'thumb_img'})
    for idx, image in enumerate(images):
        # print(image['src'])
        image_url = image['src']
        if image_url.startswith('//'):
            image_url = 'https:'+image_url
        # print(image_url)

        # 이미지 파일 저장
        image_res = requests.get(image_url)
        image_res.raise_for_status()
        with open(f"movie_{year}_{idx+1}.jpg", "wb") as f:
            f.write(image_res.content)
        # 1-5위만
        if idx >= 4:
            break
