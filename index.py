# -*- coding: utf-8 -*-
import os
import web
import menu
from zouwx import zouwx
from controller import controller

urls = (
'/weixin','zouwx',
'/menu/(.+)','controller'
)


app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
render = web.template.render(templates_root)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()