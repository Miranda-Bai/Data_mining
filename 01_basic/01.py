import requests

# 模拟构造headers请求头信息
headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
}

# 通过requests模拟发送网络请求
r = requests.get("https://www.douban.com", headers=headers)
print("r: ", r)
