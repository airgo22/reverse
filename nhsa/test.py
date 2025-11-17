import requests
import json
import execjs

with open("./test.js", "r", encoding="utf-8") as f:
    js_code = f.read()
ctx = execjs.compile(js_code)
payload = ctx.call("get_payload", 1)


headers = {
    "Accept": "application/json",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "https://fuwu.nhsa.gov.cn",
    "Referer": "https://fuwu.nhsa.gov.cn/nationalHallSt/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
    # "X-Tingyun": "c=B|4Nl_NnGbjwY;x=548a9d21b8ea44fe",
    "channel": "web",
    "contentType": "application/x-www-form-urlencoded",
    "sec-ch-ua": "\"Chromium\";v=\"142\", \"Google Chrome\";v=\"142\", \"Not_A Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "x-tif-nonce": payload['headers']['x-tif-nonce'],
    "x-tif-paasid": "undefined",
    "x-tif-signature": payload['headers']['x-tif-signature'],
    "x-tif-timestamp": str(payload['headers']['x-tif-timestamp'])
}
cookies = {
    "amap_local": "120000",
    "yb_header_active": "-1",
    "acw_tc": "276aeddb17633648204795001e739c0f24758962600d82ecf214960792ae6b"
}
url = "https://fuwu.nhsa.gov.cn/ebus/fuwu/api/nthl/api/CommQuery/queryWmTcmpatInfoBFromEs"
data = payload['data']
# data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, cookies=cookies, data=data)
decoded_data = ctx.call("decode_data", response.json())

print(decoded_data)