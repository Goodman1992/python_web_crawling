from gevent import monkey
monkey.patch_all()
import gevent,requests, bs4, csv
from gevent.queue import Queue

work = Queue()
food_list=[]
#前3个常见食物分类的前3页的食物记录的网址：
url_1 = 'http://www.boohee.com/food/group/{type}?page={page}'
for x in range(1, 4):
    for y in range(1, 4):
        real_url = url_1.format(type=x, page=y)
        work.put_nowait(real_url)

#第11个常见食物分类的前3页的食物记录的网址：
url_2 = 'http://www.boohee.com/food/view_menu?page={page}'
for x in range(1,4):
    real_url = url_2.format(page=x)
    work.put_nowait(real_url)

#请写出crawler函数和启动协程的代码：
def crawler():
    headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    while not work.empty():
        url = work.get_nowait()
        res = requests.get(url, headers=headers)
        bs_res = bs4.BeautifulSoup(res.text, 'html.parser')
        foods = bs_res.find_all('li', class_='item clearfix')
        temp_food = []

        for food in foods:
            food_name = food.find_all('a')[1]['title']
            food_url = 'http://www.boohee.com' + food.find_all('a')[1]['href']
            food_calorie = food.find('p').text
            temp_food.append([food_name,food_url,food_calorie])

        food_list.append(temp_food)

tasks_list=[]
for i in range(4):
    task=gevent.spawn(crawler)
    tasks_list.append(task)

gevent.joinall(tasks_list)
print(food_list)
