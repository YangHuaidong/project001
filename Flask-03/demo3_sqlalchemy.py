# encoding=utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


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

    # 创建外键
    # "roles.id" --> 数据库层面的理解 roles表的id作为外键关联起来
    # Role.id -->面向对象层面理解  Role类的id属性作为外键关联起来
    role_id = db.Column(db.Integer, db.ForeignKey(Role.id))

    def __repr__(self):
        """自定义格式输出"""
        return "User: %s  %s " % (self.id, self.name)


@app.route('/')
def index():
    return "hello world "


if __name__ == '__main__':
    # 删除数据库所有表
    db.drop_all()
    # 创建所有表
    db.create_all()

    app.run(debug=True)
