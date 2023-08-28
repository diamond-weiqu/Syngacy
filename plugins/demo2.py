from PluginManager import Model_Plugin
from main import *
import main
from logger_on import logger

global version
version='v1.0.0'

class Plugin2(Model_Plugin):
    def __init__(self):
        pass

    #实现接入点的接口
    def load(self):
        info={
            'package':'xyz.995200.napay',
            'name':'钠支付',
            'author':'钠加速',
            'version':version
        }
        Plugin.load_plugin(info,main.AllPlugins)
        if Plugin.check_plugin('xyz.995200.napay',main.AllPlugins)!=True:
            logger.critical("插件钠支付缺少前置xyz.veltgop.administor")