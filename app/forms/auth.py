from wtforms import Form, StringField, PasswordField
from wtforms.validators import Length, DataRequired, Email, ValidationError, EqualTo

from app.models.user import User


class EmailForm(Form):
    """邮箱"""
    email = StringField(validators=[
        DataRequired(), Length(5, 64),
        Email(message="电子邮箱不符合规范")
    ])


class RegisterForm(EmailForm):
    """用户注册"""
    password = PasswordField(validators=[
        DataRequired(message="密码不能为空，请输入密码"),
        Length(6, 32)
    ])
    nickname = StringField(validators=[
        DataRequired(),
        Length(2, 10, message="昵称至少需要两个字符， 最多10个字符")
    ])

    @staticmethod
    def validate_email(field):
        """自定义邮箱校验"""
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("电子邮箱已被注册")

    @staticmethod
    def validate_nickname(field):
        """自定义昵称校验"""
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError("昵称已存在")


class LoginForm(EmailForm):
    """用户登陆"""
    password = PasswordField(validators=[
        DataRequired(message="密码不能为空，请输入密码"),
        Length(6, 32)
    ])


class ResetPasswordForm(Form):
    """重置密码"""
    password1 = PasswordField(validators=[
        DataRequired(),
        Length(6, 32, message="密码长度至少需要在 6-20 个支付之间"),
        EqualTo("password2", message="两次输入的密码不相同")
    ])
    password2 = PasswordField(validators=[
        DataRequired(), Length(6, 32)
    ])
