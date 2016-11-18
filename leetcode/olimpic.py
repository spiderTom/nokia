import requests
import re
import string

login_headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Content-Length':'103',
    'Content-Type':'application/x-www-form-urlencoded',
    'Cookie':'__atuvc=1%7C38; _gat=1; csrftoken=dVfpRkdbQB2KTdwguyRjLRUgBOWro49H; _ga=GA1.2.2097154511.1474444144',
    'Host':'leetcode.com',
    'Origin':'https://leetcode.com',
    'Referer':'https://leetcode.com/accounts/login/',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
forward_headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Cookie':'csrftoken=gv20OSvQNs5JTtSrV0CMhGUsOZ8co79w; _ga=GA1.2.2097154511.1474444144; _gat=1; __atuvc=4%7C38; __atuvs=57e28fed5bafbc2e002',
    'Host':'leetcode.com',
    'Referer':'https://leetcode.com/problems/two-sum/',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
my_data = {
    'csrfmiddlewaretoken':'dVfpRkdbQB2KTdwguyRjLRUgBOWro49H',
    'login':'j9wu@nokia.com',
    'password':'dayang',
    'remember':'on'
}
http_proxy = {"https": 'https://10.144.1.10:8080'}
login_url = 'https://leetcode.com/accounts/login/'
algorithms_url = 'https://leetcode.com/problemset/algorithms/'

sss = requests.Session()
r = sss.post(login_url, headers=login_headers, data=my_data, proxies=http_proxy)
print r.url, r.status_code, r.history
#f = open('olypic.html','w+')
#f.write(r.content)
#f.close()
answer = 'https://leetcode.com/articles/add-two-numbers/'
r = sss.get(answer, headers=forward_headers, proxies=http_proxy)
print r.url, r.status_code, r.history
f = open('add-tow-number.html','w+')
f.write(r.content)
f.close()