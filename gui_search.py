import requests
from bs4 import BeautifulSoup
import pyautogui

input_value = pyautogui.prompt("검색어를 입력하세요. ")
response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={input_value}")
html = response.text

soup = BeautifulSoup(html,'html.parser')
links = soup.select(".news_tit") #리스트로 나옴

for link in links:
    title = link.text
    url = link.attrs['href']
    print(title, url)