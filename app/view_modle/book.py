class BookViewModel:
    """单本书籍数据"""
    def __init__(self, book):
        self.title = book["title"]
        self.publisher = book["publisher"]
        self.author = "、".join(book["author"])
        self.image = book["image"]
        self.price = "￥" + book["price"] if book["price"] else book["price"]
        self.summary = book["summary"]
        self.pages = book["pages"]
        self.isbn = book["isbn"]
        self.pubdate = book["pubdate"]
        self.binding = book["binding"]

    @property
    def intro(self):
        """书籍作者、出版社、价钱信息合并"""
        intros = filter(lambda x: True if x else False,
                        [self.author, self.publisher, self.price])
        return "/".join(intros)


class BookCollection:
    """书籍数据集合"""
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ""

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in yushu_book.books]


class _BookViewModel:
    """书籍视图模型"""
    @classmethod
    def package_single(cls, data, keyword):
        """单个书籍数据"""
        returned = {
            "book": [],
            "total": 0,
            "keyword": keyword
        }

        if data:
            returned["total"] = 1
            returned["book"] = [cls.__cut_book_data(data)]

        return returned

    @classmethod
    def package_collection(cls, data, keyword):
        """书籍数据集合"""
        returned = {
            "books": [],
            "total": 0,
            "keyword": keyword
        }

        if data:
            returned["total"] = data["total"]
            returned["books"] = [cls.__cut_book_data(book) for book in data["books"]]

        return returned

    @classmethod
    def __cut_book_data(cls, data):
        """获取书籍详情"""
        book = {
            "title": data["title"],
            "publisher": data["publisher"],
            "pages": data["pages"] or "",
            "author": "、".join(data["author"]),
            "price": data["price"],
            "summary": data["summary"] or "",
            "image": data["image"]
        }

        return book
