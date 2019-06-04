import json

d = {
    "a": 123,
    "b": "中文",
    "c": None,
    "d": True,
    "e": False,
    "f": ("aa", 123),
    "g": {
        "aaa": "ddd",
        "ccc": "ccc"
    }
}

# print(type(d))
print("python里的字典：%s" % d)

# 字典转json数据
dj = json.dumps(d)
print("转为json数据：%s" % dj)

# json数据转字典
js_dic = json.loads(dj)
print(type(js_dic))
print("json转字典: %s" % js_dic)
