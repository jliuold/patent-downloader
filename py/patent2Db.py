# coding:utf-8

import re
import cookielib
import urllib
import urllib2
import optparse
from bs4 import BeautifulSoup as bs
import sys
import MySQLdb

cj = cookielib.CookieJar();
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)

'''
获得搜索词的url编码
搜索方式为专利之星的默认搜索方式
'''
def keywordPostData(keyword):
	strSearchQuery = "F YY ("+keyword+"/AB+"+keyword+"/CL+"+keyword+"/TI+"+keyword+"/IN+"+keyword+"/PA+"+keyword+"/AT+"+keyword+"/DZ)"
	strSearchQuery = urllib2.quote(strSearchQuery)
	postData = "{'strSearchQuery':'"+strSearchQuery+"', '_strSdbType':'CN','_sDoSrc':'0'}"
	print postData
	return postData

'''
得到网页代码中的特定数据
'''
def getVE():
	s = "getVE......"
	print s
	MainUrl = "http://www.patentstar.cn/"
	resp = urllib2.urlopen(MainUrl)
	html = resp.read()
	soup = bs(html)
	VIEWSTATE = soup.find(id="__VIEWSTATE").get('value')
	EVENTVALIDATION = soup.find(id='__EVENTVALIDATION').get('value')
	ve = {'V':VIEWSTATE,'E':EVENTVALIDATION}
	print ve
	return ve

'''
得到程序运行时的参数
python filename -u 专利之星用户名 -p 账户密码 -k 关键词
'''
def argsInfo():
	parser = optparse.OptionParser();
	parser.add_option("-u","--username",action="store",type="string",default='',dest="username",help="Your User Name")
	parser.add_option("-p","--password",action="store",type="string",default='',dest="password",help="Your Password")
	parser.add_option("-k","--keyword",action="store",type="string",default='',dest="keyword",help="Keyword you want to search")
	(options, args) = parser.parse_args()
	
	for i in dir(options):
		exec(i + " = options." +i)
	if (len(username)>0 and len(password)>0 and len(keyword)>0):
		return [username,password,keyword]
	else:
		sys.exit("no args info")

'''
登陆账户，需要指定[username,password]
'''
def login(userinfo):
	s = "login......"
	print s
	ve = getVE()
	postDict = {
		'TextBoxAccount':userinfo[0],
		'Password':userinfo[1],
		'__VIEWSTATE':ve['V'],
		'__EVENTVALIDATION':ve['E'],
		'ImageButtonLogin.x':"71",
		'ImageButtonLogin.y':"32"
	}
	print "login info:",postDict
	loginHeader = {
		'Host':"www.patentstar.cn",
		'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
		'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
		'Accept-Language':"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
		'Accept-Encoding':"gzip, deflate",
		'Referer':"http://www.patentstar.cn/frmLogin.aspx",
		'Content-Type':"application/x-www-form-urlencoded",
		'Connection':"keep-alive"
	}
	postData = urllib.urlencode(postDict)
	loginUrl = "http://www.patentstar.cn/frmLogin.aspx"
	req = urllib2.Request(loginUrl, postData, headers = loginHeader)
	resp = urllib2.urlopen(req).read()
	if "用户中心" in resp:
		print "login success"
		return True
	s = "login filed"
	print s
	return False

'''
关键字搜索，能够得到搜索关键字后返回的数目等信息，包括用户的搜索次数
'''
def search(keyword):
	searchHeader = {
		'Host':"www.patentstar.cn",
		'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
		'Accept':"application/json, text/javascript, */*; q=0.01",
		'Accept-Language':"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
		'Accept-Encoding':"gzip, deflate",
		'Content-Type':"application/json; charset=utf-8",
		'X-Requested-With':"XMLHttpRequest",
		'Connection':"keep-alive"
	}
	postData = keywordPostData(keyword)
	searchUrl = "http://www.patentstar.cn/my/SmartQuery.aspx/DoPatSearch"
	req = urllib2.Request(searchUrl, postData, headers = searchHeader)
	resp = urllib2.urlopen(req).read()
	print "Search results:",resp
	if "请求错误" in resp:
		return []
	dict = eval(resp)
	results = dict['d']
	return results #返回列表


'''
通过指定网站搜索信息的页码与登陆次数获得信息ID列表
'''
def getInfoList(NodeId, pageIndex):
	print "getList......",pageIndex
	Header = {
		'Host':"www.patentstar.cn",
		'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
		'Accept':"application/json, text/javascript, */*; q=0.01",
		'Accept-Language':"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
		'Accept-Encoding':"gzip, deflate",
		'Content-Type':"application/json; charset=utf-8",
		'X-Requested-With':"XMLHttpRequest",
		'Connection':"keep-alive",
		'Cache-Control':"max-age=0"
	}
	url = "http://www.patentstar.cn/comm/GetList.aspx/GetPageList"
	try:
		postData = "{'Type': 'CN', 'NodeId':'"+str(NodeId)+"', 'SourceType': 'FI', 'ItemCount':'1815', 'pageindex':'"+str(pageIndex)+"', 'rows':'50','Sort':'PD|DESC'}"
		req = urllib2.Request(url, postData, headers = Header)
		resp = urllib2.urlopen(req).read()
		return getInfoListByJson(resp)
	except:
		s = "get no info"
		print s
		return []

def getInfoListByJson(json):
	json.replace("\\","")
	dict = eval(json)
	infoList = eval(dict['d'])['rows']
	return infoList

def toDB(infoList):
	conn = MySQLdb.connect(
		host='127.0.0.1',
		port=3306,
		user='root',
		passwd='root',
		db="patent",
		charset="utf8"
	)
	cur = conn.cursor()
	for info in infoList:
		COLstr = ''
		Rowstr = ''
		for key in info.keys():
			COLstr=COLstr+' '+key+','
			Rowstr=Rowstr+" '"+info[key]+"',"
		sql = "insert into patentstar ("+COLstr[:-1]+") value ("+Rowstr[:-1]+")"
		#print sql
		print "create sql OK!"
		cur.execute(sql)
	cur.close()
	conn.commit()
	conn.close()
		

def allToDB(NodeId, NumOfRecord):
	pages = getNumOfPages(NumOfRecord)
	pageIndex = 1
	while pageIndex<=pages:
		infoList = getInfoList(NodeId, pageIndex)
		toDB(infoList)
		pageIndex = pageIndex+1


'''
获得搜索信息的页码数量，默认一页50条信息
'''
def getNumOfPages(NumOfRecord):
	n = int(NumOfRecord)
	if n%50 !=0:
		pages = n/50+1
	else:
		pages = n/50
	s = "search "+str(NumOfRecord)+"records "+str(pages)+" pages in total"
	print s
	return pages

def start(pageIndex=1):

	login(argsInfo()[0:2])
	searchResult = search("在线监测")
	allToDB(searchResult[1],searchResult[2])
	
start()
