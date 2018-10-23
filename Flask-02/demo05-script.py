from flask_script import Manager

from flask import Flask

#1.创建app对象
app = Flask(__name__)

#2.创建管理对象,将app交给manager管理
manager = Manager(app)

@app.route('/index.html')
def helloworld():
    return "hello world 666"

if __name__ == '__main__':
   manager.run()
