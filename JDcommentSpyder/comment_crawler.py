# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 22:44:01 2021

@author: duoge
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import re
import time


def parse_page(html, data):

    soup = BeautifulSoup(html, features="html.parser")
    comment_items = soup.find_all("div", attrs={'class': 'comment-item'})
    for comment_item in comment_items:
        order_info = comment_item.find("div", attrs={'class': 'order-info'})
        spans = order_info.find_all("span")
        datetime = spans[-1].text  # 评论时间
        color = spans[0].text  # 颜色
        type = spans[1].text  # 款式
        comment_star = comment_item.find('div', attrs={'class': re.compile("comment-star star[0-9]")})
        stars = comment_star.attrs['class'][-1]  # 评分
        comment = comment_item.find('p', attrs={'class': 'comment-con'}).text
        data.append([datetime, stars, color, type, comment])




# 浏览器设置
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
user_agent = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) " +
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36"
    )
chrome_options.add_argument('user-agent=%s' % user_agent)
chrome_options.add_argument('blink-settings=imagesEnabled=false')


browser = webdriver.Chrome(executable_path="chromedriver.exe", options=chrome_options)
browser.implicitly_wait(10)


# 获取网页
browser.get("https://item.jd.com/100014418816.html#comment", )
page_num = 177
data = []
for i in range(page_num):
    page = browser.page_source
    parse_page(page, data)
    # browser.find_element_by_class_name("ui-pager-next").click()  # 翻页
    element = browser.find_element_by_class_name("ui-pager-next")
    browser.execute_script("arguments[0].click();", element)
    print("第{}页已爬取完成".format(i+1))


# 导出文件
colnames = ['datetime', 'stars', 'color', 'type', 'comment']
data = pd.DataFrame(data, columns=colnames)
data.to_csv("comment.csv")