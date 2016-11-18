#coding:utf-8
import os


def getfilelist(dir, fileList):
    newdir = dir
    if os.path.isfile(dir):
        fileList.append(dir.decode('gbk'))
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newdir=os.path.join(dir, s)
            getfilelist(newdir, fileList)
    return fileList

list = getfilelist('D:\\2', [])


for fileName in list:
    newfilename = fileName
    newfilename = newfilename.replace('.html', '.txt')
    fileW = open(newfilename, 'w+')
    done = 0
    for line in open(fileName, "r"):
        if line.find("codehilite") != -1:
            done = 1
        if done == 1:
            targetLine = ''
            line = '   ' + line
            while line != '':
                cur = line.find("<")
                if cur != -1:
                    if cur != 0:
                        targetLine += line[0:cur]
                    line = line[cur + 1:]
                    cur = line.find(">")
                    if cur != -1:
                        if cur != len(line) - 1:
                            line = line[cur + 1:]
                        else:
                            line = ''
                else:
                    break
            fileW.write(targetLine)
            fileW.write('\n')
            if line.find("</pre></div>") != -1:
                done = 0

    fileW.close()


