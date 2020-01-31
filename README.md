# Django-积分商城

- 基于 Flask 框架搭建的图书赠送平台，利用外部API获取书籍数据，使用MySQL储存内部数据信息，为前端提供方便实用的 Web 后端处理接口。



## 配置及运行

secure.py 文件中，配置数据库相关数据：

```python
SQLALCHEMY_DATABASE_URI = "mysql+cymysql://root:数据库密码@localhost:3306/数据库名称"
```

导入数据库数据文件：fisher_new.sql

邮箱配置

```python
MAIL_SERVER = "smtp.qq.com"
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TSL = False
# 邮箱用户名
MAIL_USERNAME = "你的qq邮箱用户名"
# 邮箱授权码，注意不是邮箱密码
MAIL_PASSWORD = "QQ邮箱设置中的授权码"
```

## 应用功能

用户注册/登录/忘记密码、书籍搜索/浏览详情/收藏、交易发起/拒绝/撤销/邮件通知/地址信息填写等；



## 数据处理

数据处理：使用 ORM 框架--SQLAlchemy 建立数据模型，结合 WTForms 组件与 MySQL 数据库完成数据的校验与存储；



## 整体框架及流程

![image](https://github.com/Leofighting/book_sharing/blob/master/GitHub_file/fisher.png)

## 功能页面展示

- 首页
![image](https://github.com/Leofighting/book_sharing/blob/master/GitHub_file/01.gif)

- 注册--登录--忘记密码
![image](https://github.com/Leofighting/book_sharing/blob/master/GitHub_file/02.gif)

## 项目实操收获

- 掌握 Flask 框架基本开发流程
- 使用蓝图实现项目的模块化
- 了解多线程编程，并实现邮件功能的多线程异步处理

## Requirements

```python
cymysql=0.9.14
Flask=1.1.1
Flask-Login=0.4.1
Flask-Mail=0.9.1
Flask-SQLAlchemy=2.4.1
Jinja2=2.10.3
requests=2.22.0
SQLAlchemy=1.3.11
urllib3=1.25.7
Werkzeug=0.16.0
WTForms=2.2.1
```



## 关于项目

学习来源：慕课网
