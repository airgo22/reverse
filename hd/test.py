import requests
import execjs 

with open('./test.js', 'r', encoding='utf-8') as f:
    js_code = f.read()
ctx = execjs.compile(js_code)



headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "C-GATEWAY-QUERY-ENCRYPT": "1",
    "Connection": "keep-alive",
    "Referer": "https://credit.hd.gov.cn/xyxxgs/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Chromium\";v=\"142\", \"Google Chrome\";v=\"142\", \"Not_A Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "x-gateway-body": "blob"
}
cookies = {
    "_gscu_2016493642": "61468519xgz8bv10",
    "_gscbrs_2016493642": "1",
    "_gscs_2016493642": "63432368zm95wb40|pv:1"
}
url = "https://credit.hd.gov.cn/zx_website/website/sgs/xzxkfr"
params = ctx.call("get_payload" , 1) 
response = requests.get(url, headers=headers, cookies=cookies, params=params)

decoded_data = ctx.call("decode_data", list(response.content))
print(decoded_data)