from flask import Flask,redirect,url_for


app = Flask(__name__)


@app.route("/demo01")
def demo01():
    """重定向到黑马官网"""
    #使用redirect 函数完成重定向 参数: url
    return redirect("http://www.itheima.com")

@app.route('/index.html')
def helloworld():
    return "hello world 666"

if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)
