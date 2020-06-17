#https://stu.goe.go.kr/edusys.jsp?page=sts_m42320
import urllib
from urllib.request import Request
import bs4
from datetime import datetime # 날짜 구하는거


def lunchtext():
    hdr = {'User-Agent': 'Mozilla/5.0'}
    url = 'http://www.daeho.ms.kr/wah/main/schoolmeal/calendar.htm?menuCode=179'
    print(url)
    print(datetime.today().day)  # 오늘 Day 값 가져옴
    today = datetime.today().day # 오늘날짜 구함
    req = Request(url, headers=hdr)
    html = urllib.request.urlopen(req)
    bsObj = bs4.BeautifulSoup(html, "html.parser") # 학교 홈피 크롤링
    lunch1 = bsObj.find('div', {'class': 'Cont_Cont'}) # 학교 소스에서 검색
    lunch2 = lunch1.find('tbody') # <div class="Cont_Cont" id="Conten"> 에서 "tbody"검색
    lunch3 = lunch2.find_all('td') # 위에서랑 똑같음
    lunch4 = lunch3[today+1] # 날자를 구함
    lunch5 = lunch4.text # text만 입력
    lunchlen = len(lunch5) # 문자길이를 구함
    itLunchlen = int(lunchlen) # int값으로 바꿈
    if itLunchlen<=2:
        lunch5 = "없음"
    else:
        lunch5_1 = lunch4.find('a')
        lunch5 = lunch5_1.text.strip()
    return lunch5

def lunchtextD1():
    hdr = {'User-Agent': 'Mozilla/5.0'}
    url = 'http://www.daeho.ms.kr/wah/main/schoolmeal/calendar.htm?menuCode=179'
    print(url)
    print(datetime.today().day)  # 오늘 Day 값 가져옴
    today = datetime.today().day # 오늘날짜 구함
    req = Request(url, headers=hdr)
    html = urllib.request.urlopen(req)
    bsObj = bs4.BeautifulSoup(html, "html.parser")
    lunch1 = bsObj.find('div', {'class': 'Cont_Cont'})
    lunch2 = lunch1.find('tbody')
    lunch3 = lunch2.find_all('td')
    lunch4 = lunch3[today+2]
    lunch5 = lunch4.text
    lunchlen = len(lunch5)
    itLunchlen = int(lunchlen)
    if itLunchlen<=2:
        lunch5 = "없음"
    else:
        lunch5_1 = lunch4.find('a')
        lunch5 = lunch5_1.text.strip()
    return lunch5

def lunchtextD2():
    hdr = {'User-Agent': 'Mozilla/5.0'}
    url = 'http://www.daeho.ms.kr/wah/main/schoolmeal/calendar.htm?menuCode=179'
    print(url)
    print(datetime.today().day)  # 오늘 Day 값 가져옴
    today = datetime.today().day #오늘 날짜 구함
    req = Request(url, headers=hdr)
    html = urllib.request.urlopen(req)
    bsObj = bs4.BeautifulSoup(html, "html.parser")
    lunch1 = bsObj.find('div', {'class': 'Cont_Cont'})
    lunch2 = lunch1.find('tbody')
    lunch3 = lunch2.find_all('td')
    lunch4 = lunch3[today+3]
    lunch5 = lunch4.text
    lunchlen = len(lunch5)
    itLunchlen = int(lunchlen)
    if itLunchlen<=2:
        lunch5 = "없음"
    else:
        lunch5_1 = lunch4.find('a')
        lunch5 = lunch5_1.text.strip()
    return lunch5

print(lunchtext())
print(lunchtextD1())
print(lunchtextD2())