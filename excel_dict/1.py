#!/usr/bin/env python
# -*- coding:utf8 -*-

from bs4 import BeautifulSoup
import requests
import time
import xlrd
import xlwt

path_to_excel='./1.xls' #excel文件路径

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}

def dict_to_excel(dic,table_title):
    oldxls=xlrd.open_workbook(path_to_excel) #先读后写
    oldsheet=oldxls.sheet_by_name('sheet1')
    newxls=xlwt.Workbook(encoding='utf-8')
    newsheet=newxls.add_sheet('sheet1')

    rows=oldsheet.nrows
    cols=oldsheet.ncols

    col_width=[600,600,128,1000,256,128] #设置列宽
    for col in range(cols):
        newsheet.col(col).width=col_width[col]*20

    for row in range(rows): #复制原来数据
        row_data=oldsheet.row_values(row)
        for col in range(cols):
            newsheet.write(row,col,label=row_data[col])
    row=rows
    for col in range(cols): #写新数据
        newsheet.write(row,col,label=dic.get(table_title[col]))
    newxls.save(path_to_excel)

def judgment_sex(class_name):
  if class_name == ['member_ico1']:
      return '女'
  else:
      return  '男'

def get_links(url):
    wb_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(wb_data.text,'lxml')
    links = soup.select('#page_list > ul > li > a')
    for link in links:
        href = link.get("href")
        get_info(href)

def get_info(url):
    wb_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(wb_data.text,'lxml')
    tittles = soup.select('div.pho_info > h4')
    addresses = soup.select('span.pr5')
    prices = soup.select('#pricePart > div.day_l > span')
    imgs = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > a > img')
    names = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')
    sexs = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > div')
    for tittle, address, price, img, name, sex in zip(tittles,addresses,prices,imgs,names,sexs):       
		data = {
            'tittle':tittle.get_text().strip(),
            'address':address.get_text().strip(),
            'price':price.get_text(),
            'img':img.get("src"),
            'name':name.get_text(),
            'sex':judgment_sex(sex.get("class"))
        }
		#print(data)	
		dict_to_excel(data,table_title) #写入excel，追加写
		
if __name__ == '__main__':
    urls = ['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(number) for number in range(1,14)]

    table_title=['tittle', 'address', 'price', 'img', 'name', 'sex'] #写入表头
    xls=xlwt.Workbook(encoding='utf-8')
    sheet=xls.add_sheet('sheet1')
    for col in range(len(table_title)):
        sheet.write(0,col,label=table_title[col])
    xls.save(path_to_excel)
    
    for single_url in urls:
        get_links(single_url)
        time.sleep(2)


