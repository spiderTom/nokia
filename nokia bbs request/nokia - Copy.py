import requests
import re
import string

class third_topic:
    name
    url

class second_topic:
    third_topic[]
    name
    url

class forum_data:
    index_url
    login_url
    second_url
    third_url


newtopic = 'http://www.nsntradeunion.com.cn/bbs/mvnforum/listrecentthreads?offset='
forum_data.index_url = 'http://www.nsntradeunion.com.cn/bbs/mvnforum/index'
login_url = 'http://www.nsntradeunion.com.cn/bbs/mvnforum/login'
second_url = 'http://www.nsntradeunion.com.cn/bbs/mvnforum/listthreads?forum='
cs_user = '61463034'
cs_psw = '123456'
http_proxy = {"http": 'http://10.144.1.10:8080'}

login_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Referer': 'http://www.nsntradeunion.com.cn/bbs/mvnforum/login'
}

forward_header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cookie': 'JSESSIONID=E19F1982A70283480FFD6DCC7A802E6D',
    'Host': 'www.nsntradeunion.com.cn',
    'Proxy-Connection': 'keep-alive',
    'Referer': 'http://www.nsntradeunion.com.cn/bbs/mvnforum/listrecentthreads?offset=20',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}

my_data = {
    'FromLoginPage': 'true',
    'md5pw': '4QrcOUm6Wau+VuBX8g+IPg==',
    'MemberName': cs_user,
    'MemberMatkhau': cs_psw,
    'AutoLoginExpire': '2592000'
}

sss = requests.Session()

#login
r = sss.post(login_url, headers=login_headers, data=my_data, proxies=http_proxy)
print r.url, r.status_code, r.history

#get index page and write to index.html
r = sss.get(index_url, headers=forward_header, proxies=http_proxy)
print r.url, r.status_code, r.history
f = open('index.html','w+')
f.write(r.content)
f.close()

#pattern = r'a href="listthreads\?forum=\d+" class="messageTopic">\D+</a><br/>'
pattern = r'a href="listthreads\?forum=\d+'
secondIndex = re.findall(pattern, r.content)
#print secondIndex
secondNumber = []
#get secondIndex number
for item in secondIndex:
    item = item[item.rfind('=') + 1:]
    if item not in secondNumber:
        secondNumber.append(item)
    #print item
print secondNumber
secondNumber.sort()
print secondNumber

#check one of the second index
for number in secondNumber:
    sName = number + '.html'
    url = second_url + number
    print 'web spider......' + number
    r = sss.get(url, headers=forward_header, proxies=http_proxy)
    f = open(sName, 'w+')
    f.write(r.content)
    f.close()
    #get the third topic address
    #"viewthread?thread=

#for i in range(1, 1):
    #sName = string.zfill(i,5) + '.txt'
    #print 'web spider......' + str(i)
    #f = open(sName,'w+')
    #number = i * 20
    #currentUrl = newtopic + str(number)
    #print newtopic + str(number)
    #r = sss.get(currentUrl, headers=forward_header, proxies=http_proxy)
    #print r.status_code, r.url, r.history
    #f.write(r.content)
    #f.close()
