DEBUG = True

SQLALCHEMY_DATABASE_URI = "mysql+cymysql://root:数据库密码@localhost:3306/数据库名称"
SECRET_KEY = "123qweasdzxc"

# 邮件配置
MAIL_SERVER = "smtp.qq.com"
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TSL = False
# 邮箱用户名
MAIL_USERNAME = "你的qq邮箱用户名"
# 邮箱授权码，注意不是邮箱密码
MAIL_PASSWORD = "QQ邮箱设置中的授权码"
