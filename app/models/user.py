from math import floor

from flask import current_app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from sqlalchemy import Column, Integer, String, Boolean, Float

from app import login_manager
from app.libs.enums import PendingStatus
from app.libs.helper import is_isbn_or_key
from app.models.base import Base, db
from app.models.drift import Drift
from app.models.gift import Gift
from app.models.wish import Wish
from app.spider.yushu_book import YuShuBook


class User(UserMixin, Base):
    """用户"""
    id = Column(Integer, primary_key=True)
    _password = Column("password", String(128), nullable=False)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        """密码加密"""
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        """核对密码"""
        if not self._password:
            return False
        return check_password_hash(self._password, raw)

    def can_save_to_list(self, isbn):
        """"判断该 isbn 编号的书籍能否上传"""
        if is_isbn_or_key(isbn) != "isbn":
            return False

        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(isbn)

        if not yushu_book.first:
            return False

        # 书籍既不在赠送清单，也不再心愿清单中才能添加
        gifting = Gift.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()
        wishing = Wish.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()

        return not gifting and not wishing

    def generate_token(self, expiration=6000):
        """生成 token"""
        s = Serializer(current_app.config["SECRET_KEY"], expires_in=expiration)
        result = s.dumps({"id": self.id}).decode("utf-8")
        return result

    @staticmethod
    def reset_password(token, new_password):
        """重置密码"""
        s = Serializer(current_app.config["SECRET_KEY"])
        try:
            data = s.loads(token.encode("utf-8"))
        except:
            return False

        uid = data.get("id")
        with db.auto_commit():
            user = User.query.get_or_404(uid)
            user.password = new_password
        return True

    def can_send_drift(self):
        """能够索要书籍"""
        if self.beans < 1:
            return False

        # 查询成功送出书籍的数量
        success_gifts_count = Gift.query.filter_by(
            uid=self.id,
            launched=True
        ).count()

        success_receive_count = Drift.query.filter_by(
            requester_id=self.id,
            pending=PendingStatus.SUCCESS
        ).count()

        return floor(success_receive_count / 2) <= floor(success_gifts_count)

    @property
    def summary(self):
        """用户简介信息"""
        return dict(
            nickname=self.nickname,
            beans=self.beans,
            email=self.email,
            send_receive=str(self.send_counter)+" / "+str(self.receive_counter)
        )

    def has_in_gifts(self, isbn):
        return Gift.query.filter_by(uid=self.id, isbn=isbn).first() is not None

    def has_in_wishes(self, isbn):
        return Wish.query.filter_by(uid=self.id, isbn=isbn).first() is not None


@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))
