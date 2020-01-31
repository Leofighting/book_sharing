from flask import current_app
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Boolean, ForeignKey, String, desc, func

from app.models.base import Base, db
from app.spider.yushu_book import YuShuBook


class Gift(Base):
    """礼物"""
    id = Column(Integer, primary_key=True)
    user = relationship("User")
    uid = Column(Integer, ForeignKey("user.id"))
    isbn = Column(String(15), nullable=False)
    # 判断书籍是否已经赠送
    launched = Column(Boolean, default=False)

    @property
    def book(self):
        """通过isbn获取书籍信息"""
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

    @classmethod
    def recent(cls):
        """最近上传"""
        recent_gift = Gift.query.filter_by(
            launched=False).group_by(
            Gift.isbn).order_by(
            desc(Gift.create_time)).limit(
            current_app.config["RECENT_BOOK_COUNT"]).distinct().all()

        return recent_gift

    @classmethod
    def get_user_gifts(cls, uid):
        """获取用户礼物清单信息"""
        gifts = Gift.query.filter_by(
            uid=uid, launched=False).order_by(
            desc(Gift.create_time)).all()
        return gifts

    @classmethod
    def get_wish_counts(cls, isbn_list):
        """获取对应isbn 书籍的心愿数量"""
        from app.models.wish import Wish

        count_list = db.session.query(
            func.count(Wish.id), Wish.isbn).filter(
            Wish.launched == False,
            Wish.isbn.in_(isbn_list),
            Wish.status == 1).group_by(
            Wish.isbn).all()
        # 使用字典形式获取 func.count(Wish.id), Wish.isbn 的值
        count_list = [{"count": w[0], "isbn": w[1]} for w in count_list]
        return count_list

    def is_yourself_gift(self, uid):
        """判断是否自己的礼物"""
        return self.uid == uid
