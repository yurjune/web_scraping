from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window()
url = 'https://flight.naver.com/flights/'
browser.get(url)

# 왕복 이번달 27~28
browser.find_element_by_link_text('가는날 선택').click()
browser.find_elements_by_link_text('27')[0].click()  # [0]이번달 [1]다음달
browser.find_elements_by_link_text('28')[0].click()

# 추천리스트에서 제주도 선택 xpath이용
browser.find_element_by_xpath('//*[@id="recommendationList"]/ul/li[1]').click()
browser.find_element_by_link_text('항공권 검색').click()

# 10초 대기중 로딩다되면 들어가기
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="content"]/div[2]/div/div[4]/ul/li[1]')))
    print(elem.text)
finally:
    browser.quit()