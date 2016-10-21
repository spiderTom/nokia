#coding:utf-8
import string, urllib2
import requests
import cookielib


def spider(url,begin_page,end_page):
    for i in range(begin_page, end_page+1):
        sName = string.zfill(i,5) + '.html'
        print 'web spider......' + str(i)
        f = open(sName,'w+')
        number = i * 20
        print url + str(number)
        m = urllib2.urlopen(url + str(number)).read()
        f.write(m)
        f.close()

def saveCookie(file):
    #设置保存cookie的文件，同级目录下的cookie.txt
    filename = file + '.txt'
    #声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
    cookie = cookielib.MozillaCookieJar(filename)
    #利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
    handler = urllib2.HTTPCookieProcessor(cookie)
    #通过handler来构建opener
    opener = urllib2.build_opener(handler)
    #创建一个请求，原理同urllib2的urlopen
    response = opener.open(login_url)
    #保存cookie到文件
    cookie.save(ignore_discard=True, ignore_expires=True)


def setproxy(proxy):
    proxy_handler = urllib2.ProxyHandler({"http": 'http://10.144.1.10:8080'})
    null_proxy_handler = urllib2.ProxyHandler({})

    if proxy:
        opener = urllib2.build_opener(proxy_handler)
    else:
        opener = urllib2.build_opener(null_proxy_handler)
    urllib2.install_opener(opener)


def testCookie(login_url):
    #创建MozillaCookieJar实例对象
    cookie = cookielib.MozillaCookieJar()
    #从文件中读取cookie内容到变量
    cookie.load('nokia.txt', ignore_discard=True, ignore_expires=True)
    #创建请求的request
    req = urllib2.Request(login_url)
    #利用urllib2的build_opener方法创建一个opener
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    response = opener.open(req)
    #print response.read()
    sName = 'test.html'
    print 'web spider test for nokia......'
    f = open(sName,'w+')
    m = response.read()
    f.write(m)
    f.close()


def testLogin():
    url = "http://www.nsntradeunion.com.cn/bbs/mvnforum/login"
    # Add username and password.
    MemberName = "61463034"
    MemberMatkhau = "123456"
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, url, MemberName, MemberMatkhau)
    handler = urllib2.HTTPDigestAuthHandler(password_mgr)
    opener = urllib2.build_opener(handler)
    #use the opener to fetch a URL
    urllib2.install_opener(opener)
    response = urllib2.urlopen(url)
    file = open("a.html", "w")
    file.write(response.read())
    file.close()

enable_proxy = False
setproxy(enable_proxy)
nokia = 'http://www.nsntradeunion.com.cn/bbs/mvnforum/listrecentthreads?sort=ThreadCreationDate&order=DESC&offset='
login_url = 'http://www.nsntradeunion.com.cn/bbs/mvnforum/login'

testLogin()


#s = requests.Session()  # 可以在多次访问中保留cookie
#s.post(login_url, {'username':61463034, 'password': 123456,})  # POST帐号和密码，设置headers
#r = s.get(login_url)  # 已经是登录状态了

#saveCookie('nokia')
#testCookie(login_url)
#spider(nokia,1,2)
#spider2(qiubaiurl,1,14)