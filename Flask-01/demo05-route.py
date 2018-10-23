from flask import Flask

app = Flask(__name__)


@app.route('/index.html')
def helloworld():
    return "hello world 666"

# 127.0.0.1:5000/user?user_id=1
#http://127.0.0.1:5000/user/2
#<user_id>  转换器方式提取url路径携带的参数 默认提取的是字符串类型的数据
#<string:user_id>
@app.route("/user/<user_id>")
def demo01(user_id):
    return "demo01 %s" % user_id

#http://127.0.0.1:5000/user_int/2
# <int:user_id>转换器提取url携带的参数 默认提取的是int类型
# int 暂时理解成整形
@app.route('/user_int/<int:user_id>')
def demo02(user_id):
    return "demo02 %d" % user_id

if __name__ == '__main__':
    app.run(debug=True)
