import requests
import urllib3
from requests.cookies import RequestsCookieJar

urllib3.disable_warnings()  # 去除警告
# verify=False 不校验SSL
url = "http://192.168.2.109:9999/DTOWebLogin"
header = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"
}

body = {
    "UserName": "kf2",
    "Password": "MQ=="
}

# 格式1:application/json  传输参数为：json  其它传data
# 格式2：application/x-www-form-urlencoded  传输参数为：data
r = requests.post(url=url, data=body, headers=header, verify=False)
print(r.url)
print(r.status_code)
print(r.cookies)

# 退出登录

url2 = "http://192.168.2.109:9999/Organization/DTOAddBizEmployee"

header = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"
}
body2 = {
    "ID": "1205c781-fb4d-445c-bcb0-aa510115560e",
    "LoginName": "sy01",
    "Password": "1",
    "RealName": "收银2",
    "Phone": "",
    "CashAble": "true",
    "DeparmentID": '[{"roleid": "b8b8219a-3e14-4e2a-8451-807805940d2e"}]',
    "DefaultRoleId": "",
    "DataSelectGet": "0",
    "DateSelectTotle": "0",
    "Terminal": ""
}
co = requests.cookies.RequestsCookieJar()
co.set("ss-id", "YPbqaa8mfUoiXyMOhyZK")
co.set("ss-pid", "xSBcwXWQYk5L2o1lPxNJ")
print(co)
r2 = requests.post(url=url2, headers=header, data=body2, cookies=co, verify=False)
print(r2.text)
# r2.up
print(r2.cookies)
