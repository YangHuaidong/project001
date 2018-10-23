from flask import Flask,request, session, current_app, g

app = Flask(__name__)

"""
working outside of request context 超出了请求上下文的范围
print(request)
print(session)


working outside of application context 超出了应用上下文的范围
print(current_app)
print(g)
"""
@app.route('/index.html')
def helloworld():
    return "hello world 666"

    # 请求上下文 (request session)
    print(request.method)
    print(request.url)
    session["name"] = "durant"
    print(session.get("name"))

    # 应用上下文(current_app g)
    print(current_app.config.get("DEBUG"))

    # 不通用户使用线程id进行区分
    g.username = "james"
    print(g.username)

    return 'Hello World!'



if __name__ == '__main__':
    app.run(debug=True)
