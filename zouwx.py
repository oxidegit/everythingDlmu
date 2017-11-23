# -*- coding: utf-8 -*-
import hashlib
import web
import lxml
import time
import requests
import os
import urllib2
import json
from lxml import etree
import cookielib
import re
import random
import cxkd
from imgtest import *
from wechatpy import parse_message
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException
from wechatpy import parse_message
from wechatpy.replies import create_reply
from wechatpy import WeChatClient




class zouwx:
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)

        """
        self.bindPage = web.form.Form(
            web.form.
        )
        """

    def GET(self):
        # 获取输入参数
        print "df"

        try :
            data = web.input()
            signature=data.signature
            timestamp=data.timestamp
            nonce=data.nonce
            echostr = data.echostr
            token="token" #这里改写你在微信公众平台里输入的token
            check_signature(token, signature, timestamp, nonce)
            return echostr
        except InvalidSignatureException:
            return 'a'

        #return "zoucheng"
    def POST(self):
        str_xml = web.data()
        xml = etree.fromstring(str_xml)
        msg = parse_message(str_xml)
        #msgType = xml.find("MsgType").text
        msgType = msg.type
        msgContent = msg.content

        fromUser = xml.find("FromUserName").text
        toUser = xml.find("ToUserName").text

        if (msgType == 'text'):
            if (msgContent.isdigit()):
                if (True):#这里要判断下，输入的功能是否在合理范围内
                    num = int(msgContent)
                    url = 'http://sgyyamn.free.ngrok.cc/menu/'+str(num)
                    if (num==1):
                        info = "课表"
                    elif (num==2):
                        info = "借阅信息"
                    else:
                        info = "校园网信息"
                    a = format("<a href=\"%s\">亲，点击查询%s</a>"%(url, info))
                    reply = create_reply(a, message=msg)
                return reply.render()
            elif (msgContent == u'菜单'):
                print msgContent
                reply = create_reply("输入\n数字1，查询课表\n数字2，查询借阅信息\n数字3，查询校园网信息", message=msg)
            else:
                url = 'http://www.tuling123.com/openapi/api'
                s = json.dumps({'key':'7ddf844547a446a7a9d22e8de2fb41f4', 'info':msgContent, 'userid':'175534'})
                r = requests.post(url, data=s)
                t = json.loads(r.text)
                reply = create_reply(t['text'], message=msg)
        elif (msgType == 'image'):
            reply = create_reply('这是图片消息', message=msg)
        elif (msgType == 'voice'):
            reply = create_reply('这是语音消息', message=msg)
        else:
            reply = create_reply('小伙发的啥玩意儿啊', message=msg)
        # 转换成 XML
        xml = reply.render()
        return xml




