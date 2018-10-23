from flask import Blueprint


#1 创建蓝图对象
car_bp = Blueprint("car_bp",__name__)

#2.使用蓝图
@car_bp.route('/cart/info')
def cart():
    """购物车试图函数"""
    return "cart"