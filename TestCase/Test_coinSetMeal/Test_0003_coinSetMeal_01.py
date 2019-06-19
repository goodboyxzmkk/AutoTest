import unittest, json, time, os
from Common import TestCaseBase, ConfigManage
from selenium.webdriver.common.by import By
from Utils import ReadFileUtils
from ddt import ddt, data, unpack
from Utils.MysqlHelper import MySql

'''
用例说明：
1.先选择门店，再添加游戏币套餐
'''

coinSetMealElement = ConfigManage.get_yaml_pagedic('coinSetMealElement.yaml')
testData = ReadFileUtils.getdata_from_Csv("Test_coinSetMeal")
dbconfig = ConfigManage.get_default_configdic()


# @unittest.skip('无条件跳过用例')
@ddt
class Test_CoinSetMeal(TestCaseBase.TestBaseClass):

    @data(*testData)
    def test_001_coinSetMealCase(self, data):
        super().DefaultLogin()
        time.sleep(1)
        self.seleniumutils.click(By.XPATH, coinSetMealElement['首页']['游戏币套餐'])
        time.sleep(1)
        self.seleniumutils.click(By.XPATH, coinSetMealElement['游戏币套餐']['选择门店'])
        time.sleep(3)
        self.seleniumutils.click(By.XPATH, coinSetMealElement['游戏币套餐']['门店内新增按键'])
        self.seleniumutils.input(By.XPATH, coinSetMealElement['游戏币套餐']['游戏币'], data['游戏币'])
        self.seleniumutils.input(By.XPATH, coinSetMealElement['游戏币套餐']['售价'], data['售价'])
        time.sleep(1)
        if data['是否兑换'] == '是':
            self.seleniumutils.click(By.XPATH, coinSetMealElement['游戏币套餐']['兑换开关'])
            self.seleniumutils.input(By.XPATH, coinSetMealElement['游戏币套餐']['兑换积分'], data['积分'])
        self.seleniumutils.click(By.XPATH, coinSetMealElement['游戏币套餐']['保存按键'])

        # 断言是否添加成功
        time.sleep(2)
        self.seleniumutils.click(By.XPATH, coinSetMealElement['游戏币套餐']['查询输入框'])
        time.sleep(1)
        self.seleniumutils.input_and_KeyEnter(By.XPATH, coinSetMealElement['游戏币套餐']['跳转查询框'], data['游戏币'] + '游戏币')
        time.sleep(1)
        result = self.seleniumutils.get_text(By.XPATH, coinSetMealElement['断言']['查询套餐名称'])
        # print(result)
        time.sleep(1)
        assert result == data['游戏币'] + '游戏币'
        self.flag = False


if __name__ == "__main__":
    print("===继承unittest后执行main,需要手动在edit configuration 添加py文件")
    unittest.main()
