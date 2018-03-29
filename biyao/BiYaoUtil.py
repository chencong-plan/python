from bs4 import BeautifulSoup
from urllib import request
import re

import uuid

# 引入Category

# 引入DBUtils
import DBUtil

url = "http://www.biyao.com/home/index.html"
html = request.urlopen(url).read().decode("utf8")


# 由于首页存在瀑布流，在这里将所有文件列举在index.html当中
# html = open("index.html",encoding='UTF-8').read()


# 获得所有分类信息,一级分类信息
def insertAllCateList(html):
    soup = BeautifulSoup(html, "html.parser").find("div", class_="banner")
    # 获得分类信息，应该从导航栏里面获取
    lis = soup.find_all("li", class_="nav-main")
    for li in lis:
        li_soup = BeautifulSoup(str(li), "html.parser")
        p_content = li_soup.find_all('p')[0]
        regex = re.compile('<a href="(.*?)">(.*?)</a>')
        a = str(p_content).strip().replace("\n", "").replace("\r", "").replace("\t", "")
        list = re.findall(regex, a)
        # 往库当中插入
        for temp in list:
            sql = "INSERT INTO category(cate_id,pre_id,name,url) VALUES('%s','%s','%s','%s')"
            url = temp[0]
            cate_id = url[url.index("=") + 1:]
            pre_id = 0
            name = temp[1]
            params = (cate_id, pre_id, name, url)
            DBUtil.execute(sql, params)


# insertAllCateList(html)

# 获得所有以及分类url
def getAllCateUrl(html):
    soup = BeautifulSoup(html, "html.parser").find("div", class_="banner")
    # 获得分类信息，应该从导航栏里面获取
    lis = soup.find_all("li", class_="nav-main")
    result = []
    for li in lis:
        li_soup = BeautifulSoup(str(li), "html.parser")
        p_content = li_soup.find_all('p')[0]
        regex = re.compile('<a href="(.*?)">(.*?)</a>')
        a = str(p_content).strip().replace("\n", "").replace("\r", "").replace("\t", "")
        list = re.findall(regex, a)
        # 往库当中插入
        for temp in list:
            result.append(temp[0])
    return result


# print(getAllCateUrl(html))


# 通过一级分类获取二级分类信息
# ('279', ('280', '男士上装'), ('295', '男士外套'))
def getAllChirdCate(html):
    urls = getAllCateUrl(html)
    result = []
    for url in urls:
        content = request.urlopen(url).read().decode("utf8")
        soup = BeautifulSoup(content, "html.parser")
        #  categoryList = soup.find_all("div",class_="category-title")
        category_list = soup.find_all("div", class_="cateBread")
        # <li class="123">太阳镜</li>
        regex = re.compile('<li class="(.*?)">(.*?)</li>')
        list = re.findall(regex, str(category_list))
        pre_id = url[url.index("=") + 1:]
        temp = (pre_id, list)
        result.append(temp)
    return result


# print(getAllChirdCate(html))

# 通过url获得分类
def getAllChirdCateByUrl(url):
    result = []
    content = request.urlopen(url).read().decode("utf8")
    soup = BeautifulSoup(content, "html.parser")
    #  categoryList = soup.find_all("div",class_="category-title")
    category_list = soup.find_all("div", class_="cateBread")
    # <li class="123">太阳镜</li>
    regex = re.compile('<li class="(.*?)">(.*?)</li>')
    list = re.findall(regex, str(category_list))
    pre_id = url[url.index("=") + 1:]
    temp = (pre_id, list)
    result.append(temp)
    return result


# url = "http://www.biyao.com/classify/category.html?categoryId=280"
# print(getAllChirdCateByUrl(url))


# 往数据库当中插入所有二级分类信息
def insertChirdCate(html):
    # list = getAllChirdCate(html)
    for cate in list:
        # ('279', [('280', '男士上装'), ('295', '男士外套'), ('289', '男士下装')])
        sql = "INSERT INTO category(cate_id,name,url,pre_id) VALUES('%s','%s','%s','%s')"
        pre_id = cate[0]
        cate_list = cate[1:]
        for chird_cate in cate_list[0]:
            cate_id = str(chird_cate[0])
            name = chird_cate[1]
            url = "http://www.biyao.com/classify/category.html?categoryId=" + cate_id
            params = (cate_id, name, url, pre_id)
            print(params)
            DBUtil.execute(sql, params)


def insertChirdCateByUrl(url):
    list = getAllChirdCateByUrl(url)
    for cate in list:
        # ('279', [('280', '男士上装'), ('295', '男士外套'), ('289', '男士下装')])
        sql = "INSERT INTO category(cate_id,name,url,pre_id) VALUES('%s','%s','%s','%s')"
        pre_id = cate[0]
        cate_list = cate[1:]
        for chird_cate in cate_list[0]:
            cate_id = str(chird_cate[0])
            name = chird_cate[1]
            url = "http://www.biyao.com/classify/category.html?categoryId=" + cate_id
            params = (cate_id, name, url, pre_id)
            print(params)
            DBUtil.execute(sql, params)


# url = "http://www.biyao.com/classify/category.html?categoryId=280"
urls = ["http://www.biyao.com/classify/category.html?categoryId=295",
        "http://www.biyao.com/classify/category.html?categoryId=289",
        "http://www.biyao.com/classify/category.html?categoryId=300",
        "http://www.biyao.com/classify/category.html?categoryId=299",
        "http://www.biyao.com/classify/category.html?categoryId=301",
        "http://www.biyao.com/classify/category.html?categoryId=340",
        "http://www.biyao.com/classify/category.html?categoryId=342",
        "http://www.biyao.com/classify/category.html?categoryId=38",
        "http://www.biyao.com/classify/category.html?categoryId=37",
        "http://www.biyao.com/classify/category.html?categoryId=320",
        "http://www.biyao.com/classify/category.html?categoryId=191",
        "http://www.biyao.com/classify/category.html?categoryId=40",
        "http://www.biyao.com/classify/category.html?categoryId=40",
        "http://www.biyao.com/classify/category.html?categoryId=216",
        "http://www.biyao.com/classify/category.html?categoryId=245",
        "http://www.biyao.com/classify/category.html?categoryId=154",
        "http://www.biyao.com/classify/category.html?categoryId=209",
        "http://www.biyao.com/classify/category.html?categoryId=381",
        "http://www.biyao.com/classify/category.html?categoryId=382",
        "http://www.biyao.com/classify/category.html?categoryId=356",
        "http://www.biyao.com/classify/category.html?categoryId=357",
        "http://www.biyao.com/classify/category.html?categoryId=392",
        "http://www.biyao.com/classify/category.html?categoryId=410",
        "http://www.biyao.com/classify/category.html?categoryId=394",
        "http://www.biyao.com/classify/category.html?categoryId=395",
        "http://www.biyao.com/classify/category.html?categoryId=393",
        "http://www.biyao.com/classify/category.html?categoryId=120",
        "http://www.biyao.com/classify/category.html?categoryId=477",
        "http://www.biyao.com/classify/category.html?categoryId=214",
        "http://www.biyao.com/classify/category.html?categoryId=181",
        "http://www.biyao.com/classify/category.html?categoryId=413",
        "http://www.biyao.com/classify/category.html?categoryId=454",
        "http://www.biyao.com/classify/category.html?categoryId=456",
        "http://www.biyao.com/classify/category.html?categoryId=482",
        "http://www.biyao.com/classify/category.html?categoryId=467",
        "http://www.biyao.com/classify/category.html?categoryId=187",
        "http://www.biyao.com/classify/category.html?categoryId=186",
        "http://www.biyao.com/classify/category.html?categoryId=371",
        "http://www.biyao.com/classify/category.html?categoryId=370",
        "http://www.biyao.com/classify/category.html?categoryId=372",
        "http://www.biyao.com/classify/category.html?categoryId=14",
        "http://www.biyao.com/classify/category.html?categoryId=15",
        "http://www.biyao.com/classify/category.html?categoryId=13",
        "http://www.biyao.com/classify/category.html?categoryId=16",
        "http://www.biyao.com/classify/category.html?categoryId=234"]
for url in urls:
    insertChirdCateByUrl(url)


#
# insertChirdCate(html)


# insertChirdCate(html)


# print(getAllChirdCate(html))


# 查看所有子分类信息
# getAllChirdCate(html)


# 获得所有分类信息
def getCateList(html):
    soup = BeautifulSoup(html, "html.parser")
    # 获得分类信息
    categoryList = soup.find_all("div", class_="category-title")
    print(categoryList)
    return categoryList


# getCateList(html)


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


def getChirdCate(url):
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
        params = getChirdCate(url)
        for t in params:
            sql = "INSERT INTO category(cate_id,name,url,pre_id) VALUES('%s','%s','%s','%s')"
            c_url = "http://www.biyao.com/classify/category.html?categoryId=" + t[0]
            params = (t[0], t[1], c_url, id)
            DBUtil.execute(sql, params)
        # print(params)


# 获得子分类信息
# doChildCate(html)


def doProductByCateId(html):
    categoryList = getCateList(html)
    urls = getCateUrlList(categoryList)
    for url in urls:
        ids = getChirdCate(url)
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
            params = (cate_id, names[i], price[price.index("¥") + 1:], img)
            print(params)
            DBUtil.execute(sql, params)
        # print(len(img), img)
        # print(len(name), name)
        # print(len(price), price)
        # print("======================================================")

# 按照分类下载商品信息入库
# doProductByCateId(html)
