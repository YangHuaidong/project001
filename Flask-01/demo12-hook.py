from flask import Flask

app = Flask(__name__)

# / --> hello_world  self.url_map.add()
@app.route('/')
def hello_world():
    return 'Hello World!'


# 第一次请求之前调用该视图函数(只会调用一次)
# 应用场景: 初始化操作
@app.before_first_request
def before_first_request():
    print("before_first_request")


# 每次请求之前都会调用该视图函数(调用多次)
# 应用场景：ip处理(封ip)
@app.before_request
def before_request():
    print("before_request")
    # if ip in black_ips:
    #     假装封ip处理


# 每次请求之后会调用该视图函数(调用多次)
# 应用场景：可以拦截对响应对象进行统一处理
@app.after_request
def after_request(response):
    print("after_request")
    # 拦截处理
    # response.headers["Content-Type"] = "application/json"
    # response.set_cookie
    return response


# 每次请求结束之后会调用该视图函数(调用多次)
# 每次会传入error  如果请求没有错误 error为空
# 应用场景：异常处理
@app.teardown_request
def teardown_request(error):
    print(error)
    print("teardown_request")


if __name__ == '__main__':
    app.run(debug=True)
