from selenium import webdriver

# options 설정
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument('window-size=1920x1080')

# 유저에이전트가 HeadlessChrome이 아니라 Chrome으로 정상적으로 나오게 하는 방법
# 이거 안하면 HeadlessChrome으로 인식
# user-agent와 = 사이 띄면 출력안됌
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36')

browser = webdriver.Chrome(options=options)
browser.maximize_window()
url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent'
browser.get(url)

# 유저에이전트 출력
# 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
detected_value = browser.find_element_by_id('detected_value')
print(detected_value.text)
browser.quit()