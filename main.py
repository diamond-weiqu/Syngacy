# -*- coding: utf-8 -*-
import contextlib, os, requests, urllib3, time, hashlib

with contextlib.suppress(Exception):
    os.mkdir("logs")
    open('logs/bot.log', 'w+')
from logger_on import logger
from PluginManager import __ALLMODEL__
from PluginManager import PluginManager
from flask import Flask, request, Response
from ConfigManager import *

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
AllPlugins = []


def genearteMD5(str):
    hl = hashlib.md5()
    hl.update(str.encode(encoding='utf-8'))
    return hl.hexdigest()


class Plugin():
    def __init__(self):
        pass

    def load_plugin(self, AllPlugins):
        if self['package'].count(".") != 2:
            logger.error(f"插件{self['package']}包名不规范，加载失败！")
        else:
            logger.info(f'插件{self["name"]}(作者：{self["author"]})加载成功！版本：{self["version"]}')
            AllPlugins.append(self)

    def check_plugin(self, AllPlugins):
        return any(self == Plugin['package'] for Plugin in AllPlugins)


class Event():
    def __init__(self):
        pass
    # Message_Event(self,):
    # 帮我写一个处理go-cqhttp上报的函数


class Action():
    def __init__(self):
        pass

    def send_group_message(self):
        self = {
            "group_id": self['group_id'],
            "message": self['message'] + "\n本次防风控服务码:" + genearteMD5(str(time.time()))
        }
        res = requests.get(
            url=f'http://127.0.0.1:111/send_group_msg?group_id={self["group_id"]}&message={self["message"]}',
            verify=False,
        )
        return (res.json())


def print_logo():
    logger.info("    _   __      __       _                    ______                     ")
    logger.info("   / | / /___ _/ /______(_)_  ______ ___     / ____/________  __  ______ ")
    logger.info("  /  |/ / __ `/ __/ ___/ / / / / __ `__ \   / / __/ ___/ __ \/ / / / __ \ ")
    logger.info(" / /|  / /_/ / /_/ /  / / /_/ / / / / / /  / /_/ / /  / /_/ / /_/ / /_/ /")
    logger.info("/_/ |_/\__,_/\__/_/  /_/\__,_/_/ /_/ /_/   \____/_/   \____/\__,_/ .___/ ")
    logger.info("                                                                /_/      ")


if __name__ == '__main__':
    if not os.path.isfile("lock"):
        logger.info("您已进入文件补全模式")
        logger.info("或许因为您是第一次使用 Natrium 框架，或许删除了某些文件")
        logger.info("若您的文件缺失，可以删除根目录下的 lock 文件，即会进入该模式")
        logger.info("正在进行文件补全......")
        open('lock', 'w+')
        with contextlib.suppress(Exception):
            os.mkdir("configs")
            open('configs/main/config.yml', 'w+')
        with contextlib.suppress(Exception):
            os.mkdir("plugins")
    print_logo()
    logger.info("请稍等，框架正在初始化...")

    app = Flask(__name__)
    PluginManager.LoadAllPlugin()
    for SingleModel in __ALLMODEL__:
        plugins = SingleModel.GetPluginObject()
        for item in plugins:
            item.load()


    @app.route('/', methods=["POST"])
    def event_listener():
        return 'OK'


    logger.info("Natrium 框架启动成功！")
    app.run(debug=False, host='127.0.0.1', port=5701)
