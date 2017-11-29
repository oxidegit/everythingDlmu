# -*- coding:utf-8 -*-
import re
import requests as r
from PIL import Image
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFilter
import sys
import pytesseract
from bs4 import BeautifulSoup
import bs4
from selenium import webdriver


#爬取图书借阅信息
#爬取课程信息

class DlnuSpider:
    def __init__(self, stu_account, stu_pwd):
        self.account = stu_account
        self.pwd = stu_pwd
        self.sess = r.Session()
        self.dlnu_url = {'library_check':'http://210.30.8.233:8080/reader/captcha.php',#图书管理系统验证码url
                        'library_index':'http://210.30.1.114:8089/Self/nav_login',#图书管理系统首页
                         'library_login':'http://210.30.8.233:8080/reader/redr_verify.php',#图书管理系统登录页面
                         'library_book':'http://210.30.8.233:8080/reader/book_hist.php?page=1',#图书管理系统图书信息页面
                        'school_login':'http://zhjw.dlnu.edu.cn/loginAction.do',#教务系统登录页面
                        'course_info':'http://zhjw.dlnu.edu.cn/xkAction.do',#课程信息页面
                         'net_index':'http://210.30.1.114:8089/Self/nav_login',#校园网系统首页
                        'net_info':'http://210.30.1.114:8089/Self/nav_getUserInfo'#校园网信息页面
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
            resp = self.sess.get(self.dlnu_url['library_check'])
            # 将图片打开
            path = 'C:\\Users\\f404-1\\Desktop\\a.gif'
            with open (path, 'wb') as f:
                f.write(resp.content)
            img = Image.open(path)
            checkcode = pytesseract.image_to_string(img, lang='eng') #识别出来的验证码

            kv = {'number':self.account, 'passwd':self.pwd, 'captcha':checkcode, 'select':'cert_no', 'returnUrl':None}

            #提交表单
            resp = self.sess.post(self.dlnu_url['library_login'], data = kv, headers = {'user-agent': 'Mozilla/5.0'})
            bookInfo = self.sess.get(self.dlnu_url['library_book'], headers = {'user-agent': 'Mozilla/5.0'})
            bookInfo.encoding = bookInfo.apparent_encoding
            #print bookInfo.text
            soup = BeautifulSoup(bookInfo.text, 'html.parser')

            #print (soup.table.contents)
            info = []#保存每本书的信息
            i = 0
            for tr in soup.find('table').children:
                if isinstance(tr, bs4.element.Tag):
                    tds = tr('td')
                    if i != 0:
                        info.append((tds[2].string, tds[3].string, tds[4].string, tds[5].string))
                    i += 1

            #print resp.content
            # 将图片加载到网页上面去
            if (len(resp.text) == 288):
                state = 0
            else:
                state = 1
            return info, state
        except:
            return '出错了'

    #爬取校园网信息

    def getNetBySele(self):
        browser = webdriver.Firefox()
        browser.get(self.dlnu_url['net_index'])
        #提交表单
        acc = browser.find_element_by_id('account')
        pwd = browser.find_element_by_id('pass')
        acc.send_keys(self.account)
        pwd.send_keys(self.pwd)
        submit = browser.find_element_by_name('Submit')
        submit.click()
        try:
            browser.get(self.dlnu_url['net_info'])
            content = {}

            a = browser.find_elements_by_class_name('account')
            content[u'账号:'] = a[0].text
            content[u'套餐:'] = browser.find_element_by_class_name('service').text
            content[u'余额:'] = browser.find_element_by_class_name('redtext').text
            content[u'状态:'] = browser.find_element_by_class_name('greentextl').text
            #content['是否在线'] = browser.find_element_by_class_name('greentext21')
            info = browser.find_elements_by_class_name('t_r1')
            content[u'本月时长:'] = info[1].text
            content[u'本月流量:'] = info[2].text
            content[u'用户类别:'] = info[4].text
            return content
        except:
            browser.close()
    # 爬取校园网信息
    def getNetInfo(self):
        try:
            r = self.sess.get(self.dlnu_url['net_index'])
            rst = re.search(r'checkcode=\"(\d{4})\"', r.content)
            checkcode = rst.group(1)
            h = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
                 'Accept':'text/html,application/xhtml+xm…plication/xml;q=0.9,*/*;q=0.8',
                 'Accept-Encoding':'gzip, deflate',
                 'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                 'Connection':'keep-alive',
                 'Content-Type	':'application/x-www-form-urlencoded',
                 'Referer':'http://210.30.1.114:8089/Self/nav_login',
                 'Cookie':'JSESSIONID=2A22F5C6B55B176076C52D3E13ABD928'
                 }
            kv = {'account': self.account, 'password': '2e31a5d7acc69951c56164863aa52955', 'checkcode': checkcode, 'Submit': '登+录',
                  'code': None}
            r1 = self.sess.post(self.dlnu_url['net_login'], data=kv,headers=h)
            #print r1.text
            if (len(r1.text) == 288):
                state = 0
            else:
                state = 1

            return r1.text, state
        except:

            return '出错了'

            # 爬取课程信息

if __name__ == '__main__':
    a = DlnuSpider('wangpengjie1', 'wpjf404')
    content = a.getNetBySele()

    for (d, x) in content.items():
        print format("%s %s"%(d, x))
