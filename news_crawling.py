import requests
from bs4 import BeautifulSoup
import pyautogui

keyword = pyautogui.prompt("검색어를 입력하세요.")
lastpage = pyautogui.prompt("마지막 페이지 번호를 입력해 주세요.")

count = 1
page_number = 1
lastpage = int(lastpage)*10

for page in range(1,lastpage,10):
    response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_pge&query={keyword}&start={page}")
    html = response.text

    soup = BeautifulSoup(html,"html.parser")
    datas = soup.select(".news_tit")
    
    if len(datas) == 0:
        print("값을 입력하여 주세요!!")
        break
    else:
        print(f"{page_number} 페이지 입니다.================================")
        page_number += 1

    for data in datas:
        title = data.text
        url = data.attrs['href']
        print(f"{count}: {title}, {url}")
        count += 1
