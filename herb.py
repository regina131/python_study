import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.herbvillage.co.kr/pension/reserve.html?sdate=2016-08-20&date=2016-08&reserve_days=&reserve_form=list");
soup = BeautifulSoup(r.content, 'html.parser', from_encoding='utf-8')

details_info = soup.findAll('span', {'class':'ic_room_ok'})
print len(details_info)


