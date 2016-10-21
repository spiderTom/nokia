import requests
import re

cs_url = 'https://github.com/session'
cs_user = 'xiaomingatu@163.com'
cs_psw = 'AAAsss111'
http_proxy = {"https": 'https://10.144.1.10:8080'}
my_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'
}
sss = requests.Session()
r = sss.get(cs_url, headers=my_headers, proxies=http_proxy)
print r.status_code, r.url
reg = r'<input name="authenticity_token" type="hidden" value="(.*)" />'
pattern = re.compile(reg)
result = pattern.findall(r.content)
token = result[0]
print token
my_data = {
    'commit': 'Sign in',
    'utf8': '%E2%9C%93',
    'authenticity_token': token,
    'login': cs_user,
    'password': cs_psw
}
#error 404
r = sss.post(cs_url, headers=my_headers, data=my_data, proxies=http_proxy)

print r.url, r.status_code, r.history

