# -*- coding:utf-8 -*-
import re
import requests as r

#爬取图书借阅信息
#爬取课程信息

class DlnuSpider:
    def __init__(self, stu_account, stu_pwd):
        self.account = stu_account
        self.pwd = stu_pwd
        self.sess = r.Session()
        self.dlnu_url = {'library_check':'http://210.30.8.233:8080/reader/captcha.php',
                        'library_login':'http://210.30.1.114:8089/Self/nav_login',
                        'school_login':'http://zhjw.dlnu.edu.cn/loginAction.do',
                        'course_info':'http://zhjw.dlnu.edu.cn/xkAction.do',

                     }
    def getCourseInfo(self):
        try:
            kv = {'ldap': 'auth', 'zjh': self.account, 'mm': self.pwd}
            r1 = self.sess.post(self.dlnu_url['school_login'], data=kv, headers={'user-agent': 'Mozilla/5.0'})
            r2 = self.sess.get(self.dlnu_url['course_info'], params={'actionType': '17'}, headers={'user-agent': 'Mozilla/5.0'})
            #判断是否登录成功
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
    def getBookInfo(self):
        try:
            # get请求获取验证码
            image = self.sess.get(self.dlnu_url['library_check'])
            # 将图片打开

            # 将图片加载到网页上面去
            return r2.text, state
        except:
            return '出错了'

    # 爬取校园网信息
    def getNetInfo(url, stu_num, pwd):
        try:
            s = re.Session()
            r = s.get()
            rst = re.search(r'checkcode=\"(\d{4})\"', r.content)
            a = rst.group(1)
            kv = {'account': stu_num, 'password': '2e31a5d7acc69951c56164863aa52955', 'checkcode': a, 'Submit': '登+录',
                  'code': None}
            r1 = s.post('http://210.30.1.114:8089/Self/LoginAction.action', data=kv,
                        headers={'user-agent': 'Mozilla/5.0'})
            r2 = s.get(url, params={'actionType': '17'}, headers={'user-agent': 'Mozilla/5.0'})
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

            # 爬取课程信息

if __name__ == '__main__':
    #getBookInfo()