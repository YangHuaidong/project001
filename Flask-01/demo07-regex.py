from flask import Flask
from werkzeug.routing import BaseConverter

class RegexConverter(BaseConverter):
    #重新regex属性
    # 将自定义的正则表达式传入,BaseConverter这个父类就会版子类完成正则的注册
    #regex="[0-9]{6}"
    def __init__(self,map,re):
        #1.初始化父类init的方法,完成父类的功能 map:相当于url_map
        super(RegexConverter, self).__init__(map)
        #2.子类自身的初始化工作,完成额外的需求
        self.regex = re



app = Flask(__name__)

#2,将自定义的类关联到url_map.converters形成键值对
app.url_map.converters['re']=RegexConverter

@app.route('/index.html')
def helloworld():
    return "hello world 666"


#http://127.0.0.1:5000/user/123456
#3.基本使用：<re:user_id>
#传入参数的方式：re("[0-9]{6}")
@app.route('/user/<re("[0-9]{6}"):user_id>')
def demo1(user_id):
    return "user_id %s" % user_id


if __name__ == '__main__':
    app.run(debug=True)
