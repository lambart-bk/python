#!/usr/bin/env python
#coding:utf8
import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox()
driver.get('https://passport.ustc.edu.cn/login?service=http%3A%2F%2Fyjs.ustc.edu.cn%2Fdefault.asp')
driver.implicitly_wait(3)
print driver.title
userid= driver.find_element_by_id("login")
userpwd=driver.find_element_by_name('password')
#check=driver.find_element_by_name('txt_check')
#username.clear()
userid.send_keys('***')
userpwd.send_keys('***')
#check.send_keys('2564')
loginBtn=driver.find_element_by_id("button")
#loginBtn=driver.find_element_by_xpath("html/body/table[2]/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr[4]/td/input")
loginBtn.click()
time.sleep(2)

#assert 'No results found.' not in driver.page_source
frame = driver.find_element_by_id("top-frame")
driver.switch_to_frame(frame)
menu=driver.find_element_by_xpath('html/body/table[2]/tbody/tr/td[2]/table/tbody/tr[1]/td[1]/table/tbody/tr/td[9]/span/a')
menu.click()
time.sleep(2)

driver.switch_to.default_content()
frame = driver.find_element_by_id("menu-frame")
driver.switch_to_frame(frame)
menu=driver.find_element_by_xpath('//*[@id="mm_2"]')
menu.click()
time.sleep(2)

driver.switch_to_window(driver.window_handles[1])
print driver.title
frame = driver.find_element_by_id('mainFrame')
driver.switch_to_frame(frame)
frame = driver.find_element_by_id("I2")
driver.switch_to_frame(frame)
frame = driver.find_element_by_id("xkFrame")
driver.switch_to_frame(frame)
box=driver.find_element_by_xpath('//*[@id="kczwtxt"]')
box.send_keys(u'计算机视觉')
btn1=driver.find_element_by_name("button2")
btn1.click()
time.sleep(2)

while True:
	btn1=driver.find_element_by_xpath("html/body/div/form/div[3]/table/tbody/tr[2]/td[2]/a/img")
	btn1.click()
	time.sleep(0.5)

	al = driver.switch_to_alert()
	time.sleep(0.5)
	if(al.text!=u'很抱歉，课堂已满员!'):
		al.accept()
		break
	al.accept()
	time.sleep(2)


time.sleep(15)
driver.close()

