import requests

url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=11936238&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
response = requests.get(url)

print(response)
print(response.text)
