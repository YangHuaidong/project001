from flask import Flask



# 1.自定义项目配置类,只需要将flask的配置属性类的属性的形式定义
class Config(object):
    DEBUG=True

app = Flask(__name__)

# 2.将配置类关联到app的config中
# 方法一:从配置类中读取项目的配置信息(重点)
app.config.from_object(Config)


app.config["DEBUG"]=True


@app.route('/index.html')
def helloworld():
    print(app.config['DEBUG'])
    return "hello world 666"

if __name__ == '__main__':
    app.run()
