from PluginManager import Model_Plugin
from main import *
import main


global version
version='v1.0.0'

class Plugin2(Model_Plugin):
    def __init__(self):
        pass

    #实现接入点的接口
    def load(self):
        info={
            'package':'xyz.veltgop.shenquan',
            'name':'神权系统',
            'author':'官方',
            'version':version
        }
        Plugin.load_plugin(info,main.AllPlugins)
        if Plugin.check_plugin('xyz.veltgop.admin',main.AllPlugins)!=True:
            logger.critical("插件钠支付缺少前置xyz.veltgop.administor")