from bs4 import BeautifulSoup
from urllib import request
from urllib.request import urlretrieve
import uuid
import re

import uuid
import DBUtils


def insertProduct():
    sql = "select * from category c where c.pre_id in (select cate_id from category where pre_id = 0)"
    params = ()
    cursor = DBUtils.select(sql, params)
    for row in cursor.fetchall():
        url = row[4]
        cate_id = row[1]
        soup = BeautifulSoup(request.urlopen(
            url).read().decode("utf8"), "html.parser")
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
                price = prices[i]
                params = (cate_id, names[i], price[price.index("¥") + 1:], img)
                print(params)
                DBUtils.execute(sql, params)
# insertProduct()
# 从上面插入到库当中的商品数据，重新更新库，对商品图片进行下载


def download_image():
    sql = "select * from product"
    params = ()
    cursor = DBUtils.select(sql, params)
    for row in cursor.fetchall():
        url = str(row[4])
        # url = "http://bfs.biyao.com/group1/M00/30/2A/rBACVFq1-IGAEnGgAABx9dK4CuM199.jpg"
        url_new = url[-10:]
        extar_name = url_new[url_new.index("."):]
        img_name = str(uuid.uuid1())
        img_name = img_name.replace("-", "")
        sql = "update product set img_name = '%s' where id = '%s'"
        new_name = img_name+extar_name
        params = (new_name,row[0])
        imageLocation="E:/python_work/biyao_product_img/"+new_name     # 图片保存的地址，这里uuid.jpg 
        urlretrieve(url,imageLocation)     # 下载图片   
        DBUtils.execute(sql,params)
        print(new_name)


download_image()
