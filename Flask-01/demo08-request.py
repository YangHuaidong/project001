from flask import Flask
from flask import request
app = Flask(__name__)

"""
GET:获取服务器资源,问好后面携带的参数:
一般告知服务器我需要什么数据
POST: 往服务器提交新建数据 服务器最终保存到数据库
请求体里面的参数:需要保存的数据
"""

@app.route('/index.html')
def helloworld():
    return "hello world 666"

# 127.0.0.1:5000/get?user_name=curry&user_id=30
@app.route('/get')
def demo01():
    """提取get请求的问好后面携带的键值对参数"""
    #使用request.method获取请求方式 注意GET需要大写

    if request.method== "GET":
        #方法:request.args.get("key","")
        user_name = request.args.get('user_name','')
        user_id = request.args.get('user_id','')
        return '%s----%s' %(user_name,user_id)
    else:
        return '405 请求方式不正确'



# 127.0.0.1:5000/post
@app.route('/post', methods=['post'])
def demo2():
    """获取post请求体里面携带的参数"""
    # 限定请求方式
    if request.method == 'POST':
        # 方法: request.form.get('key', '')
        user_name = request.form.get("user_name", "")
        user_id = request.form.get("user_id", "")
        return "%s --- %s" % (user_name, user_id)
    else:
        return "405 请求方法不正确"



# 127.0.0.1:5000/upload
@app.route('/upload', methods=['POST'])
def demo3():
    """上传一张图片数据到服务器保存起来"""
    if request.method == 'POST':
        # 方法：request.files.get('key', '')
        file = request.files.get('pic', '')
        # 将图片保存到当前文件(修改图片名称为1.png)
        file.save('./1.png')
        return "upload success"
    else:
        return "405 请求方法不正确"

if __name__ == '__main__':
    app.run(debug=True)
