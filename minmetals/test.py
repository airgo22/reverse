import requests
import json
import execjs

with open("test.js", "r", encoding="utf-8") as f:
    js_code = f.read()
ctx = execjs.compile(js_code)

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "https://ec.minmetals.com.cn",
    "Referer": "https://ec.minmetals.com.cn/open/home/purchase-info",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Chromium\";v=\"142\", \"Google Chrome\";v=\"142\", \"Not_A Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\""
}
cookies = {
    "SUNWAY-ESCM-COOKIE": "026cf778-55fb-48f4-9728-50917453e1c0",
    "__jsluid_s": "d7c8a20ed02a6b3271e5f6a2debe52e4",
    "JSESSIONID": "0921F04B6F06ACC22B0C9F2ED4545324"
}

url = "https://ec.minmetals.com.cn/open/homepage/public"
key = requests.post(url, headers=headers, cookies=cookies).text 

param = ctx.call("get_param", key , 1)
url = "https://ec.minmetals.com.cn/open/homepage/zbs/by-lx-page"
data = {
    "param": param,
    }
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, cookies=cookies, data=data)

print(response.text)
print(response)