from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():
    # 只显示4行数据，背景颜色依次为：黄，绿，红，紫
    my_list = [
        {
            "id": 1,
            "value": "我爱工作"
        },
        {
            "id": 2,
            "value": "工作使人快乐"
        },
        {
            "id": 3,
            "value": "沉迷于工作无法自拔"
        },
        {
            "id": 4,
            "value": "日渐消瘦"
        },
        {
            "id": 5,
            "value": "以梦为马，越骑越傻"
        }
    ]
    return render_template('demo09-controlblock.html',my_list=my_list)




if __name__ == '__main__':
    app.run(debug=True)
