# import os, json
# import time
from selenium import webdriver
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.ui import Select


class DriverManagerClass():
    def Get_Driver(self, type):
        if type.lower() == 'firefox':
            self.driver = webdriver.Firefox()
            self.driver.maximize_window()
            return self.driver
        elif type.lower() == 'ie':
            self.driver = webdriver.Ie()
            self.driver.maximize_window()
            return self.driver
        elif type.lower() == 'h5':  # H5页面
            mobile_emulation = {'deviceName': 'iPhone 6/7/8'}
            options = webdriver.ChromeOptions()
            options.add_experimental_option("mobileEmulation", mobile_emulation)
            self.driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
            return self.driver
        else:  # chrome
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            return self.driver
