# 按需导入
from lxml import etree

text = '''
<div>
        <ul>
            <li class="item-0"><a href="link1.html">first item</a></li>
            <li class="item-1"><a href="link2.html">second item</a></li>
            <li class="item-inactive"><a href="link3.html">third item</a></li>
            <li class="item-1"><a href="link4.html">fourth item</a></li>
            <li class="item0"><a href="link5.html">fifth item</a> # 注意，此处缺少一个</li>闭合标签
        </ul>
    </div>
'''

html = etree.HTML(text)
# 补全html文档内容
# print(etree.tostring(html))

# 提取数据 /html //标签
# result = html.xpath('//li/@class')
# result = html.xpath('//li[@class="item-inactive"]')

# result = html.xpath('//li/a/text()')
# result = html.xpath('//li/a[text()="first item"]')
# result = html.xpath('//li/a[contains(text(),"item")]')
result = html.xpath('//li[contains(@class,"item-")]')
print(result)