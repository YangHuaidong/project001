from flask import Flask,make_response,request

app = Flask(__name__)


@app.route('/index.html')
def helloworld():
    return "hello world 666"


@app.route('/login')
def login():
    """登陆成功后使用cookie保存用户的登陆信息"""
    # 1.创建响应对象
    response = make_response('login success')
    # 2.使用响应对象中的set_cookie方法设置用户信息(键值对)
    # 参数1：key  参数2：value 参数3：max_age代表过期时长
    response.set_cookie("user_name","laowang",max_age=3600)
    response.set_cookie("user_id","1",max_age=3600)
    #3.返回 响应对应
    return response


@app.route('/index')
def index():
    """再次请求首页的时候获取cookie中的用户信息"""
    user_name = request.cookies.get('user_name','')
    user_id = request.cookies.get('user_id','')

    return 'index %s ---%s' % (user_name,user_id)



if __name__ == '__main__':
    app.run(debug=True)
