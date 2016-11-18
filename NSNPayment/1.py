import string
import requests


cs_url = 'https://www.excelityglobal.cn/embrace/servlet/login'
test = 'https://www.baidu.com'
http_proxy = {"https": 'https://10.144.1.10:8080'}
my_headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    #'Cookie': 'JSESSIONID=23DE6DDC9FC7B2CA2132A756F0699E0C.app2',
    'Host': 'www.excelityglobal.cn',
    'Origin': 'https://www.excelityglobal.cn',
    'Referer': 'https://www.excelityglobal.cn/embrace/servlet/login',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}

my_data = {
    'txtLoginId': '6FDD74B09AEAFF249B3493EE0BF3459E.app261463034',
    'txtPassword': '6FDD74B09AEAFF249B3493EE0BF3459E.app2AAAsss11',
    'txtCorporation': '6FDD74B09AEAFF249B3493EE0BF3459E.app2NSN',
    'txtVerificationCode': '6FDD74B09AEAFF249B3493EE0BF3459E.app2',
    'sessionid': '6FDD74B09AEAFF249B3493EE0BF3459E.app2',
    'txtFlag': '6FDD74B09AEAFF249B3493EE0BF3459E.app21',
    'usrCorporation': 'nsn',
    'usrLoginId': '61463034',
    'usrPassword': 'AAAsss11',
    'verificationCode': ''
}
sss = requests.Session()

print '111111111111111'
r = sss.post(cs_url, headers=my_headers, proxies=http_proxy, data=my_data)
print r.url, r.status_code
if r.status_code == 200:
    f = open('001.html','w+')
    f.write(r.content)
    f.close()


sessionId = str(sss.cookies)
begin = sessionId.find('=')
end = sessionId.find('.app2')
sessionId = sessionId[begin+1:end]
sessionId += '.app2'


my_data['txtLoginId'] = sessionId + my_data['usrLoginId']
my_data['txtPassword'] = sessionId + my_data['usrPassword']
my_data['txtCorporation'] = sessionId + my_data['usrCorporation'].upper()
my_data['txtVerificationCode'] = sessionId
my_data['sessionid'] = sessionId

#r = sss.post(cs_url, headers=my_headers, proxies=http_proxy, data=my_data)
topic_url = 'https://www.excelityglobal.cn/embrace/servlet/controller?module=Main&screen=MainPage&action=View&event=View&encodSel=zhCN'
sss.get(topic_url, headers=my_headers, proxies=http_proxy, timeout=0.002)
print r.url, r.status_code
if r.status_code == 200:
    f = open('002.html','w+')
    f.write(r.content)
    f.close()
print r.content