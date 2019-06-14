#encoding=utf-8
import xlrd
from xlwt import *
import scrapy

# from openpyxl import Workbook
# from openpyxl import load_workbook
import os
import re
from openpyxl import Workbook as wb
import pandas as pd
from xlrd import open_workbook
from xlutils.copy import copy
import openpyxl
from openpyxl.styles import PatternFill, Alignment
import csv
import numpy as np
import random
import requests
import io
import sys
from lxml import etree
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码



def all_path(dirname):

	# print(item_dict)

	proxies = {"https": "https://127.0.0.1:1080", "http": "http://127.0.0.1:1080"}
	base_url = 'https://patents.google.com/xhr/query?'
	url_list = []
	# company_list = read_company()
	headers = {'user_agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
	'authority':'patents.google.com',
	'method':'GET',
	'scheme':'https',
	'accept':'*/*',
	'accept-encoding':'gzip, deflate, br',
	'accept-language':'en,en-US;q=0.9,zh-CN;q=0.8,zh;q=0.7',
	'cookie':'_ga=GA1.3.650546010.1557842690; 1P_JAR=2019-06-13-03; NID=185=HFLQWsc9gyTy7jWJiX-sZ242_kqMdEVUKf89m0r0R8jrCT1n2jN8cuSFmh6abb50bDB8u6qYhcF7KXWHgZy4TPj-zkheFl9g6kiLCqFrNEf6G_2hLhWzCfjwkz7EjLB8jrROilpayn5NIIKf0WLZsZCBemnNt88RdO4Tik_zYwg; _gid=GA1.3.814134454.1560407883; _gat=1'
	}
	user_agent_pool = ["Mozilla/5.0 (Macintosh; U; Mac OS X Mach-O; en-US; rv:2.0a) Gecko/20040614 Firefox/3.0.0 ",
	"Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.0.3) Gecko/2008092414 Firefox/3.0.3",
	"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.1) Gecko/20090624 Firefox/3.5",
	"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.14) Gecko/20110218 AlexaToolbar/alxf-2.0 Firefox/3.6.14",
	"Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"]
	ip_pool = ['114.230.69.170:9999','61.135.155.82:443']

	url_list = []#所有的文件
	title_list = ['Item','Report Number','Brand & Product Name','Distribution Countries','Country of Manufacture',	'Manufacturer',	'Distributor',	'Affiliate',	'Publication Date',	 'SKUs'	'Image'	'Innovation Name',	'Claims / Tags','PackType Name',	'Flavors & Fragrances',	'Shelving Name'	,'Ingredient Name',	'UPC Code',	'Package Material',	'Industry',	'Market',	'Category'	,'Nutrition'	,'Private Label Manuf.Code',	'Internet Address',	'Address',	'Product Price & Package Size',	'Description',	'Notes'	,'Segments']
	for maindir, subdir, file_name_list in os.walk(dirname):
		# print('G:\\数据\\test2\\'+maindir+'\\')
		record = []
		for filename in file_name_list:
			total_units = 0;
			total_dollars = 0;
			data = []
			apath = os.path.join(maindir, filename)#合并成一个完整路径
			df = pd.read_csv(apath,header=1,usecols=['result link'])
			df = np.array(df)
			df = df.tolist()
			for url in df:
				cur_url = url[0]
				ip = ip_pool[random.randrange(0,2)]
				headers['user_agent'] = user_agent_pool[random.randrange(0,len(user_agent_pool))]
				proxy_ip = 'http://'+ip
				proxies = {'http':proxy_ip}
				# print(url)
				r = requests.get(cur_url,headers=headers,proxies=proxies)
				text = r.text
				# print(text)
				html = etree.HTML(text)
				# print(html)
				title = html.xpath('body//div[@class="abstract"]/text()')
				print(title)
				print(cur_url)
				# print(title)
			print('********************')

		
 
	# return url_list

all_path('G:\\spider_study\\google_patent\\google_patent\\spiders\\company_patent')