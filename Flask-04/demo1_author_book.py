#-*-coding:utf8-*-
from flask import Flask, render_template, redirect, url_for
from flask import request, flash
from flask_sqlalchemy import SQLAlchemy


class Config(object):
    """项目配置类"""
    # 数据库链接配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/author_book"
    # 开启数据库跟踪操作
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 设置加密字符串
    SECRET_KEY = "SAKLDLASKJDLASDSAKNJDJK9U898AS8D8"


# 1.创建app对象
app = Flask(__name__)
app.config.from_object(Config)

# 2.创建数据库对象
db = SQLAlchemy(app)


# 3.创建模型类 默认是类名的小写作为表的名称：author
class Author(db.Model):
    """作者类  一的一方"""

    # id字段
    id = db.Column(db.Integer, primary_key=True)
    # name字段
    name = db.Column(db.String(64), unique=True)
    # 定义关系字段方便查询
    # author.books 该作者编写了那些书籍
    # book.author  该书籍属于哪个作者
    books = db.relationship("Book", backref='author')

    def __repr__(self):
        return "Author: %s  %s " % (self.id, self.name)


class Book(db.Model):
    """书籍类 多的一方"""
    # id字段
    id = db.Column(db.Integer, primary_key=True)
    # name字段
    name = db.Column(db.String(64), unique=True)
    # 定义外键
    author_id = db.Column(db.Integer, db.ForeignKey(Author.id))

    def __repr__(self):
        return "Book: %s  %s " % (self.id, self.name)


@app.route('/', methods=['POST', 'GET'])
def index():
    # 添加书籍,作者
    if request.method == 'POST':
        # 1.获取参数
        author_name = request.form.get("author")
        book_name = request.form.get("book")
        # 2.校验参数
        if not all([author_name, book_name]):
            # 通过flash函数能将消息添加到一个消息队列
            flash("参数不足")
            return
        # 3.逻辑处理
        # 3.1 查询作者
        author = Author.query.filter(Author.name == author_name).first()
        # 3.2 作者不存在
        if not author:
            # 3.2.1 添加作者 添加书籍 将书籍关联到作者身上
            # 创建作者对象
            author = Author(name=author_name)
            db.session.add(author)
            db.session.commit()
            # 创建书籍 注意：必须先将作者添加到数据库，author.id才有值
            book = Book(name=book_name, author_id=author.id)
            db.session.add(book)
            db.session.commit()
        # 3.3 作者存在
        else:
            # 3.3.1 查询书籍
            book = Book.query.filter(Book.name == book_name).first()
            # 3.3.2 书籍存在，提示不能重复添加
            if book:
                flash("书籍已经存在，不能重复添加")
            # 3.3.3 书籍不存在 添加书籍
            else:
                book = Book(name=book_name, author_id=author.id)
                db.session.add(book)

                db.session.commit()


    # 1.查询所有作者
    authors = Author.query.all()
    # 2.查询所有书籍 因为作者对象有books属性，直接能获取对应作者的所有书籍author.books
    return render_template("author_book.html", authors=authors)

"""
 127.0.0.1:5000/delete_author/1 (url路径)--->  <user_id>
 127.0.0.1:5000/delete_author?id=1 (url路径+参数) ---> request.args.get('id')
"""


# 删除作者
@app.route('/delete_author/<author_id>')
def delete_author(author_id):
    # 1.查询作者是否存在
    try:
        author = Author.query.get(author_id)
    except Exception as e:
        flash(e)

    # 2.作者不存在
    if not author:
        flash("作者不存在不允许删除")
        return
    else:
        try:
            # 1.删除书籍
            # 获取到当前作者的所有书籍
            books = author.books
            for book in books:
                db.session.delete(book)
            # 2.删除作者
            db.session.delete(author)
            db.session.commit()
        except Exception as e:
            flash(e)
            # 回顾
            db.session.rollback()

    # 注意：以上操作只是影响到数据库的数据变化，如果界面需要刷新，需要重新查询数据库
    return redirect(url_for("index"))


# 删除书籍
# delete_book/1
@app.route('/delete_book/<book_id>')
def delete_book(book_id):
    # 1.查询书籍是否存在
    try:
        book = Book.query.get(book_id)
    except Exception as e:
        flash(e)

    # 2.书籍不存在
    if not book:
        flash("书籍不存在，不允许删除")
        return
    # 3.书籍存在
    else:
        try:
            db.session.delete(book)
            db.session.commit()
        except Exception as e:
            flash(e)
            # 数据库回滚
            db.session.rollback()
    # 注意：以上操作只是影响到数据库的数据变化，如果界面需要刷新，需要重新查询数据库
    return redirect(url_for("index"))


if __name__ == '__main__':
    # 删除所有表
    db.drop_all()
    # 创建所有表
    db.create_all()

    # 生成数据
    au1 = Author(name='老王')
    au2 = Author(name='老尹')
    au3 = Author(name='老刘')
    # 把数据提交给用户会话
    db.session.add_all([au1, au2, au3])
    # 提交会话
    db.session.commit()
    bk1 = Book(name='老王回忆录', author_id=au1.id)
    bk2 = Book(name='我读书少，你别骗我', author_id=au1.id)
    bk3 = Book(name='如何才能让自己更骚', author_id=au2.id)
    bk4 = Book(name='怎样征服美丽少女', author_id=au3.id)
    bk5 = Book(name='如何征服英俊少男', author_id=au3.id)
    # 把数据提交给用户会话
    db.session.add_all([bk1, bk2, bk3, bk4, bk5])
    # 提交会话
    db.session.commit()

    app.run(debug=True)
