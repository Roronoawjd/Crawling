from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import pyperclip
from selenium.webdriver.common.keys import Keys
import time

# 구글 크롬 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# 불필요한 오류 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])

# 웹 페이지 해당 주소로 이동
driver.implicitly_wait(5)       # 웹 페이지가 로딩 될때까지 5초는 기다림
driver.maximize_window()        # 화면 최대화
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")

user_id = 'id'
user_pw = 'pw'

# 아이디 입력 창
id = driver.find_element(By.CSS_SELECTOR,'#id')
id.click()
pyperclip.copy(user_id)
id.send_keys(Keys.CONTROL,'V')
time.sleep(1)

# 비밀번호 입력 창
pw = driver.find_element(By.CSS_SELECTOR,'#pw')
pw.click()
pyperclip.copy(user_pw)
pw.send_keys(Keys.CONTROL,'V')
time.sleep(1)

button = driver.find_element(By.CSS_SELECTOR,'#log\.login')
button.click()