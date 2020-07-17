



from background_task import background
import time
@background()   
def task_hello(schedule = 2, repeat = 5):   # per second : 2초 후에 시작하고, 5초 마다 반복
    time_tuple = time.localtime()
    time_str = time.strftime('%m/%d/%Y, %H:%M:%S', time_tuple)
    print('this is test task -> Hello, World!', time_str)

import requests;
from bs4 import BeautifulSoup;
import sqlite3

res = requests.get('http://media.daum.net/economic/')

@background()
def task_crawling_daum(schedule = 5, repeat = 60*3):
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