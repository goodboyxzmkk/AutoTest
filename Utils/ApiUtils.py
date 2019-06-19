import requests

from Common import ConfigManage

apiconfig = ConfigManage.get_configdic("apiConfig.yaml")


class api_utils():
    def __init__(self):
        self.url = apiconfig["apiURL"]["URL"]
        self.ss = requests.session()
        self.header = {
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"
        }

    def get_post(self, uri, body):
        url = self.url + uri
        respones = self.ss.post(url, headers=self.header, data=body, verify=False)
        return respones

    def get_get(self, uri, body=None):
        url = self.url + uri
        respones = self.ss.get(url, headers=self.header, data=body, verify=False)
        return respones
