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
        print menuId
        id = int(menuId)
        task = id+10
        if (True):
            return self.render.bindPage(task)
    def POST(self, id):
        
        data = web.input()
        stu_num = data.get('stu_num')
        stu_pwd = data.get('stu_pwd')
        id = int(id)

        #user bind
        if id==11:
            content, state = sp.getHtmlText2('http://zhjw.dlnu.edu.cn/xkAction.do', stu_num, stu_pwd)

            if (state == 0):
                return u"大兄弟，信息错误， 俺无能为力啊".encode("gb2312")
            else:
                return content.encode("gb2312")


