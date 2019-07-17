import time
from selenium import  webdriver
from selenium.webdriver.chrome.options import Options

#initial driver in quite mode
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options = chrome_options)

#connect to login page
driver.get('https://wordpress-edu-3autumn.localprod.forc.work/wp-login.php')
print('connected to login page')
time.sleep(3)

#get login text fields
usr_login = driver.find_element_by_id('user_login')
usr_pass = driver.find_element_by_id('user_pass')
sub_btn = driver.find_element_by_id('wp-submit')

#send login details
usr_login.send_keys('xxx')
usr_pass.send_keys('xxx')
sub_btn.click()
print('loged in')
time.sleep(3)

#go to article 3
driver.find_elements_by_class_name('entry-title')[1].find_element_by_tag_name('a').click()
print('Directing to article 3')
time.sleep(3)

#submit comment
comment_box = driver.find_element_by_id('comment')
comment_box.send_keys('ZZZ....This is a comment sent by a Selenium bot ZZZ...')
comment_box_submit = driver.find_element_by_id('submit')
comment_box_submit.click()
print('Comment submited')

driver.close()
