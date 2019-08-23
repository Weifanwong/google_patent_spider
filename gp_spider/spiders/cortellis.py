# -*- coding: utf-8 -*-
import scrapy
import sys
import io
import json
import requests
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码


def read_film_name():
    fileName = './file_list.xlsx'
    bk=xlrd.open_workbook(fileName)
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
    tmp1 = sh.col_values(0)[1:]  #id
    tmp2 = sh.col_values(1)[1:]  #com
    # tmp3 = sh.col_values(2)[1:]  #IRI
    return tmp2



company_list = read_film_name()
url = 'https://www.cortellis.com/intelligence/exportReport.do'
headers = {
		'Host': 'www.cortellis.com',
		'Connection': 'keep-alive',
		'Content-Length': '293',
		'Cache-Control': 'max-age=0',
		'Pragma': 'no-cache',
		'Origin': 'https://www.cortellis.com',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
		'Content-Type': 'application/x-www-form-urlencoded',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'If-Modified-Since': 'Mon, 26 Jul 1997 05:00:00 GMT',
		'X-1P-SESSION': '409b9d3c-53c8-4c41-b1ac-380beed5df2d',
		'Referer': 'https://www.cortellis.com/intelligence/report/ci/nextgendealall/172541',
		'Accept-Encoding': 'gzip, deflate, br',
		'Accept-Language': 'en,en-US;q=0.9,zh-CN;q=0.8,zh;q=0.7',
		'Cookie': 'dotmatics.elementalKey=SLsLWlMhrHnTjDerSrlG; spotfireTab=null; BrowserDetails=%7B%22aBrowsers%22%3A%5B%22opera%22%2C%22chrome%22%2C%22safari%22%2C%22firefox%22%2C%22msie%22%2C%22trident%22%2C%22ipad%22%5D%2C%22chrome%22%3Atrue%2C%22firefox%22%3Afalse%2C%22ipad%22%3Afalse%2C%22msie%22%3Afalse%2C%22name%22%3A%22chrome%22%2C%22opera%22%3Afalse%2C%22safari%22%3Afalse%2C%22trident%22%3Afalse%2C%22version%22%3A%2275.0.3770.100%22%2C%22mversion%22%3A75%7D; JSESSIONID=3-Tk-Tmg9DR_N0SALsFH6klIyVVMjyOel27L-ov_.prodeu-eu-west-1-frontend-2; currentStateUrl=%2Fintelligence%2Freport%2Fci%2Fnextgendealall%2F172541; __utmc=220075659; __utmz=220075659.1561796246.3.3.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); liveagent_oref=https://www.cortellis.com/intelligence/login.do; account=UNIV OF ADELAIDE; accountStatus={}; company=null; email=chengli.shu@adelaide.edu.au; jobArea=Business /Corporate Development; jobAreaOther=null; jobAreaSpecific=null; jobAreaSpecificOther=null; jobRole=Scientist/Dept member; jobRoleOther=null; subLevel=Cortellis Deal Intelligence+Cortellis - CI Custom+Cortellis - CI Professional; subLevelContent=Company Expanded+Cortellis News Export+CI Drug Expanded+Patent Essential+CI Matrix+Cortellis News+Cortellis Deal Expanded+Conferences+Broker Research Search Only Access+Events Transcript Limited+Cortellis Deal Export+CI Virtual Merger+Cortellis Company Export+Patent Spotfire Essential+Venture Capital Limited; username=null; liveagent_sid=5a7d76bf-98f7-4663-a407-1e4662e6f53c; liveagent_vc=2; liveagent_ptid=5a7d76bf-98f7-4663-a407-1e4662e6f53c; _pendo_visitorId.a2344573-fc41-40b6-4d5c-a5323ae55bce=10591295; savedFormData=stickynessFlag%3Dtrue%26searchResultsSelectAll%3Dtrue%26checkedEntityIds%3D%26unCheckedEntityIds%3D%26myRegionFilterStatus%3Dtrue; _pendo_meta.a2344573-fc41-40b6-4d5c-a5323ae55bce=3415940822; _sp_id.db9f=fef68385-c4a6-4c21-9672-c9b47cea367e.1560407035.5.1562036653.1561875763.d0fad3f3-4739-4c33-9827-565f3a48e02b; __utma=220075659.1675404293.1560407022.1562040468.1562043036.7; _sp_id.db9f=fef68385-c4a6-4c21-9672-c9b47cea367e.1560407035.8.1562047216.1562044938.9e48c98b-b4a7-4f8e-b218-6f494e400107; loginOwnerCookie=3-Tk-Tmg9DR_N0SALsFH6klIyVVMjyOel27L-ov_; _sp_ses.e4d1=*; AWSALB=q4QKcq8ETHxLJ8iWLxixO8KU6lt3puRd6XVqnXiLeooWqFBGgH8XrQnN3JrzaAes8EIoub15LzJDLViWpZx/4K8RsFHMeX8ya2l0c7apFx+FZ5iDmc/VldZwN9hU; _sp_id.e4d1=1cd2352af8e5894f.1561796463.3.1562049129.1562040455.c2f1e5e7-4dad-4c91-b802-c0bb9b29dbb0'
}
filename = 'test.pdf'
Form = {
		'id': '172541',
		'exportFormat': 'PDF',
		'isCustomized': 'false',
		'exportReportName': 'Purchase of Epi-Plus antibody product line for epigenetic research .pdf',
		'selectedFields': 'dealSnapShot,events,financial[dealFinanceSummary&principal&partner&],',
		'entityType': 'nextgendealall',
		'exportSubmit': '提交'
}
response = requests.post(url,data=Form,headers=headers)
fo = open(filename,'wb')                         # 注意要用'wb',b表示二进制，不要用'w'
fo.write(response.content)      
