from flask import Flask, jsonify
from flask import request

app = Flask(__name__)


#127.0.0.1:5000/login
@app.route('/login', methods=['POST'])
def login():
    #1.获取参数
    username = request.form.get('username')
    password = request.form.get('password')

    #2.判断参数是否为空
    if not all([username, password]):
        result = {
            "errcode": -2,
            "errmsg": "params error"
        }
        return jsonify(result)

    a = 1 / 0
    # 如果账号密码正确
    #3. 判断账号密码是否正确
    if username == 'itheima' and password == 'python':
        result = {
            "errcode": 0,
            "errmsg": "success"
        }
        return jsonify(result)
    else:
        result = {
            "errcode": -1,
            "errmsg": "wrong username or password"
        }
        return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
