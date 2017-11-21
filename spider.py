# -*- coding:utf-8 -*-
import re as Re
import requests as re

#爬取图书借阅信息
#爬取课程信息
def getBookInfo():
    try:
        s = re.Session()
        path = 'C:\\Users\\f404-1\\Desktop\\everythingDlmu\\templates\\image\\a.gif'
        #get请求获取验证码
        image = s.get('http://210.30.8.233:8080/reader/captcha.php')
        #将图片保存到image路径下
        with open(path, 'wb') as f:
            f.write(image.content)

        #将图片加载到网页上面去












        return r2.text, state
    except:
        return '出错了'


#爬取校园网信息
def getNetInfo(url, stu_num, pwd):
    try:
        s = re.Session()
        r = s.get('http://210.30.1.114:8089/Self/nav_login' )
        rst = Re.search(r'checkcode=\"(\d{4})\"', r.content)
        a = rst.group(1)
        kv = {'account':stu_num,'password':'2e31a5d7acc69951c56164863aa52955', 'checkcode':a, 'Submit':'登+录', 'code':None}
        r1 = s.post('http://210.30.1.114:8089/Self/LoginAction.action', data=kv, headers={'user-agent':'Mozilla/5.0'})
        r2 = s.get(url, params={'actionType':'17'}, headers={'user-agent':'Mozilla/5.0'})
        print r1.text
        if (len(r2.text) == 288):
            state = 0
        else:
            state = 1
        r1.raise_for_status()
        r2.raise_for_status()
        r1.encoding = r1.apparent_encoding
        r2.encoding = r2.apparent_encoding
        return r2.text, state
    except:
        return '出错了'

#爬取课程信息
def getCourseInfo(url, stu_num, pwd):
    try:
        s = re.Session()
        kv = {'ldap':'auth', 'zjh':stu_num, 'mm':pwd}
        r1 = s.post('http://zhjw.dlnu.edu.cn/loginAction.do', data=kv, headers={'user-agent':'Mozilla/5.0'})
        r2 = s.get(url, params={'actionType':'17'}, headers={'user-agent':'Mozilla/5.0'})

        if (len(r2.text) == 288):
            state = 0
        else:
            state = 1
        r1.raise_for_status()
        r2.raise_for_status()
        r1.encoding = r1.apparent_encoding
        r2.encoding = r2.apparent_encoding
        return r2.text, state
    except:
        return '出错了'

if __name__ == '__main__':
    getBookInfo()