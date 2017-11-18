# -*- coding: utf-8 -*-
#控制页面的跳转

import web
import os
import sae.kvdb

class controller:
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)
        self.kv = sae.kvdb.Client()
    def GET(self, menuId):
        
        id = int(menuId)
        if (not id == 1):
            return self.render.register('zoucheng')
        else:
            return self.render.bindPage()
        self.kv.disconnect_all()
    def POST(self, id):
        
        data = web.input()
        stu_num = data.get('stu_num')
        stu_pwd = data.get('stu_pwd')
        id = int(id)
        
        
        #user bind
        if id==10:
            if (not self.kv.get(str(stu_num))):
                self.kv.set(str(stu_num), str(stu_pwd))
            	return u'student_number:'+data.get('stu_num')+u'has success bind'
            else:
                return 'The number has bean binded'
        self.kv.disconnect_all()
        
        '''
        if True:
            return 'dealBindInfo'
        else:
            id = int(menuId)
            if (id == 1):
                return self.render.bindPage()
        '''


