import string
import requests


cs_url = 'https://www.excelityglobal.cn/embrace/servlet/login'
cs_url_control = 'https://www.excelityglobal.cn/embrace/servlet/controller'
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

my_header_first = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    #'Cookie': 'JSESSIONID=23DE6DDC9FC7B2CA2132A756F0699E0C.app2',
    'Host': 'www.excelityglobal.cn',
    'Origin': 'https://www.excelityglobal.cn',
    'Referer': 'https://www.excelityglobal.cn/embrace/servlet/controller?module=Payroll&screen=PayslipSelfServiceCN&action=Query',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}

my_data = {
    'txtLoginId': '61463034',
    'txtPassword': 'AAAsss11',
    'txtCorporation': 'NSN',
    'txtVerificationCode': '',
    'sessionid': '',
    'txtFlag': '1',
    'usrCorporation': 'nsn',
    'usrLoginId': '61463034',
    'usrPassword': 'AAAsss11',
    'verificationCode': ''
}
my_data_first = {
    'module': 'Payroll',
    'screen': 'PayslipSelfServiceCN',
    'action': 'Show',
    'txtStartDate':'2016/1',
    'txtEndDate':''
}

sessionId = '764B20106BED0025FAF788B03B51613B'
sessionId += '.app2'


my_data['txtLoginId'] = sessionId + my_data['usrLoginId']
my_data['txtPassword'] = sessionId + my_data['usrPassword']
my_data['txtCorporation'] = sessionId + my_data['usrCorporation'].upper()
my_data['txtVerificationCode'] = sessionId
my_data['sessionid'] = sessionId

sss = requests.Session()

print '111111111111111'
r = sss.post(cs_url, headers=my_headers, proxies=http_proxy, data=my_data)
print r.url, r.status_code
r = sss.post(cs_url_control, headers=my_header_first, proxies=http_proxy, data=my_data_first)
print r.url, r.status_code
if r.status_code == 200:
    f = open('001.html', 'w+')
    f.write(r.content)
    f.close()
