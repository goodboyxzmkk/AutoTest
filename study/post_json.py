import requests
import urllib3

urllib3.disable_warnings()  # 去除警告
# verify=False 不校验SSL
url = "http://localhost:8080//j_acegi_security_check"

# 格式1:application/json  传输参数为：json
body = {
    "j_username": "admin",
    "j_password": "admin",
    "from": "/",
    "Submit": "登录"
}

# 格式2：application/x-www-form-urlencoded  传输参数为：data
body2 = {
    "j_username": "admin",
    "j_password": "admin",
    "json": {"j_username": "admin",
             "j_password": "admin",
             "from": "/"},
    "from": "/",
    "Submit": "登录"
}

header = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"
}

# 格式1:application/json  传输参数为：json  其它传data
# 格式2：application/x-www-form-urlencoded  传输参数为：data
r = requests.post(url=url, data=body, headers=header, verify=False)
print(r.encoding)
print(r.url)
print(r.cookies)  #
print(r.content)  # 正文用二进制流输出
print(r.text)  # 正文utf-8输出
