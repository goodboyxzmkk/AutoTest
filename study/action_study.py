import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.hao123.com/')
# 开始位置：定位到元素的原位置
# source = driver.find_element_by_xpath('//*[@id="search"]/form/div[3]/input')
print("滚动中")
# 结束位置：定位到元素要移动到的目标位置
target = driver.find_element_by_xpath('//*[@id="box-toplist1"]/div/h3')

driver.execute_script("arguments[0].scrollIntoView();", target)

# 执行元素的拖放操作
# ActionChains(driver).drag_and_drop(source, target).perform()
print('滚动结束')
time.sleep(5)
driver.quit()