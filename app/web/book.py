from flask import request, flash, render_template
from flask_login import current_user

from app.forms.book import SearchForm
from app.models.gift import Gift
from app.models.wish import Wish
from app.view_modle.book import BookViewModel, BookCollection
from app.view_modle.trade import TradInfo
from app.web import web
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook


@web.route("/book/search")
def search():
    """书籍搜索"""
    # 通过 form 验证参数q, page
    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        # 通过 form 获取 q, page
        q = form.q.data.strip()
        page = form.page.data
        # 判断用户输入的是 关键字 或者 isbn编码
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == "isbn":
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book, q)
    else:
        flash("搜索的关键字不符合要求，请重新输入")

    return render_template("search_result.html", books=books)


@web.route("/book/<isbn>/detail")
def book_detail(isbn):
    """书本详情"""

    # 取书籍的详情数据
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)

    # 判断是否在赠送清单或心愿清单中
    has_in_gifts = current_user.is_authenticated and current_user.has_in_gifts(isbn)
    has_in_wishes = current_user.is_authenticated and current_user.has_in_wishes(isbn)
    # 赠送人列表、索要人列表
    trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
    trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()

    trade_wishes_model = TradInfo(trade_wishes)
    trade_gifts_model = TradInfo(trade_gifts)

    return render_template("book_detail.html",
                           book=book,
                           wishes=trade_wishes_model,
                           gifts=trade_gifts_model,
                           has_in_gifts=has_in_gifts,
                           has_in_wishes=has_in_wishes,
                           )
