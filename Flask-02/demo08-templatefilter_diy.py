from flask import Flask,render_template

app = Flask(__name__)

#1.自定义列表反转函数
#@app.template__filer("list_reverse")
def do_list_reverse(list):
    # list =None # type: list
    list.reverse()
    return list

#2.通过add_template_filter方法添加自定义函数到jinja2模板过滤器中
# 参数1：函数名称 参数2： 过滤器名称
app.add_template_filter(do_list_reverse,'list_reverse')




@app.route('/')
def index():
    list=[1,4,2,5,3]  # 反转[3,5,2,4,1]

    return render_template('demo08-templatefilter-diy.html',list=list)




if __name__ == '__main__':
    app.run(debug=True)
