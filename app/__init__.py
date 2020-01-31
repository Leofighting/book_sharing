from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail

from app.models.base import db

login_manager = LoginManager()
mail = Mail()


def creat_app():
    """创建 app"""
    app = Flask(__name__)
    # 配置文件相关
    app.config.from_object("app.secure")
    app.config.from_object("app.setting")
    # 注册蓝图
    register_blueprint(app)
    # 注册SQLAlchemy
    db.init_app(app)
    # 创建数据表
    with app.app_context():
        db.create_all()

    # 登陆相关
    login_manager.init_app(app)
    login_manager.login_view = "web.login"
    login_manager.login_message = "请先登录或注册"
    # 邮件相关
    mail.init_app(app)

    return app


def register_blueprint(app):
    """注册蓝图"""
    from app.web.book import web
    app.register_blueprint(web)
