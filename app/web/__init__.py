from flask import Blueprint, render_template

web = Blueprint("web", __name__)


@web.app_errorhandler(404)
def not_found(e):
    """返回 404 页面"""
    return render_template("404.html"), 404


@web.app_errorhandler(500)
def not_found(e):
    """返回 500 页面"""
    return render_template("500.html"), 500


from app.web import book
from app.web import auth
from app.web import drift
from app.web import gift
from app.web import main
from app.web import wish
