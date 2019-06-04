# coding:utf-8
import yaml
import os

projectPath = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))  # 项目路径
# reportPath = projectPath + '\\TestReport\\'  # 测试报告目录
# testCasePath = projectPath + '\\TestCase\\'  #测试用例目录
# imagePath = projectPath + '\\Image\\'  # 错误截图目录
# dataPath = projectPath + '\\TestData\\'  # 测试数据目录

reportPath = os.path.join(projectPath,"TestReport\\")# 测试报告目录
testCasePath = os.path.join(projectPath,"TestCase\\")# 测试用例目录
imagePath = os.path.join(projectPath,"Image\\")# 错误截图目录
dataPath = os.path.join(projectPath,"TestData\\")# 测试数据目录



def get_default_configdic():
    # config yaml文件目录
    configpath = os.path.join(projectPath,"ConfigFile")
    yamlPath = os.path.join(configpath, "Config.yaml")  # 拼接config.yaml文件
    # open方法打开直接读出来
    # projectPath + '\\ConfigFile\\Config.yaml'
    f = open(yamlPath, 'r', encoding='utf-8')
    cfg = f.read()  # 读出来是字符串
    dic = yaml.load(cfg, Loader=yaml.FullLoader)  # 用load方法转字典
    # print('读取config.yaml成功')
    return dic


def get_configdic(configName):
    # config yaml文件目录
    configpath = configpath = os.path.join(projectPath,"ConfigFile")
    yamlPath = os.path.join(configpath, configName)  # 拼接config.yaml文件
    # open方法打开直接读出来
    # projectPath + '\\ConfigFile\\Config.yaml'
    f = open(yamlPath, 'r', encoding='utf-8')
    cfg = f.read()  # 读出来是字符串
    dic = yaml.load(cfg, Loader=yaml.FullLoader)  # 用load方法转字典
    # print('读取config.yaml成功')
    return dic


def get_yaml_pagedic(pageName):
    # 获取page元素定位目录
    pagepath = projectPath + '\\PageElement'
    yamlPath = os.path.join(pagepath, pageName)
    f = open(yamlPath, 'r', encoding='utf-8')
    cfg = f.read()  # 读出来是字符串
    dic = yaml.load(cfg, Loader=yaml.FullLoader)  # 用load方法转字典
    # print('读取loginelement.yaml成功')
    return dic


if __name__ == "__main__":
    get_default_configdic()
    loginpage = get_yaml_pagedic('loginElement.yaml')
    print("URL:" + loginpage['UAT']['URL'])
