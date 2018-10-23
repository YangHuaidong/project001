# encoding=utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import not_, or_, and_

# 0.创建系统配置类
class Config(object):
    """项目配置信息"""
    DEBUG = True
    # mysql数据库连接配置
    # 格式:mysql://账号:密码@ip地址:端口号/数据库名称
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/test19'
    # 跟踪数据库修改操作
    SQLALCHEMY_TRACK_MODIFICATIONS = True


# 1.创建app对象
app = Flask(__name__)
# 将配置信息关联到app中
app.config.from_object(Config)


# 2.创建数据库对象
db = SQLAlchemy(app)


# 3.使用自定义模型累的方法创建数据库的表,继承:db.Model
class Role(db.Model):
    """角色表"""
    # 使用__tablename__自定义表名称,如果不设置默认值是类名的小写role
    __tablename__ = 'roles'
    # id字段 db.Integer:32位的整型数据 primary_key=True:
    # 设置该字段为主键
    id = db.Column(db.Integer, primary_key=True)
    # name字段 db.String(128):128位的字符串类型
    # unique=True:设置字段的唯一性
    name = db.Column(db.String(128), unique=True)
    """
        定义关系字段 该字段并不是数据库一列，在数据库并不存在，
        只是在flask代码层面方便我们查询而定义的字段

        role = Role()
        role.users : 该角色下面有那些用户

        user = User()
        user.role ：该用户属于那种角色

        backref: 反向引用，给User对象使用
    """
    users = db.relationship("User", backref="role")

    def __repr__(self):
        """
        自定义格式化输出
        没有重写该方法
        role = Role()   print(role) --->object对象

        重写该方法:
        role = Role() print(role) ---->"Role: xx xx"
        """
        return "Role: %s  %s " % (self.id, self.name)


class User(db.Model):
    """用户表  多"""

    __tablename__ = 'user'

    # id字段
    id = db.Column(db.Integer, primary_key=True)
    # name字段
    name = db.Column(db.String(128), unique=True)

    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))
    # 创建外键
    # "roles.id" --> 数据库层面的理解 roles表的id作为外键关联起来
    # Role.id -->面向对象层面理解  Role类的id属性作为外键关联起来
    role_id = db.Column(db.Integer, db.ForeignKey(Role.id))

    def __repr__(self):
        """自定义格式输出"""
        return "User: %s  %s  %s  %s " % (self.id, self.name, self.email,self.password)


@app.route('/')
def index():
    return "hello world "


if __name__ == '__main__':
    # 删除数据库所有表
    db.drop_all()
    # 创建所有表
    db.create_all()

    ro1 = Role(name='admin')
    db.session.add(ro1)
    db.session.commit()
    # 再次插入一条数据
    ro2 = Role(name='user')
    db.session.add(ro2)
    db.session.commit()

    us1 = User(name='wang', email='wang@163.com', password='123456', role_id=ro1.id)
    us2 = User(name='zhang', email='zhang@189.com', password='201512', role_id=ro2.id)
    us3 = User(name='chen', email='chen@126.com', password='987654', role_id=ro2.id)
    us4 = User(name='zhou', email='zhou@163.com', password='456789', role_id=ro1.id)
    us5 = User(name='tang', email='tang@itheima.com', password='158104', role_id=ro2.id)
    us6 = User(name='wu', email='wu@gmail.com', password='5623514', role_id=ro2.id)
    us7 = User(name='qian', email='qian@gmail.com', password='1543567', role_id=ro1.id)
    us8 = User(name='liu', email='liu@itheima.com', password='867322', role_id=ro1.id)
    us9 = User(name='li', email='li@163.com', password='4526342', role_id=ro2.id)
    us10 = User(name='sun', email='sun@163.com', password='235523', role_id=ro2.id)
    db.session.add_all([us1, us2, us3, us4, us5, us6, us7, us8, us9, us10])
    db.session.commit()
    app.run(debug=True)

    """
    查询所有用户数据
    查询有多少个用户
    查询第1个用户
    查询id为4的用户[3种方式]
    查询名字结尾字符为g的所有数据[开始/包含]
    查询名字不等于wang的所有数据[2种方式]
    查询名字和邮箱都以 li 开头的所有数据[2种方式]
    查询password是 `123456` 或者 `email` 以 `itheima.com` 结尾的所有数据
    查询id为 [1, 3, 5, 7, 9] 的用户列表
    查询name为liu的角色数据
    查询所有用户数据，并以邮箱排序
    每页3个，查询第2页的数据
    """
