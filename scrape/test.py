import requests
import pywasm
import time




headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Connection": "keep-alive",
    "Referer": "https://spa14.scrape.center/page/4",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Chromium\";v=\"142\", \"Google Chrome\";v=\"142\", \"Not_A Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\""
}
url = "https://spa14.scrape.center/api/movie/"

page = 1 
offset = (page-1) * 10
vm = pywasm.load('./Wasm.wasm')
sign = vm.exec('encrypt', [offset , round(time.time())])

params = {
    "limit": "10",
    "offset": offset,
    "sign": sign
}
response = requests.get(url, headers=headers, params=params)

print(response.text)
print(response)