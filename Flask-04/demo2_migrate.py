from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager

class Config(object):
    """显目配置类"""
    # 数据库链接配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/author_book"
    # 开启数据库跟踪操作
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 设置加密字符串
    SECRET_KEY = "SAKLDLASKJDLASDSAKNJDJK9U898AS8D8"

#1.创app对象
app = Flask(__name__)
app.config.from_object(Config)

#2.创建数据库对象
db = SQLAlchemy(app)

#3.创建迁移对象
migrate = Migrate(app,db)

#4.创建管理类
manager = Manager(app)

#5.通过管理类添加数据库迁移指令
#db 数据库迁移命令
manager.add_command("db",MigrateCommand)

"""
(必须掌握)
#第一次执行相当于:db.create_all()
#第一次数据库迁移初始化操作  产生一个migrations文件夹(只需要执行一次)
python3 demo2_migrate.py db init

#执行数据库迁移  生成一个对应版本  -m: 注释
(只要模型类的结构发生改变每次都需要执行)
python3 demo2_migrate.py db migrate -m "messge"

#执行数据库版本的升级  才会真正在数据库创建表
(只要模型类的结构发生改变每次都需要执行)
python3 demo2_migrate.py db upgrade

(会copy)
#查看历史版本
python3 demo2_migrate.py db history

#回到低版本
python3 demo2_migrate.py db downgrade 版本号

#回到高版本
python3 demo2_migrate.py db upgrade 版本号

"""

#3.创建模型类  默认是类名的小写作为表的名称:author
class Author(db.Model):
    """作者类   一的一方"""
    #id字段
    id = db.Column(db.Integer,primary_key=True)
    #name字段
    name = db.Column(db.String(64),unique=True)
    #添加邮箱字段
    email = db.Column(db.String(64),unique=True)
    #添加密码字段
    password = db.Column(db.String(64),unique=True)
    #定义关系字段为方便查询
    #author.books  该作者编写了那些书籍
    #book.author  该书籍属于哪个作者
    book = db.relationship("Book",backref="author")

    def __repr__(self):
        return "Author:  %s  %s  %s   %s " % (self.id , self.name,self.email,self.password)


class  Book(db.Model):
    """书籍类  多的一方"""
    #id字段
    id = db.Column(db.Integer,primary_key=True)
    #name字段
    name = db.Column(db.String(64),unique=True)
    #定义外键
    author_id = db.Column(db.Integer,db.ForeignKey(Author.id))

    def __repr__(self):
        return "Book: %s  %s  " % (self.id,self.name)



@app.route('/')
def index():
    return "hello world "




if __name__ == '__main__':

    # app.run(debug=True)
    #6.使用manager对象开启项目
    manager.run()
