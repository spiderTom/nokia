#coding:utf-8
import urllib2,urllib,cookielib

cookiejar= cookielib.CookieJar()
cookie=urllib2.HTTPCookieProcessor(cookiejar)
opener= urllib2.build_opener(cookie,urllib2.HTTPHandler())
urllib2.install_opener(opener)

personID=raw_input('输入员工号')
password=raw_input('输入密码')
#domain='nsntradeunion.com.cn'#域名
#domain='renren.com'
url='http://www.nsntradeunion.com.cn/bbs/mvnforum/login'

headers={
   'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0'
    }
data={
    'MemberName' : personID,
    'MemberMatkhau' : password
    #'domain': domain
    }

postdata = urllib.urlencode(data)
req=urllib2.Request(url,postdata,headers)
#print urllib2.urlopen(req).read()
file = open("b.html", "w")
file.write(urllib2.urlopen(req).read())
file.close()
