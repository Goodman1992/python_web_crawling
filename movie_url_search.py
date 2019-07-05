import requests, bs4

url='https://c.y.qq.com/soso/fcgi-bin/client_search_cp'

headers ={
    'origin' = 'https://y.qq.com',
    'referer' : 'https://y.qq.com/portal/search.html',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

params={
    'ct': '24'
    'qqmusic_ver': '1298'
    'remoteplace': 'txt.yqq.lyric'
    'searchid': '96687771239025412'
    'aggr': '0'
    'catZhida': '1'
    'lossless': '0'
    'sem': '1'
    't': '7'
    'p': '1'
    'n': '5'
    'w': '周杰伦'
    'g_tk': '5381'
    'loginUin': '0'
    'hostUin': '0'
    'format': 'json'
    'inCharset': 'utf8'
    'outCharset': 'utf-8'
    'notice': '0'
    'platform': 'yqq.json'
    'needNewCode': '0'}
