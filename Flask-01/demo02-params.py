from flask import Flask

"""
__name__作用：
 就会认为当前py文件所在的目录就是项目目录，会在这个目录文件夹下去寻找对应的静态文件目录和模板文件目录

static_path: 访问静态文件的是时候url的前缀(过期了) 默认值：/static
static_url_path: 访问静态文件的是时候url的前缀 默认值：/static
static_folder: 静态文件存储的文件夹名称 默认值：static
template_folder: 模板文件存储的文件夹名称 默认值：templates

注意点：__name__ 值的没有的文件名称，flask默认会认为该文件夹就是项目目录
      __name__ python自带的这么写模块，这些模块下面就没有定义static静态文件夹那么就会访问不到
"""
app = Flask(__name__,
            static_path='/static',
            static_url_path='/static',
            static_folder='static',
            template_folder='templates'


            )

"""
Map(
[
 <Rule '/' (HEAD, OPTIONS, GET) -> index>,
 <Rule '/static/<filename>' (HEAD, OPTIONS, GET) -> static>   #flask默认提供的路径
 ])
"""
@app.route('/index.html')
def index():
    print(app.url_map)
    return "hello world 666"

if __name__ == '__main__':
    app.run(debug=True)
