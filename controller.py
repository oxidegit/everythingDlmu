# -*- coding: utf-8 -*-
#控制页面的跳转

import web
import os
import spider as sp

class controller:
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)
    def GET(self, menuId):

        #当用户发送选择信息的数字后，点击链接跳转到这里
        print menuId
        id = int(menuId)
        if id==1:
            #返回查询成绩的登录页面
            return self.render.bindPage(id)
        elif id==2:
            #返回查询借阅信息的登录页面
            return self.render.searchBookInfo(id)
    def POST(self, id):
        
        data = web.input()
        stu_num = data.get('stu_num')
        stu_pwd = data.get('stu_pwd')
        id = int(id)

        #查询课程信息
        if id==1:
            content, state = sp.getCourseInfo('http://zhjw.dlnu.edu.cn/xkAction.do', stu_num, stu_pwd)

            if (state == 0):
                return u"大兄弟，信息错误， 俺无能为力啊".encode("gb2312")
            else:
                return content.encode("gb2312")
        #查询图书借阅信息

        if id==12:


