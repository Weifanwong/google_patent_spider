# -*- coding: utf-8 -*-
import scrapy
import io
import sys
import requests
import xlrd
from xlwt import *
from openpyxl import Workbook as wb
import os
import re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

def read_company():
    fileName0 = './firm_list.xlsx'
    bk=xlrd.open_workbook(fileName0)
    shxrange=range(bk.nsheets)
    try:
        sh=bk.sheet_by_name("Sheet1")
    except:
        print ("代码出错")
    # ncols=sh.ncols #获取列数
    # nrows=sh.nrows #获取列数

    book = Workbook(encoding='utf-8')
    # sheet = book.add_sheet('Sheet1') #创建一个sheet
    UPC = []
    tmp1 = sh.col_values(1)[1:]  #company
    tmp2 = sh.col_values(0)[1:]  #id
    # tmp3 = sh.col_values(2)[1:]  #IRI
    return tmp1

def start_requests():
    base_url = 'https://patents.google.com/xhr/query?'
    company = 'TETRAPHASE PHARMACEUTICALS INC'
    patent_name = 'url=assignee=' + company + '&oq=' + company + '&exp=&download=true'
    param = {}
    suburl = base_url + patent_name
    print(suburl)
    file_name = 'test.csv'
    r = requests.get(suburl)
    fo = open(file_name,'wb')                         # 注意要用'wb',b表示二进制，不要用'w'
    fo.write(r.content)                               # r.content -> requests中的二进制响应内容：以字节的方式访问请求响应体，对于非文本请求
    fo.close()
      
# start_requests()
read_company()

base_url = 'https://patents.google.com/xhr/query?'
url_list = []
company_list = read_company()
for company in company_list:
    patent_name = 'url=assignee=' + company + '&oq=' + company + '&exp=&download=true'
    url = base_url + patent_name
    filename = './company_patent/' + company + '.csv'
    r = requests.get(url)
    fo = open(filename,'wb')                         # 注意要用'wb',b表示二进制，不要用'w'
    fo.write(r.content)                               # r.content -> requests中的二进制响应内容：以字节的方式访问请求响应体，对于非文本请求
    fo.close() 

