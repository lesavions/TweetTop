# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:36:20 2022


@author: marti
"""

#TO OBTAIN A LIST OF TOP 100 POSTS BASED ON YOUR CHOSEN SEACH TERM

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome('C:/Users/marti/chromedriver.exe')

#ENTER SEARCHTERM BELOW
searchTerm = 'Joe Duffy'


driver.get('https://twitter.com/explore')
time.sleep(2)

button = driver.find_element('xpath','//*[@id="layers"]/div/div[2]/div/div/div/div[2]/div[1]').click()
time.sleep(2)

link_click = driver.find_element('xpath','//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[2]/nav/div/div[2]/div/div[2]/a/div').click()
time.sleep(2)

search = driver.find_element('xpath',
'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input')
time.sleep(2)
search.send_keys(searchTerm)
search.send_keys(Keys.ENTER)

soup = BeautifulSoup(driver.page_source, 'lxml')

postings = soup.find_all('div', class_= 'css-1dbjc4n r-j5o65s r-qklmqi r-1adg3ll r-1ny4l3l')
tweets = []
while True:
    for post in postings:
        tweets.append(post.text)
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    postings = soup.find_all('div', class_= 'css-1dbjc4n r-j5o65s r-qklmqi r-1adg3ll r-1ny4l3l')
    tweets2 = list(set(tweets))
    if len(tweets2) > 100:
        break


         