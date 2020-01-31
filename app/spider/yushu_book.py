from flask import current_app

from app.libs.httper import HTTP


class YuShuBook(object):
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.total = 0
        self.books = []

    def search_by_isbn(self, isbn):
        """根据isbn搜索"""
        url = self.isbn_url.format(isbn)
        result = HTTP.get(url)
        self.__fill_single(result)

    def search_by_keyword(self, keyword, page=1):
        """根据关键字搜索"""
        url = self.keyword_url.format(keyword, current_app.config["PER_PAGE"],
                                      self.__calculate_start(page))
        result = HTTP.get(url)
        self.__fill_collection(result)

    @staticmethod
    def __calculate_start(page):
        """搜索开始值计算"""
        return (page - 1) * current_app.config["PER_PAGE"]

    def __fill_single(self, data):
        """收集单条书籍数据"""
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_collection(self, data):
        """收集书籍数据的集合"""
        self.total = data["total"]
        self.books = data["books"]

    @property
    def first(self):
        return self.books[0] if self.total >= 1 else None
