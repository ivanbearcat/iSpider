#coding:utf8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.common.exceptions import TimeoutException
import requests
import re
import os
from gevent import monkey; monkey.patch_socket()
import gevent


#保存图片的目录
img_dir = 'e:/gif'
url_list = []
gif_url_list = []

browser = webdriver.Chrome()
browser.get('http://tu.duowan.com/m/bxgif')

#获取所有的img元素
li = browser.find_elements_by_xpath('//ul//em/a')

li_old_sum = 0
li_new_sum = 1

def get_gif(url):
    request = requests.get(url)

while li_old_sum != li_new_sum:
    # for i in li:
    #     print i.get_attribute('src')
    li_old_sum = len(li)

    #滚动条拉到底
    browser.execute_script("window.scrollBy(0,3000)","")
    sleep(1)

    #获取所有的img元素
    li = browser.find_elements_by_xpath('//ul/li/em/a')
    li_new_sum = len(li)

#处理掉失效的url
for element in li:
    url = element.get_attribute('href')
    num = re.search(r'\d+',url).group()
    if int(num) > 93181:
        # print element.get_attribute('href')
        url_list.append(url)

browser.close()

#获取每个页面上的所有gif链接
for gif_url in url_list:
    count = 1
    while 1:
        try:
            browser1 = webdriver.Chrome()
            print '{0}#p{1}'.format(gif_url,count)
            browser1.get('{0}#p{1}'.format(gif_url,count))
            #智能等待
            WebDriverWait(browser1,10).until(lambda x:os.path.basename(x.find_element_by_xpath('//img[@alt]').get_attribute('src')) != 'qd.gif')
            url = browser1.find_element_by_xpath('//img[@alt]').get_attribute('src')
            print url
            gif_url_list.append(url)
            count += 1
            browser1.close()
        except TimeoutException,e:
            browser1.close()
            break

print gif_url_list


