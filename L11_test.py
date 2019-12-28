from gevent import monkey

monkey.patch_all()

import gevent, requests, csv
from bs4 import BeautifulSoup
url='http://www.boohee.com/food/'

res_tvs=requests.get(url)
print(res_tvs)
bs_tvs=BeautifulSoup(res_tvs.text,'html.parser')

div_list=bs_tvs.find('li',class_='col-md-4 col-sm-4 col-xs-12 item')
print(div_list.text)

#item_list=div_list.find_all('li')
#for i in item_list:
    #print(i.find('div',class_='number').text)
