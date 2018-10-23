from flask import Flask
"""
__name__
1.当你使用python3 helloworld.py 运行的时候 此时 __name__ == '__main__'
2.当你导包的形式  此时 __name__ ==  helloworld

__name__作用:(重点)

会认为 helloworld.py文件所在的目录就是flask项目目录

就会
"""
app=Flask(__name__)


@app.route('/index.html')
def helloworld():
    return "hello world 666"

if __name__ == '__main__':
    app.run()