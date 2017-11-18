# -*- coding: utf-8 -*-
import os
import web

class bindUser:
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)
    def GET(self):
        name = 'Bob'
        return self.render.register(name)
    def POST(self):
        return