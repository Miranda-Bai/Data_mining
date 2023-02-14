import requests

url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'

# post请求才有data数据，即form表单数据
data = {
    'log': 'miranda',
    'pwd': '1233434',
    'wp-submit': '登录',
    'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
    'testcookie': '1'
}

response = requests.post(url, data=data)

response.encoding = 'utf-8'
print(response.text)
