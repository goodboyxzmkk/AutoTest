import unittest, time
from Common import TestCaseBase, ConfigManage
from selenium.webdriver.common.by import By
from Utils import ReadFileUtils
from ddt import ddt, data, unpack

orderElement = ConfigManage.get_yaml_pagedic('orderManageElement.yaml')
testData = ReadFileUtils.getdata_from_Csv("Test_orderQuery")


# @unittest.skip('无条件跳过用例')
@ddt
class Test_OrderManage(TestCaseBase.TestBaseClass):

    @data(*testData)
    def test_001_OrderManageCase(self, data):
        super().DefaultLogin()
        time.sleep(1)
        self.seleniumutils.click(By.XPATH, orderElement['首页']['订单管理'])
        time.sleep(1)
        self.seleniumutils.click(By.XPATH, orderElement['订单管理']['头部查询框'])
        time.sleep(3)
        self.seleniumutils.input_and_KeyEnter(By.XPATH, orderElement['订单管理']['跳转查询框'], data['订单号'])
        time.sleep(1)
        retult = self.seleniumutils.get_text(By.XPATH, orderElement['断言']['查询订单号'])
        self.assertEqual(retult, data['订单号'])
        self.flag = False


if __name__ == "__main__":
    print("===继承unittest后执行main,需要手动在edit configuration 添加py文件")
    unittest.main()
