from flask import Flask
from cart import car_bp
from user import user_bp



app = Flask(__name__)

#4.注册蓝图
app.register_blueprint(car_bp)
app.register_blueprint(user_bp)


# ImportError: cannot import name 'user' : 循环导入
@app.route('/')
def hello_world():
    return 'Hello World!'


#将用户信息模块抽取到user.py中
# @app.route('/user/info')
# def user():
#     """用户视图函数"""
#     return "user"


#抽取到cart包里面
# @app.route('/cart/info')
# def cart():
#     """购物车视图函数"""
#     return "cart"


@app.route('/goods/info')
def goods():
    """商品视图函数"""
    return "goods"


@app.route('/admin/info')
def admin():
    """admin视图函数"""
    return "admin"


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)
