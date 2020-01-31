from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Boolean, ForeignKey, String, desc, func

from app.models.base import Base, db
from app.spider.yushu_book import YuShuBook


class Wish(Base):
    """心愿清单"""
    id = Column(Integer, primary_key=True)
    user = relationship("User")
    uid = Column(Integer, ForeignKey("user.id"))
    isbn = Column(String(15), nullable=False)
    # 判断书籍是否已经赠送
    launched = Column(Boolean, default=False)

    @classmethod
    def get_user_wishes(cls, uid):
        """获取用户心愿清单信息"""
        wishes = Wish.query.filter_by(
            uid=uid, launched=False).order_by(
            desc(Wish.create_time)).all()
        return wishes

    @classmethod
    def get_gifts_counts(cls, isbn_list):
        """获取对应isbn 书籍的赠送数量"""
        from app.models.gift import Gift

        count_list = db.session.query(
            func.count(Gift.id), Gift.isbn).filter(
            Gift.launched == False,
            Gift.isbn.in_(isbn_list),
            Gift.status == 1).group_by(
            Gift.isbn).all()
        # 使用字典形式获取 func.count(Gift.id), Gift.isbn 的值
        count_list = [{"count": w[0], "isbn": w[1]} for w in count_list]
        return count_list

    @property
    def book(self):
        """通过isbn获取书籍信息"""
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first
