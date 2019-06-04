import requests
import urllib.parse

# url转码

d = "中文"
r = requests.get("http://zzk.cnblogs.com/s/blogpost?Keywords=%s" % d, verify=False)
print(r.url)
aa = "%E4%B8%AD%E6%96%87"
# 编码
print("ddd:"+urllib.parse.quote(d))
# 解码
print(urllib.parse.unquote(aa))

a = r.url.encode("utf-8")
print(type(a))
