import urllib.request

# coding:utf-8
import re


def get_html(url):
    page = urllib.request.urlopen(url)
    html_code = page.read()
    html_code = html_code.decode('utf-8')  # python3这句代码
    return html_code


def get_image(html_code):
    reg = r'src="(.+?\.jpg)" alt='
    reg_img = re.compile(reg)
    img_list = reg_img.findall(html_code)
    x = 0
    for img in img_list:
        urllib.request.urlretrieve(img, '%s.jpg' % x)
        x += 1


print('-------网页图片抓取-------')
print('请输入url:')
url = input()
if url:
    pass
else:
    print('---没有地址输入正在使用默认地址---')
    url = 'http://www.biyao.com/classify/supplier.html?supplierId=130084'
print('----------正在获取网页---------')
html_code = get_html(url)
print('----------正在下载图片---------')
get_image(html_code)
print('-----------下载成功-----------')
