from flask import Flask

app = Flask(__name__)


@app.route('/index.html')
def helloworld():
    return "hello world 666"

#使用methods属性指明请求方式
@app.route("/post",methods=["POST"])
def demo01():
    return "post success"

"""
之前：
Map([<Rule '/post' (OPTIONS, GET, HEAD) -> demo1>,
 <Rule '/' (OPTIONS, GET, HEAD) -> hello_world>,
 <Rule '/static/<filename>' (OPTIONS, GET, HEAD) -> static>])

 修改后:
 Map([<Rule '/post' (OPTIONS, POST) -> demo1>,
 <Rule '/' (GET, OPTIONS, HEAD) -> hello_world>,
 <Rule '/static/<filename>' (GET, OPTIONS, HEAD) -> static>])
"""

if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)
