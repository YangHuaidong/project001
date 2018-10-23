from flask import Flask,session

app = Flask(__name__)
app.config['SECRET_KEY']='ADASDAJD'

@app.route('/index.html')
def helloworld():
    return "hello world 666"

@app.route('/login')
def login():
    """登陆成功使用session保存用户登陆成功的数据"""
    #session 是将用户数据保存到服务器内存中__>项目中会将session的存储调整到redis数据库中
    session['user_name']='kebe'
    session['user_id']='1'

    return 'login success'

@app.route('/index')
def index():
    """访问首页使用session获取用户登陆信息"""
    user_name = session.get('user_name','')
    user_id = session.get('user_id','')

    return 'index %s---%s' % (user_name,user_id)

@app.route("/login_out")
def login_out():
    """退出登陆删除session中的用户信息"""
    session.pop('user_name','')
    session.pop('user_id','')

    return 'login_out success'

if __name__ == '__main__':
    app.run(debug=True)
