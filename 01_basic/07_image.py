import requests
from lxml import etree

index_url = 'https://tieba.baidu.com/p/5475267611?red_tag=2548905466'

response = requests.get(index_url).text
# print(response)

selector = etree.HTML(response)
image_urls = selector.xpath('//img[@class="BDE_Image"]/@src')
# print(image_urls)

offset = 0
for img_url in image_urls:
    # 获取图片的原始内容
    img_content = requests.get(img_url).content
    with open('{}.jpg'.format(offset), 'wb') as f:
        f.write(img_content)
        offset += 1
