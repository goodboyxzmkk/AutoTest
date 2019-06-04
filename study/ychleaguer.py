from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://192.168.2.103:9999/admin")
driver.find_element_by_id("txtName").send_keys("cjz")
driver.find_element_by_id("txtPwd").send_keys("1")
driver.find_element_by_id("fm-login-submit").click()

# 延迟时间
time.sleep(2)
# 打开会员管理页面
driver.find_element_by_id('mumu_group100001400').click()
time.sleep(1)
# 打开会员储值页面
driver.find_element_by_id('left_101044600').click()
time.sleep(1)
# 打开口令补币页面
driver.find_element_by_id('left_101002100').click()
# time.sleep(5)
frame = driver.find_element_by_css_selector("#TabContent > div:nth-child(2) > iframe")
driver.switch_to.frame(frame)

print("切换成功")
time.sleep(2)
# driver.find_element_by_css_selector("#View_TokenTakeCoinLog\*0 > div.ych-reports-footer > div.ych-reports-btn-group > button").click()
driver.find_element_by_xpath("//*[@id='View_TokenTakeCoinLog*0']/div[2]/div[1]/button/span").click()
time.sleep(5)
driver.quit()
