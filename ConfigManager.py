from main import *
import yaml, json
class Config():
    def __init__(self,package,mode="json",name=None):
        if name is None:
            name = "config"
        if mode == "json":
            with open(f'./configs/{package}/{name}.json', 'r', encoding='utf-8') as f:
                self.config = json.load(f)
        elif mode == "yml":
            with open(f'./configs/{package}/{name}.yml', 'r', encoding='utf-8') as f:
                self.config = yaml.load(f.read(), Loader=yaml.FullLoader)
    def getConfig(self):
        return self.config