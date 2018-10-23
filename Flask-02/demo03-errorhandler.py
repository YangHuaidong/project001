from flask import Flask
from flask import abort
from flask import redirect

app = Flask(__name__)


@app.route('/')
def helloworld():
    a= 1/0
    #主动产生一个异常  状态码:必须是http标准状态码
    abort(404)
    return "hello world 666"

@app.errorhandler(404)
def error(e):
    """
        404 Not Found: The requested URL was not found on the server.
        If you entered the URL manually please check your spelling and try again.
        """
    print(e)
    return redirect('http://hd.mi.com/webfile/zt/hd/2014042802/cn.html')

#使用app.errorhandler捕获异常信息
@app.errorhandler(ZeroDivisionError)
def zeroroor(e):
    print(e)
    return '不能除以0'


if __name__ == '__main__':
    app.run(debug=True)
