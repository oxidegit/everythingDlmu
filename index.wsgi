# -*- coding: utf-8 -*-
import os
import sae
import web
import sae
import menu
import sae.kvdb
sae.add_vendor_dir('vendor')
from weixinInterface import WeixinInterface
from zouwx import zouwx
from controller import controller

urls = (
'/weixin','zouwx',
'/menu/(.+)','controller'
)


app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
render = web.template.render(templates_root)

#menu.createMenu()

app = web.application(urls, globals()).wsgifunc()        
application = sae.create_wsgi_app(app)