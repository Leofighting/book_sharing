from threading import Thread

from flask import current_app, render_template
from flask_mail import Message

from app import mail


def send_async_email(app, msg):
    """异步发送邮件"""
    with app.app_context():
        try:
            mail.send(msg)
        except:
            print("邮件发送失败")


def send_mail(to, subject, template, **kwargs):
    """发送邮件"""
    msg = Message("[鱼书]" + " " + subject,
                  sender=current_app.config["MAIL_USERNAME"],
                  recipients=[to])
    msg.html = render_template(template, **kwargs)
    app = current_app._get_current_object()

    # 开启线程
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
