from flask import Flask

app = Flask(__name__)


@app.route('/index.html')
def helloworld():
    return "hello world 666"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8889,debug=True)
