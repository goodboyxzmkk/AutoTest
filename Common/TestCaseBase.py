import unittest, time
from Common import DriverManage, ConfigManage
from Utils.SeleniumUtils2 import Seleniumutils
from selenium.webdriver.common.by import By
from Common.DriverManage import DriverManagerClass

# 元素定位：文件名称
loginElement = ConfigManage.get_yaml_pagedic('loginElement.yaml')


class TestBaseClass(unittest.TestCase):
    def setUp(self) -> None:
        print("===========setUp:测试用例开始=============")
        self.flag = True
        driver_manager = DriverManagerClass()
        self.driver = driver_manager.Get_Driver(loginElement['UAT']['browserType'])
        self.seleniumutils = Seleniumutils(self.driver)
        print("【打开浏览器】：" + loginElement['UAT']['browserType'])
        self.driver.get(loginElement['UAT']['URL'])
        print("【打开URL】：" + loginElement['UAT']['URL'])
        time.sleep(2)

    def tearDown(self) -> None:
        # 异常截图
        if (self.flag):
            self.seleniumutils.screenshot_img(self._testMethodName)
        self.driver.quit()
        print("==============tearDown:测试用例结束===============")

    def DefaultLogin(self):
        self.seleniumutils.input(By.XPATH, loginElement['登录页面']['用户名'], loginElement['数据']['用户名'])
        self.seleniumutils.input(By.XPATH, loginElement['登录页面']['密码'], loginElement['数据']['密码'])
        self.seleniumutils.click(By.XPATH, loginElement['登录页面']['登录按键'])
        time.sleep(1)
        self.seleniumutils.click(By.XPATH, loginElement['登录页面']['登录主体'])
        # time.sleep(1)
        self.seleniumutils.click(By.XPATH, loginElement['登录页面']['确认登录'])
        time.sleep(2)
        print("【默认登录成功】")
