#coding:utf-8
import string
import requests

class topicName:
    def __init__(self):
        self.index = ''
        self.url = ''

f = open("all_topic.txt","r")
lines = f.readlines()
topicList = []
topicIndex = []
for line in lines:
    current = line.find('%')
    if -1 == current:
        line = line.strip()
        topicIndex.append(line)
        continue
    else:
        line = line[0:current - 5]
        line = line.strip()
        line = line.lower()
        line = line.replace(' - ', ' ')
        line = line.replace(' to ', ' ')
        line = line.replace(' from ', ' ')
        line = line.replace(' of ', ' ')
        line = line.replace(' ', '-')
        topicList.append(line)
        #topicList.append(topicName)

f = open('DSYBG002_ALL.txt', 'w+')
i = 0
for index in topicIndex:
    f.write(index + "   " + topicList[i])
    i += 1
    f.write("\n")
f.close()


cs_url = 'https://leetcode.com/articles/'
http_proxy = {"https": 'https://10.144.1.10:8080'}
my_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'
}
sss = requests.Session()

count = 0
todo = []
for topic in topicList:
    topic_url = cs_url + topic + '/'
    r = sss.get(topic_url, headers=my_headers, proxies=http_proxy)
    print r.url, r.status_code
    if r.status_code == 200:
        f = open(str(topicIndex[count]) + '  ' + topic + '.html', 'w+')
        f.write(r.content)
        f.close()
    else:
        todo.append(str(topicIndex[count]) + topic)
    count += 1

f = open('todo.txt', 'w+')
for item in todo:
    f.write(item)
f.close()

