from flask import Flask,render_template


app = Flask(__name__)


@app.route('/')
def index():
    #业务逻辑

    my_int = 18
    my_str = 'laowang'
    my_list = [1,2,3,4,5]
    my_dict = {
        'name':'haeden',
        'age': 28
    }

    #使用render_template渲染模板
    #参数1:模板名称 参数n:需要传入到模板里面的参数,以键值对的形式往后排

    return render_template('demo06_template.html',
                           my_int=my_int,
                           my_str=my_str,
                           my_list=my_list,
                           my_dict=my_dict

                           )



if __name__ == '__main__':
    app.run(debug=True)
