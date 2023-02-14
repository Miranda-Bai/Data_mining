import requests

# 构建参数字典
kw = {
    'q': 'python'
}

# 模拟构造headers请求头信息
headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
}
# 通过requests模拟发送网络请求
response = requests.get("https://www.google.com/search", params=kw,headers=headers)

# print("response: ", response)
# 查看完整url地址
print(response.url)
# 查看响应头部字符编码
# print(response.encoding)  # ISO-8859-1

# 设置响应数据的编码
response.encoding = 'utf-8'
# response.tex返回Unicode格式的数据 response.content返回字节流数据
print( response.text)
# print(response.encoding) # utf-8
# print(response.content)



# 查看响应码
# print(response.status_code)
