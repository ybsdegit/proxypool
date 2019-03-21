#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/22 0:08
# @Author  : Paulson
# @File    : demo.py
# @Software: PyCharm
# @define  : function
import json

import requests
from requests.exceptions import ConnectionError

PROXY_POOL_URL = 'http://localhost:5000/one'  # one proxy

PROXIES_POOL_URL = 'http://127.0.0.1:5000/all'  # all proxies


def get_proxy():
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            return response.json()
    except ConnectionError:
        return None

def test():
    proxy = get_proxy()['proxy']
    url = 'https://weixin.sogou.com/weixin?query=python&type=2&page=1'
    headers = {
        'Cookie': 'SUV=1547344793853119; SMYUV=1547344793854887; UM_distinctid=16844efd1034ab-0a1be8536d48a-b781636-1fa400-16844efd104204; CXID=5637462A2349CEE62D6F76AA18FF09AD; ad=HClhtZllll2tAipElllllVha6b7lllllnLLg0Zllll9lllllRZlll5@@@@@@@@@@; SUID=8F976D3B4B238B0A5C8B91BB0002B72F; IPLOC=CN1100; pgv_pvi=8364128256; pgv_si=s1505230848; ABTEST=0|1553084608|v1; SNUID=7B01FEA89397161722F5FFD993353858; weixinIndexVisited=1; sct=1; JSESSIONID=aaaD0UP5hNkqa4RQ9U-Lw; ppinf=5|1553086365|1554295965|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo1OTolRTUlODUlODMlRTUlQUUlOUQlRTYlQTMlQUUlRUYlQkMlODhQYXVsc29uJTIwV2llciVFRiVCQyU4OXxjcnQ6MTA6MTU1MzA4NjM2NXxyZWZuaWNrOjU5OiVFNSU4NSU4MyVFNSVBRSU5RCVFNiVBMyVBRSVFRiVCQyU4OFBhdWxzb24lMjBXaWVyJUVGJUJDJTg5fHVzZXJpZDo0NDpvOXQybHVCeW1jeXBjYXBVSjg4U2l6MUx6YXZ3QHdlaXhpbi5zb2h1LmNvbXw; pprdig=vmo-4_vS31dWkit52GXYNfr5d7VspV-gcfbJhb-dTfOkb9T7DxpGujrgoTJ_5ZgtIguTDlwcftF86zhWKjgIYgfjvl9qyZrh4yjhMSXYDRH0NWe4rGoBxRuY2siHHgaybghgxQo-s6Er2couIiHGJ50NNvwzbmfxPVHeurh3LbQ; sgid=14-39756811-AVySN513EIhUdTRZh2ibWXQk; ppmdig=1553086365000000133d76ef551230b4d4481bc7eb3066d5',
        'Host': 'weixin.sogou.com',
        'Referer': 'https://weixin.sogou.com/weixin?query=python&_sug_type_=&sut=1457&lkt=1%2C1553084639056%2C1553084639056&s_from=input&_sug_=y&type=2&sst0=1553084639158&page=11&ie=utf8&w=01019900&dr=1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    proxies = {
        'https': 'https://' + proxy
    }
    try:
        response = requests.get(url,allow_redirects=False,headers=headers,proxies=proxies,timeout=5)
        print(proxies)
        print(response.status_code)
    except ConnectionError as e:
        print('Error Occurred',e.args)

if __name__ == '__main__':

    while True:
        test()

    # s=json.loads(proxy)
    # print(proxy['proxy'])
