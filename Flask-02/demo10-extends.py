from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "hello world "

#父模板
@app.route('/parent')
def parent():
    return render_template('dase.html' )
#子模板
@app.route('/child')
def child():
    return render_template("child.html")

if __name__ == '__main__':
    app.run(debug=True)
