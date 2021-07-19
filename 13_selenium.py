# pip install selenium
# 버전에 맞는크롬 드라이버 설치
from selenium import webdriver
import time

# 브라우저 열기
browser = webdriver.Chrome()    # 인자: 경로, 같은폴더이면 생략
browser.get('https://naver.com')

# 로그인
elem = browser.find_element_by_class_name('link_login')
elem.click()
browser.find_element_by_id('id').send_keys('naver_id')
browser.find_element_by_id('pw').send_keys('password')
browser.find_element_by_id('log.login').click()
time.sleep(3)

# 새로입력
browser.find_element_by_id('id').clear()    # 이전데이터 지우기
browser.find_element_by_id('id').send_keys('my_id')

# html 저장
with open("naver_info", 'w', encoding="utf8") as f:
    f.write(browser.page_source)

# # 종료
# browser.quit()