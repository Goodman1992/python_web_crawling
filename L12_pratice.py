from gevent import monkey
monkey.patch_all()
#让程序变成异步模式。
import gevent,requests, bs4, csv
from bs4 import BeautifulSoup
from gevent.queue import Queue


def crawler():
    temp_ref_list=[]
    url = work.get_nowait()
    url = url+'?page='
    for i in range(1,4):
        r = requests.get(url+str(i))
        r = BeautifulSoup(r.text,'html.parser')
        temp_list=r.find_all('div',class_='text-box pull-left')
        for i in temp_list:
            temp_url=i.find('a',href=True).get('href')
            temp_ref_list.append(temp_url)
    ref_list.append(temp_ref_list)


ref_list=[]

url = 'http://www.boohee.com/food/'

base_res = requests.get(url)
base_res = BeautifulSoup(base_res.text,'html.parser')

categary_list = base_res.find_all('li',class_='col-md-4 col-sm-4 col-xs-12 item')

sub_categary_list=[]
for i in categary_list:
    sub_categary_list.append(i.find('a',href=True).get('href'))

work = Queue()
url_head = 'http://www.boohee.com'
work.put_nowait(url_head+sub_categary_list[0])
work.put_nowait(url_head+sub_categary_list[1])
work.put_nowait(url_head+sub_categary_list[2])
work.put_nowait(url_head+sub_categary_list[len(sub_categary_list)-1])

tasks_list=[]
for i in range(4):
    task=gevent.spawn(crawler)
    tasks_list.append(task)

gevent.joinall(tasks_list)
print(ref_list)
