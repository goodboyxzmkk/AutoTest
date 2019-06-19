import unittest, time
from Common import TestCaseBase, ConfigManage
from selenium.webdriver.common.by import By
from Utils.SeleniumUtils2 import Seleniumutils

loginElement = ConfigManage.get_yaml_pagedic('loginElement.yaml')


# @unittest.skip('无条件跳过用例')
class Test_LoginClass(TestCaseBase.TestBaseClass):

    def test_001_loginCase(self):
        self.seleniumutils.input(By.XPATH, loginElement['登录页面']['用户名'], loginElement['数据']['用户名'])
        self.seleniumutils.input(By.XPATH, loginElement['登录页面']['密码'], loginElement['数据']['密码'])
        self.seleniumutils.click(By.XPATH, loginElement['登录页面']['登录按键'])
        time.sleep(2)
        self.seleniumutils.click(By.XPATH, loginElement['登录页面']['登录主体'])
        # time.sleep(1)
        self.seleniumutils.click(By.XPATH, loginElement['登录页面']['确认登录'])
        time.sleep(3)
        assert self.seleniumutils.get_text(By.XPATH, loginElement['断言']['我的']) == "我的"
        self.flag = False


if __name__ == "__main__":
    unittest.main()
