import requests

url='https://wordpress-edu-3autumn.localprod.forc.work/wp-login.php'

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}

data={
    'log': 'spiderman',  #写入账户
    'pwd': 'crawler334566',  #写入密码
    'wp-submit': '登录',
    'redirect_to': 'https://wordpress-edu-3autumn.localprod.forc.work/wp-admin/',
    'testcookie': '1'
}

login_in=requests.post(url,data=data,headers=headers)
cookies = login_in.cookies

url_1= 'https://wordpress-edu-3autumn.localprod.forc.work/wp-comments-post.php'
data_1={
    'comment': input('请输入你想要发表的评论：'),
    'submit': '发表评论',
    'comment_post_ID': '13',
    'comment_parent': '0'
}
comment=requests.post(url_1,headers=headers,data=data_1)
print(comment.status_code)
