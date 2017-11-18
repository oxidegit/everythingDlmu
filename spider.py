# -*- coding:utf-8 -*-
import requests as re

#爬去课程信息

def getHtmlText2(url, stu_num, pwd):
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
    a, b = getHtmlText2('http://zhjw.dlnu.edu.cn/xkAction.do', '2015082328', '123456')