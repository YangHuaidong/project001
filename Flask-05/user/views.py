from user import user_bp
from flask import render_template


#3.使用蓝图
# 127.0.0.1:5000/user/info
# user是在创建蓝图的时候统一制定的访问前缀
@user_bp.route('/info')
def user():
    """用户视图函数"""
    return render_template("user/user.html")

"""
1.使用蓝图: 蓝图对象.route('/')
只是在内部会有一个defered_functions列表，会将形成的路由和视图函数的对应规则保存起来

defered_functions = [
    <Rule '/user/info' (GET, OPTIONS, HEAD) -> user>,
    <Rule '/user/info1' (GET, OPTIONS, HEAD) -> user1>,
    <Rule '/user/info2' (GET, OPTIONS, HEAD) -> user2>,
]

2.注册蓝图：app.register_blueprint(user_bp)
将defered_functions列表中的rule规则取出来，使用app.add_url_rule(rule)添加rule规则
最终会将rule规则添加到app.url_map.add(rule)上。


"""