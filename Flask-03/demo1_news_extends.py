from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/index')
def index():
    """返回新闻首页的模板文件"""
    return render_template("index.html")


@app.route('/detail')
def detail():
    """返回详情页面的模板文件"""
    return render_template("detail.html")

if __name__ == '__main__':
    app.run(debug=True)
