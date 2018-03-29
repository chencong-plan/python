from bs4 import BeautifulSoup
from urllib import request
import re

import uuid

# 引入Category

# 引入DBUtils
import DBUtil


# 获得所有分类信息
def getCateList(html):
    soup = BeautifulSoup(html)
    # 获得分类信息
    categoryList = soup.find_all("div", class_="category-title")
    return categoryList


# 获得所有分类标题名称
def getCateNameList(categoryList):
    # 得到所有分类的li信息
    regex_p = re.compile("<p>(.*?)</p>")
    cateNameList = re.findall(regex_p, str(categoryList))
    # 从第二个取起，第一个为"精品"
    return cateNameList[1:]


# 得到每一个分类的id
def getCateIdList(categoryList):
    # 首先得到指定的每一个分类对应的url
    regex_a = re.compile('<a href="(.*?)" target="_blank">')
    urls = re.findall(regex_a, str(categoryList))
    ids = []
    for url in urls:
        id = url[url.index("=") + 1:]
        ids.append(id)
    return ids


def getCateUrlList(categoryList):
    # 首先得到指定的每一个分类对应的url
    regex_a = re.compile('<a href="(.*?)" target="_blank">')
    urls = re.findall(regex_a, str(categoryList))
    return urls


url = "http://www.biyao.com/home/index.html"
html = request.urlopen(url).read().decode("utf8")


def doPreCate(html):
    categoryList = getCateList(html)
    for i, id in enumerate(getCateIdList(categoryList)):
        names = getCateNameList(categoryList)
        urls = getCateUrlList(categoryList)
        sql = "INSERT INTO category(cate_id,name,url,pre_id) VALUES('%s','%s','%s','%s')"
        params = (id, names[i], urls[i], 0)
        DBUtil.execute(sql, params)
        print(params)


# 执行首页获取分类信息
# doPreCate(html)

def getChidCate(url):
    html = request.urlopen(url).read().decode("utf8")
    soup = BeautifulSoup(html)
    #  categoryList = soup.find_all("div",class_="category-title")
    category_list = soup.find_all("div", class_="cateBread")
    # <li class="123">太阳镜</li>
    regex = re.compile('<li class="(.*?)">(.*?)</li>')
    list = re.findall(regex, str(category_list))
    return list


# 获取到每一个分类下所有子分类
def doChildCate(html):
    categoryList = getCateList(html)
    urls = getCateUrlList(categoryList)
    for url in urls:
        id = url[url.index("=") + 1:]
        params = getChidCate(url)
        for t in params:
            sql = "INSERT INTO category(cate_id,name,url,pre_id) VALUES('%s','%s','%s','%s')"
            c_url = "http://www.biyao.com/classify/category.html?categoryId=" + t[0]
            params = (t[0], t[1], c_url, id)
            DBUtil.execute(sql, params)
        # print(params)


# doChildCate(html)
def doProductByCateId(html):
    categoryList = getCateList(html)
    urls = getCateUrlList(categoryList)
    for url in urls:
        ids = getChidCate(url)
        for temp in ids:
            link = "http://www.biyao.com/classify/category.html?categoryId=" + temp[0]
            # print(link, temp[1])
            insertProduct(link, temp[0])


def insertProduct(url, cate_id):
    html = request.urlopen(url).read().decode("utf8")
    soup = BeautifulSoup(html)
    li_list = soup.find_all("ul", class_="category-list clearfix")
    # <img src="http://bfs.biyao.com/group1/M00/15/7A/rBACW1lTTUiANnw6AACPlZY2vio534.jpg" alt=""/>
    regex_img = re.compile('<img alt="" src="(.*?)"/>')
    regex_name = re.compile('<dt>(.*?)</dt>')
    regex_price = re.compile('<dd>(.*?)</dd>')
    for li in li_list:
        imgs = re.findall(regex_img, str(li))
        names = re.findall(regex_name, str(li))
        prices = re.findall(regex_price, str(li))
        for i, img in enumerate(imgs):
            sql = "INSERT INTO product(cate_id,name,price,img_url) VALUES ('%s','%s','%s','%s')"
            price = prices[i];
            params = (cate_id, names[i], price[price.index("¥")+1:], img)
            print(params)
        # print(len(img), img)
        # print(len(name), name)
        # print(len(price), price)
        # print("======================================================")


doProductByCateId(html)
