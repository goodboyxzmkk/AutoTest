import requests

s = requests.session()
header = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"
}
# allow_redirects 禁止重定向
r1 = s.get("https://i.cnblogs.com/EditPosts.aspx?opt=1", verify=False, headers=header, allow_redirects=False)
print(r1.status_code)
print(r1.history)
for i in r1.history:
    print(i.url)
    # print()