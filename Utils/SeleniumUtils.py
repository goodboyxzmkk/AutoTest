# coding:utf-8

import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from Common import ConfigManage


# 前进
def forward(self):
    self.driver.forward()
    print('【浏览器前进】')


# 浏览器后退
def back(self):
    self.driver.back()
    print('【浏览器后退】')


# 回车
def Key_Enter(self, loc):
    print('【浏览器后退】')


# 获取截图
def screenshot_img(self, methodName):
    file_path = ConfigManage.imagePath
    rq = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
    img_name = file_path + rq + '_' + methodName + '.png'
    try:
        self.driver.get_screenshot_as_file(img_name)
    except NameError as e:
        self.get_windows_img()
    print("【异常截图路径】：" + img_name)


# 切换窗口
def switch_handel(self):
    all_handles = self.driver.window_handles
    for handle in all_handles:
        self.driver.switch_to.window(handle)
    print('【浏览器切换窗口】')


# 输入框输入方法
def input(self, type, loc, value):
    # highlight_element(self, type, loc)
    if type == By.XPATH:
        self.driver.find_element(By.XPATH, loc).send_keys(value)
    elif type == By.CLASS_NAME:
        self.driver.find_element(By.CLASS_NAME, loc).send_keys(value)
    elif type == By.ID:
        self.driver.find_element(By.ID, loc).send_keys(value)
    elif type == By.NAME:
        self.driver.find_element(By.NAME, loc).send_keys(value)
    elif type == By.LINK_TEXT:
        self.driver.find_element(By.LINK_TEXT, loc).send_keys(value)
    elif type == By.PARTIAL_LINK_TEXT:
        self.driver.find_element(By.PARTIAL_LINK_TEXT, loc).send_keys(value)
    elif type == By.CSS_SELECTOR:
        self.driver.find_element(By.CSS_SELECTOR, loc).send_keys(value)
    print("【输入】：{} , 定位方式：{} , 定位表达式：{},".format(value, type, loc))


def input_and_KeyEnter(self, type, loc, value):
    highlight_element(self, type, loc)
    if type == By.XPATH:
        self.driver.find_element(By.XPATH, loc).send_keys(value)
        self.driver.find_element_by_xpath(loc).send_keys(Keys.ENTER)
    elif type == By.CLASS_NAME:
        self.driver.find_element(By.CLASS_NAME, loc).send_keys(value)
        self.driver.find_element(By.CLASS_NAME, loc).send_keys(Keys.ENTER)
    elif type == By.ID:
        self.driver.find_element(By.ID, loc).send_keys(value)
        self.driver.find_element(By.ID, loc).send_keys(Keys.ENTER)
    elif type == By.NAME:
        self.driver.find_element(By.NAME, loc).send_keys(value)
        self.driver.find_element(By.NAME, loc).send_keys(Keys.ENTER)
    elif type == By.LINK_TEXT:
        self.driver.find_element(By.LINK_TEXT, loc).send_keys(value)
        self.driver.find_element(By.LINK_TEXT, loc).send_keys(Keys.ENTER)
    elif type == By.PARTIAL_LINK_TEXT:
        self.driver.find_element(By.PARTIAL_LINK_TEXT, loc).send_keys(value)
        self.driver.find_element(By.PARTIAL_LINK_TEXT, loc).send_keys(Keys.ENTER)
    elif type == By.CSS_SELECTOR:
        self.driver.find_element(By.CSS_SELECTOR, loc).send_keys(value)
        self.driver.find_element(By.CSS_SELECTOR, loc).send_keys(Keys.ENTER)
    print("【输入】：{} , 定位方式：{} , 定位表达式：{},".format(value, type, loc))


# 点击方法
def click(self, type, loc):
    # highlight_element(self, type, loc)
    if type == By.XPATH:
        self.driver.find_element(By.XPATH, loc).click()
    elif type == By.CLASS_NAME:
        self.driver.find_element(By.CLASS_NAME, loc).click()
    elif type == By.ID:
        self.driver.find_element(By.ID, loc).click()
    elif type == By.NAME:
        self.driver.find_element(By.NAME, loc).click()
    elif type == By.LINK_TEXT:
        self.driver.find_element(By.LINK_TEXT, loc).click()
    elif type == By.PARTIAL_LINK_TEXT:
        self.driver.find_element(By.PARTIAL_LINK_TEXT, loc).click()
    elif type == By.CSS_SELECTOR:
        self.driver.find_element(By.CSS_SELECTOR, loc).click()
    print("【点击元素】 , 定位方式：{} ， 定位表达式：{}，".format(type, loc))


# 清除方法
def clear(self, type, loc):
    highlight_element(self, type, loc)
    if type == By.XPATH:
        self.driver.find_element(By.XPATH, loc).clear()
    elif type == By.CLASS_NAME:
        self.driver.find_element(By.CLASS_NAME, loc).clear()
    elif type == By.ID:
        self.driver.find_element(By.ID, loc).clear()
    elif type == By.NAME:
        self.driver.find_element(By.NAME, loc).clear()
    elif type == By.LINK_TEXT:
        self.driver.find_element(By.LINK_TEXT, loc).clear()
    elif type == By.PARTIAL_LINK_TEXT:
        self.driver.find_element(By.PARTIAL_LINK_TEXT, loc).clear()
    elif type == By.CSS_SELECTOR:
        self.driver.find_element(By.CSS_SELECTOR, loc).clear()
    print("【清空元素文本】 , 定位方式：{} ， 定位表达式：{}".format(type, loc))


'''高亮显示元素'''


def highlight_element(self, type, loc):
    if type == By.XPATH:
        element = self.driver.find_element_by_xpath(loc)
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element,
                                   "background: yellow; border: 2px solid red;")
    elif type == By.ID:
        element = self.driver.find_element_by_id(loc)
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element,
                                   "background: yellow; border: 2px solid red;")
    elif type == By.NAME:
        element = self.driver.find_element_by_name(loc)
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element,
                                   "background: yellow; border: 2px solid red;")
    elif type == By.LINK_TEXT:
        element = self.driver.find_element_by_link_text(loc)
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element,
                                   "background: yellow; border: 2px solid red;")
    elif type == By.PARTIAL_LINK_TEXT:
        element = self.driver.find_element_by_partial_link_text(loc)
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element,
                                   "background: yellow; border: 2px solid red;")
    elif type == By.CLASS_NAME:
        element = self.driver.find_element_by_class_name(loc)
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element,
                                   "background: yellow; border: 2px solid red;")
    elif type == By.CSS_SELECTOR:
        element = self.driver.find_element_by_css_selector(loc)
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element,
                                   "background: yellow; border: 2px solid red;")


# 获取文本信息
def get_text(self, type, loc):
    highlight_element(self, type, loc)
    if type == By.XPATH:
        return self.driver.find_element(By.XPATH, loc).text
    elif type == By.CLASS_NAME:
        return self.driver.find_element(By.CLASS_NAME, loc).text
    elif type == By.ID:
        return self.driver.find_element(By.ID, loc).text
    elif type == By.NAME:
        return self.driver.find_element(By.NAME, loc).text
    elif type == By.LINK_TEXT:
        return self.driver.find_element(By.LINK_TEXT, loc).text
    elif type == By.PARTIAL_LINK_TEXT:
        return self.driver.find_element(By.PARTIAL_LINK_TEXT, loc).text
    elif type == By.CSS_SELECTOR:
        return self.driver.find_element(By.CSS_SELECTOR, loc).text
    print("【获取元素文本】 , 定位方式：{} ， 定位表达式：{}".format(type, loc))


# 移动鼠标悬停在某元素上
def move_to_elemen_and_click(self, type, loc):
    if type == By.XPATH:
        xm = self.driver.find_element(By.XPATH, loc)
        webdriver.ActionChains(self.driver).click(xm).perform()
    elif type == By.ID:
        xm = self.driver.find_element(By.ID, loc)
        webdriver.ActionChains(self.driver).click(xm).perform()
    elif type == By.NAME:
        xm = self.driver.find_element(By.NAME, loc)
        webdriver.ActionChains(self.driver).click(xm).perform()
    elif type == By.LINK_TEXT:
        xm = self.driver.find_element(By.LINK_TEXT, loc)
        webdriver.ActionChains(self.driver).click(xm).perform()
    elif type == By.CSS_SELECTOR:
        xm = self.driver.find_element(By.CSS_SELECTOR, loc)
        webdriver.ActionChains(self.driver).click(xm).perform()
    print("【鼠标悬停】在元素上,定位方式：{} ， 定位表达式：{}".format(type, loc))


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
def element_is_visibility(self, loc, timeout=10):
    try:
        WebDriverWait(self, timeout).until(expected_conditions.visibility_of_element_located(By.XPATH, loc))
        print("【等待元素】时间：{}秒，定位表达式：{}".format(timeout, loc))
        return True
    except TimeoutError:
        return False


# 滚动界面
def page_slide(self, value):
    js = "var q=document.documentElement.scrollTop=" + str(value) + ""
    self.driver.execute_script(js)
    print("【滚动界面】到:{}  元素".format(value))


# 结束浏览器进程
def kill_driver(self, driver_name):
    if driver_name[-4:].lower() != ".exe":
        driver_name += ".exe"
    os.system("taskkill /f /im " + driver_name)
    print("【结束浏览器进程】")


# 选择下拉框的某一个值
def select_by_value(self, type, loc, value):
    if type == By.XPATH:
        element = self.driver.find_element_by_xpath(loc)
        Select(element).select_by_value(value)
    elif type == By.ID:
        element = self.driver.find_element_by_id(loc)
        Select(element).select_by_value(value)
    elif type == By.NAME:
        element = self.driver.find_element_by_name(loc)
        Select(element).select_by_value(value)
    elif type == By.CSS_SELECTOR:
        element = self.driver.find_element_by_css_selector(loc)
        Select(element).select_by_value(value)
