import unittest, json, time, os
from Public import TestCaseBase, ConfigManage
from Public.LocationType import Location as type
from Utils import SeleniumUtils, ReadFileUtils
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
        SeleniumUtils.click(self, type.xpath, orderElement['首页']['订单管理'])
        time.sleep(1)
        SeleniumUtils.click(self, type.xpath, orderElement['订单管理']['头部查询框'])
        time.sleep(3)
        SeleniumUtils.input_and_KeyEnter(self, type.xpath, orderElement['订单管理']['跳转查询框'], data['订单号'])
        time.sleep(1)
        retult = SeleniumUtils.get_text(self, type.xpath, orderElement['断言']['查询订单号'])
        self.assertEqual(retult, data['订单号'])
        self.flag = False


if __name__ == "__main__":
    print("===继承unittest后执行main,需要手动在edit configuration 添加py文件")
    unittest.main()
