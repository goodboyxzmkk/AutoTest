import requests
import urllib3

urllib3.disable_warnings()  #去除警告
# verify=False 不校验SSL
r = requests.get('https://www.baidu.com', verify=False)
print(r.encoding)
print(r.content)  # 正文用二进制流输出
print(r.text)  # 正文用utf-8输出
print(r.raise_for_status())  # 查看异常
