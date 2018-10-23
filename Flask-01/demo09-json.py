from flask import Flask,jsonify
import json
app = Flask(__name__)


@app.route('/index.html')
def helloworld():
    return "hello world 666"


@app.route('/json')
def demo1():
    """json数据的转换"""
    dict = {
        "name": "james",
        "age": 34,
        "info":{
            "team": "laker"
        }
    }
    # Serialize ``obj`` to a JSON formatted ``str``
    # 序列化 : python对象转换成json字符串
    json_str = json.dumps(dict)
    #Deserialize ``s`` (a ``str`` instance containing a JSON document) to a Python object.
    # 反序列化：json字符串转换成python对象(list dict)
    my_dict = json.loads(json_str)

    # 1.python对象转换成json字符串
    # 2.指明返回的数据的类型：Content-Type: "application/json"
    # 3.将响应体数据包装成响应对象
    response = jsonify(dict)
    # <Response 71 bytes [200 OK]>
    # response.headers["Content-Type"] = "application/json"
    print(response)
    return response


if __name__ == '__main__':
    app.run(debug=True)

