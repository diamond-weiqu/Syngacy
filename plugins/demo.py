import main
from PluginManager import Model_Plugin
from main import *
from logger_on import logger

global version
version='v1.0.0'
class Plugin1(Model_Plugin):
    def __init__(self):
        pass

    #实现接入点的接口
    def load(self):
        info = {
            'package':'xyz.veltgop.administor',
            'name': '管理员',
            'author': '官方',
            'version': version
        }
        Plugin.load_plugin(info,main.AllPlugins)

