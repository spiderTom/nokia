import requests
import re
import string

class sub_forum:
    def __init__(self):
        self.sub_form_topic = []
        self.name = ''
        self.url = ''
        self.page = 0

class forum_data:
    def __init__(self):
        self.index_url = ''
        self.login_url = ''
        self.second_url = ''
        self.third_url = ''
        self.clubList = []
        self.clubIndex = []
        self.subForum = []


newtopic = 'http://www.nsntradeunion.com.cn/bbs/mvnforum/listrecentthreads?offset='
forum_data.index_url = 'http://www.nsntradeunion.com.cn/bbs/mvnforum/index'
forum_data.login_url = 'http://www.nsntradeunion.com.cn/bbs/mvnforum/login'
forum_data.second_url = 'http://www.nsntradeunion.com.cn/bbs/mvnforum/listthreads?forum='
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


#login
sss = requests.Session()
r = sss.post(forum_data.login_url, headers=login_headers, data=my_data, proxies=http_proxy)
print r.url, r.status_code, r.history

#get index page and write to index.html
r = sss.get(forum_data.index_url, headers=forward_header, proxies=http_proxy)
print r.url, r.status_code, r.history
f = open('index.html','w+')
f.write(r.content)
f.close()

#pattern = r'a href="listthreads\?forum=\d+" class="messageTopic">\D+</a><br/>'
pattern = r'a href="listthreads\?forum=\d+'
forum_data.clubList = re.findall(pattern, r.content)
#print secondIndex
forum_data.clubIndex = []
#get secondIndex number
for club in forum_data.clubList:
    club = club[club.rfind('=') + 1:]
    if club not in forum_data.clubIndex:
        forum_data.clubIndex.append(club)
    #print item

forum_data.clubIndex.sort()

#check one of the sub forum
for number in forum_data.clubIndex:
    sName = number + '.html'
    url = forum_data.second_url + number
    print 'web spider......' + number
    r = sss.get(url, headers=forward_header, proxies=http_proxy)

    pattern = r'"viewthread\?thread=\d+'
    forum_data.clubList = re.findall(pattern, r.content)
    #forum_data.subForum
    #f = open(sName, 'w+')
    #f.write(r.content)
    #f.close()
    #get the third topic address
    #"viewthread?thread=

