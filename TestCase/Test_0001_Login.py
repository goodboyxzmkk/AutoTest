import unittest, time
from Public import TestCaseBase, ConfigManage
from Public.LocationType import Location as type
from Utils import SeleniumUtils

loginElement = ConfigManage.get_yaml_pagedic('loginElement.yaml')


@unittest.skip('无条件跳过用例')
class Test_LoginClass(TestCaseBase.TestBaseClass):

    def test_001_loginCase(self):
        SeleniumUtils.input(self, type.xpath, loginElement['登录页面']['用户名'], loginElement['数据']['用户名'])
        SeleniumUtils.input(self, type.xpath, loginElement['登录页面']['密码'], loginElement['数据']['密码'])
        SeleniumUtils.click(self, type.xpath, loginElement['登录页面']['登录按键'])
        time.sleep(2)
        SeleniumUtils.click(self, type.xpath, loginElement['登录页面']['登录主体'])
        # time.sleep(1)
        SeleniumUtils.click(self, type.xpath, loginElement['登录页面']['确认登录'])
        time.sleep(3)
        assert SeleniumUtils.get_text(self, type.xpath, loginElement['断言']['我的']) == "我的"
        self.flag = False


if __name__ == "__main__":
    unittest.main()
