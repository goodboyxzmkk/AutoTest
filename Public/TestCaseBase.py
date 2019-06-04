import unittest, time
from Public import DriverManage, ConfigManage
from Utils import SeleniumUtils
from Public.LocationType import Location as type
# from Public.DriverManage import DriverManagerClass

# 元素定位：文件名称
loginElement = ConfigManage.get_yaml_pagedic('loginElement.yaml')


class TestBaseClass(unittest.TestCase):
    def setUp(self) -> None:
        print("===========setUp:测试用例开始=============")
        self.flag = True
        self.driver = DriverManage.DriverManagerClass.Get_Driver(self, loginElement['UAT']['browserType'])
        print("【打开浏览器】：" + loginElement['UAT']['browserType'])
        self.driver.get(loginElement['UAT']['URL'])
        print("【打开URL】：" + loginElement['UAT']['URL'])

        time.sleep(2)

    def tearDown(self) -> None:
        # 异常截图
        if (self.flag):
            test_methodName = self._testMethodName
            SeleniumUtils.screenshot_img(self, test_methodName)
        self.driver.quit()
        print("==============tearDown:测试用例结束===============")

    def DefaultLogin(self):
        SeleniumUtils.input(self, type.xpath, loginElement['登录页面']['用户名'], loginElement['数据']['用户名'])
        SeleniumUtils.input(self, type.xpath, loginElement['登录页面']['密码'], loginElement['数据']['密码'])
        SeleniumUtils.click(self, type.xpath, loginElement['登录页面']['登录按键'])
        time.sleep(1)
        SeleniumUtils.click(self, type.xpath, loginElement['登录页面']['登录主体'])
        # time.sleep(1)
        SeleniumUtils.click(self, type.xpath, loginElement['登录页面']['确认登录'])
        time.sleep(2)
        print("【默认登录成功】")
