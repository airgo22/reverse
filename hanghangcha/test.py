import requests
import execjs 

with open('./test.js' , '+r') as f:
    js = f.read()
ctx = execjs.compile(js)


# cookie 可以下一次请求获取上一次的set_cookie 
# 和讲的不太一样
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Auth-Plus;": "",
    "Client-Encrypt": "v1.1",
    "Connection": "keep-alive",
    "Origin": "https://www.hanghangcha.com",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "clientInfo": "web",
    "clientVersion": "1.0.6",
    "currentHref": "https://www.hanghangcha.com/hhcreport",
    "sec-ch-ua": "\"Chromium\";v=\"142\", \"Google Chrome\";v=\"142\", \"Not_A Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\""
}
cookies = {
    "Hm_lvt_1521e0fb49013136e79181f2888214a7": "1763439797",
    "Hm_lpvt_1521e0fb49013136e79181f2888214a7": "1763439797",
    "HMACCOUNT": "6F29F6E82BEDB687",
    "JSESSIONID": "1D77493FEC3AE87CD45D983066617837",
    "WX_OPEN": "oN8HU1tc/0nco6MljGtxDKvtLKFxVwX6RvBIiEAGQwlgTWY+ngBx6qHKwk58b5IEyfaDCp7qPpZ0uEfQ6h//jpblK1lM8kGYeqVqIJvocfNTw5UFKFnlrAPV6ZbBwuMr",
    "_ACCOUNT_": "ZDI5M2MyYzQzNWQ4NDdlMzhmM2E1MzA5YTFmZjUxYzElNDAlNDBtb2JpbGU6MTc2NDY0OTY5MDQwMzo3ZTA5NWFkZTViZjU1Y2UwZjE5ZGUyNTUyMDc0YzNiOQ"
}
url = "https://api.hanghangcha.com/hhc/member/industry/getReportList"
params = {
    "filter": "{\"reportType\":null,\"limit\":10,\"skip\":20}"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

decoded_data = ctx.call("decode_data", response.json()['data'])
print(decoded_data)