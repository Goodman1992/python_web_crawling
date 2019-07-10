import requests, bs4, csv

def trim_title(str):
    result=str.replace('\n','').replace('\xa0','').replace('[可播放]','')
    return result

csv_file=open('demo.csv','w',newline='',encoding='utf-8-sig')
writer=csv.writer(csv_file)
writer.writerow(['Rank','Title','Comment','Score','Url'])

all=[]

for i in range(10):
    url="https://movie.douban.com/top250?start=" + str(i*25) + '&filter='
    res=requests.get(url)
    bs=bs4.BeautifulSoup(res.text,"html.parser")
    bs=bs.find('ol','grid_view')
    source=bs.find_all('li')
    for item in source:
        temp=[]
        temp.append(trim_title(item.find('div','hd').text).strip())
        temp.append(item.find('span','inq').text)
        temp.append(item.find('span','rating_num').text)
        temp.append(item.find('div','hd').find('a')['href'])
        all.append(temp)

for i in range(len(all)):
    print("Rank: "+str(i+1))
    print("Title: "+all[i][0])
    print("Comment: "+all[i][1])
    print("Score: "+ all[i][2])
    print("Url: "+all[i][3])
    writer.writerow([str(i+1),all[i][0],all[i][1],all[i][2],all[i][3]])
