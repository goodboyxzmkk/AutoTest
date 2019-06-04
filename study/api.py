import requests

# r = requests.get('http://www.cnblogs.com/yoyoketang/')
# print(r.status_code)
# print(r.text)

# 地址
url = 'http://zzk.cnblogs.com/s/blogpost'
# 参数
par = {"w": "yoyoketang"}
# 请求头
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36",
    "Cookie":"gads=ID=4a23892025272a94:T=1533000922:S=ALNI_MYFGCj3jHdjrrOXkMG-rCaCv8ebvg; grwng_uid=a93c45e3-fe4e-42de-a1a9-a2cb84917998; gr_user_id=6d74e5a4-3f87-4214-a4d5-49786dd0fcff; UM_distinctid=16783a6f4fa1b3-04f3219738c615-396b4e08-1fa400-16783a6f4fb988; _ga=GA1.2.1039985410.1543933670; _gid=GA1.2.1948842749.1558084843; __utmz=59123430.1558153623.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ZzkNoRobotCookie=CfDJ8JcopKY7yQlPr3eegllP76Ocqdj9KZR4JbHwLmzaTRPiwUHmx59sjr1L1sODYJ2JuauSgy7bMTuK6e8Koj4gtcl60fUQsEddNneh9yhyisRNipmy_5lR-JuKHKoqpAm8yA; DetectCookieSupport=OK; __utma=59123430.1039985410.1543933670.1558153623.1558156393.2; __utmc=59123430; __utmb=59123430.1.10.1558156393",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3"
}
# verify=False  打开fiddler,解决SSL认证错误,
res = requests.get(url=url, params=par, verify=False, headers=header)
print(res.status_code) #状态码
print(res.url) #返回url
print(res.content) #获取返回内容（自动解码）
print(res.encoding) #返回编码格式
print(res.cookies) #返回cookie
print(res.headers) #返回cookie
print(res.text) # 返回文本
