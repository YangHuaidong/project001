from flask import Flask, render_template, session, g


app = Flask(__name__)
# 加密字符串
app.secret_key = "asdlkjasdlkasjd"


# /
@app.route('/')
def index():
    # 设置键值对数据（模板中的特殊变量不需要传入直接在模板中使用即可）
    session["name"] = "jordan"
    # 使用g对象保存数据 (模板中的特殊变量不需要传入直接在模板中使用即可）
    g.user = "curry"
    return render_template("specail.html")


if __name__ == '__main__':
    app.run(debug=True)
