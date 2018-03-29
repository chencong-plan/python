# 分类实体
class Category(object):
    def __init__(self, id, name, url):
        self.id = id
        self.name = name
        self.url = url

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_url(self, url):
        self.url = url

    def get_url(self):
        return self.url
