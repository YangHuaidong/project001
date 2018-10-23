from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():
    list=[1,5,4,2,3]
    html_str ='<h1>Wosibioati</h1>'
    goods_list =[{
        'goods_name':'xigua',
        'price':10
    },
    {
        'goods_name': '柚子',
        'price': 100
    }

    ]
    return render_template('demo07-templatefilter.html',    list=list,
                           html_str=html_str,
                           goods_list=goods_list)




if __name__ == '__main__':
    app.run(debug=True)
