

from background_task import background
import time

@background     # @백그라운드로 def를 진행시키기 위한 것  
def task_hello(schedule = 10, repeat = 60*1):   # (schedule, repeat) 는 필수 옵션이나, 큰 의미가 없이 백그라운드에 들어가는 파라미터 / schedule은 시작점, repeat는 몇번 계속 반복하느냐
    time_tuple = time.localtime()
    time_str = time.strftime('%m/%d/%Y, %H:%M:%S', time_tuple)
    print('this is test task -> Hello, World!', time_str)

import requests
from bs4 import BeautifulSoup
import sqlite3

res = requests.get('http://media.daum.net/economic/')

@background
def task_crawling_daum(schedule = 2, repeat = 60*3):
    if res.status_code == 200 :
        soup = BeautifulSoup(res.content, 'html.parser')
        links = soup.find_all('a', class_ = 'link_txt')
        with sqlite3.connect('db.sqlite3') as con:
            cur = con.cursor()
            title = str()
            link = str()
            for link in links :
                title = str.strip(link.get_text())
                link = link.get('href')
                cur.execute('INSERT INTO economic (title, link) VALUES (?,?)', (title, link))
            con.commit()
    time_tuple = time.localtime()
    time_str = time.strftime('%m/%d/%Y, %H:%M:%S', time_tuple)
    print('task_crawling_daum : ', type(links), len(links), time_str)