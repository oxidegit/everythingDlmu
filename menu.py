# -*- coding: utf-8 -*-
from wechatpy import WeChatClient


def createMenu():
    appid = 'wx9884cd6e3b1f1351'
    secret = '67b0a42256f05611b135afd67b51545b'
    menuItem = createMenuItem()
    client = WeChatClient(appid, secret)
    client.menu.add_conditional(menuItem)
def createMenuItem():
    menuFace = {
        "button": [
            {
                "name":"账号相关",
                "sub_button":
                    [
                        {
                            "type":"click",
                            "name":"账号信息",
                            "key":"acc_info"
                        },
                        {
                            "type": "click",
                            "name": "解除绑定",
                            "key": "acc_del"
                        },
                        {
                            "type": "click",
                            "name": "绑定",
                            "key": "acc_add"
                        }
                    ]
            },
            {
                "name":"基本信息",
                "sub_button":
                [
                    {
                        "type": "click",
                        "name": "本学期成绩",
                        "key": "bas_grade"
                    },
                    {
                        "type": "click",
                        "name": "借阅信息",
                        "key": "bas_lend"
                    },
                    {
                        "type": "click",
                        "name": "流量剩余",
                        "key": "bas_remain"
                    }
                ]
            },
            {
                "name":"实用功能",
                "sub_button":
                [
                    {
                        "type": "click",
                        "name": "当天课表",
                        "key": "cnt_course"
                    },
                    {
                        "type": "click",
                        "name": "校园网下线",
                        "key": "web_down"
                    }
                ]
            }
        ]
    }
    return menuFace