from sqlalchemy import Column, Integer, String

from app.models.base import Base


class Book(Base):
    """书籍信息"""
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(20), default="无数据")
    # 装帧形式
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(10))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(1000))
    image = Column(String(50))

