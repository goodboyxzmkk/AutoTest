# coding:utf-8

import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from Common import ConfigManage


class Seleniumutils(object):

    def __init__(self, driver):
        self.driver = driver

    # 前进
    def forward(self):
        self.driver.forward()
        print('【浏览器前进】')

    # 浏览器后退
    def back(self):
        self.driver.back()
        print('【浏览器后退】')

    # 获取截图
    def screenshot_img(self, methodName):
        file_path = ConfigManage.imagePath
        rq = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
        img_name = file_path + rq + '_' + methodName + '.png'
        try:
            self.driver.get_screenshot_as_file(img_name)
        except NameError as e:
            self.driver.get_windows_img()
        print("【异常截图路径】：" + img_name)

    # 切换窗口
    def switch_handel(self):
        all_handles = self.driver.window_handles
        for handle in all_handles:
            self.driver.switch_to.window(handle)
        print('【浏览器切换窗口】')

    # 输入框输入方法
    def input(self, by, loc, value):
        '''
        往输入框输入内容
        :param by: 定位方式
        :param loc: 定位表达式
        :param value: 输入值
        :return:
        '''
        self.highlight_element(by, loc)
        self.driver.find_element(by, loc).send_keys(value)
        print("【输入】：{} , 定位方式：{} , 定位表达式：{},".format(value, by, loc))

    def input_and_KeyEnter(self, by, loc, value):
        '''
        输入并回车方法
        :param by: 定位方式
        :param loc: 定位表达式
        :param value: 输入值
        :return:
        '''
        self.highlight_element(by, loc)
        self.driver.find_element(by, loc).send_keys(value)
        self.driver.find_element(by, loc).send_keys(Keys.ENTER)
        print("【输入】：{} , 定位方式：{} , 定位表达式：{},".format(value, by, loc))

    # 点击方法
    def click(self, by, loc):
        '''
        点击元素
        :param by: 定位方式
        :param loc: 定位表达式
        :return:
        '''
        self.highlight_element(by, loc)
        self.driver.find_element(by, loc).click()
        print("【点击元素】 , 定位方式：{} ， 定位表达式：{}，".format(by, loc))

    # 清除方法
    def clear(self, by, loc):
        '''
        清空输入框内容方法
        :param by:定位方式
        :param loc:定位表达式
        :return:
        '''
        self.driver.find_element(by, loc).clear()
        print("【清空元素文本】 , 定位方式：{} ， 定位表达式：{}".format(by, loc))

    def highlight_element(self, by, loc):
        '''
        元素高亮显示
        :param by:定位方式
        :param loc:定位表达式
        :return:
        '''
        element = self.driver.find_element(by, loc)
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element,
                                   "background: yellow; border: 2px solid red;")

    def get_text(self, by, loc):
        '''
        获取文本
        :param by: 定位方式
        :param loc: 定位表达式
        :return:
        '''
        print("【获取元素文本】 , 定位方式：{} ， 定位表达式：{}".format(by, loc))
        return self.driver.find_element(by, loc).text

    # 移动鼠标悬停在某元素上
    def move_to_elemen_and_click(self, by, loc):
        '''
        移动鼠标悬停在某元素上
        :param by: 定位方式
        :param loc: 定位表达式
        :return:
        '''
        xm = self.driver.find_element(by, loc)
        webdriver.ActionChains(self.driver).click(xm).perform()
        print("【鼠标悬停】在元素上,定位方式：{} ， 定位表达式：{}".format(by, loc))

    # 切换进入表单
    def switch_in_iframe(self, iframe):
        # self.driver.switch_to_frame(iframe)
        self.driver.switch_to.frame(iframe)
        # chrome浏览器——f12 ——console用于显示iframe个数
        # document.getElementsByTagName('iframe').length
        print("【切换iframe】,定位表达式：{}".format(iframe))

    # 切出表单
    def switch_out_iframe(self):
        self.driver.switch_to_default_content()
        print("【返回上一层iframe】")

    # 显示等待知道元素可见
    def element_is_visibility(self, by, loc, timeout=10):
        try:
            ui.WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(by, loc))
            print("【等待元素】时间：{}秒，定位表达式：{}".format(timeout, loc))
            return True
        except TimeoutError:
            return False

    def js_slide(self, by, loc):
        '''
        js滚动浏览器,滚动到指定元素位置
        :param by:定位方式
        :param loc:定位表达式
        :return:
        '''
        target = self.driver.find_element(by, loc)
        driver.execute_script("arguments[0].scrollIntoView();", target)
        print("【滚动界面】到:{}  元素".format(loc))

    # 结束浏览器进程
    def kill_driver(self, driver_name):
        if driver_name[-4:].lower() != ".exe":
            driver_name += ".exe"
        os.system("taskkill /f /im " + driver_name)
        print("【结束浏览器进程】")

    # 选择下拉框的某一个值
    def select_by_value(self, by, loc, value):
        element = self.driver.find_element(by, loc)
        Select(element).select_by_value(value)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://192.168.2.106:9999/admin/login.html")
    tt = Seleniumutils(driver)
    tt.input(By.XPATH, '//*[@id="txtName"]', 'admin')
    tt.input(By.XPATH, '//*[@id="txtPwd"]', 'admin')
    tt.click(By.XPATH, '//*[@id="fm-login-submit"]')
    time.sleep(5)
    driver.quit()
