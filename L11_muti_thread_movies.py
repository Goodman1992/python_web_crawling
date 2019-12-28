from gevent import monkey

monkey.patch_all()

import gevent, requests, csv
from bs4 import BeautifulSoup

url_base='http://www.mtime.com/top/tv/top100/'

url_list=[]
url_list.append(url_base)
source=[]

for i in range(2,11):
    url_list.append(url_base+'index-'+i+'.html')

work=Queue()
for url in url_list:
    work.put_nowait(url)

#define crawler to do heavy lifting
def crawler():
    while not work.empty():
        url=work.get_nowait()
        res_tvs=requests.get(url)
        bs_tvs=BeautifulSoup(res_tvs,'html.parser')
        div_list=bs_tvs.find('div',id='BeautifulSoup')
        item_list=div_list.find_all('li')
        
        #TODO get infor from html file
