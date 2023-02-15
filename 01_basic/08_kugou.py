import requests

m_url='https://music.163.com/#/search/m/'
params={
    's':'大鱼'
}
header={
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

response = requests.get(m_url,params=params,headers=header)

print(response.text)