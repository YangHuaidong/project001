import json
#0.导入python自带单元测试类
import unittest
from demo02_login  import app


#1.自定义单元测试类，继承unittest.TestCase
class LoginTest(unittest.TestCase):
    """为登录逻辑编写测试案例"""

    #初始化方法
    def setUp(self):
        # 相当于开启debug模式，精确定位被测试的代码的异常信息
        app.testing = True
        # 发送网络请求的客户端
        self.client = app.test_client()

    # 单元测试函数，注意：该函数必须以test_开头
    def test_password(self):
        """测试用户名与密码填写正确的[当参数不全的话，返回errcode=0]"""
        # 发送post请求 data携带表单数据
        response = self.client.post('/login', data={"username":"itheima","password":"python"})
        json_data = response.data.decode()
        # 将data数据转换成字典
        json_dict = json.loads(json_data)

        #断言errcode是否在json_dict字典内
        self.assertIn('errcode', json_dict, '数据格式返回错误')
        #断言返回的errcode必须是0
        self.assertEqual(json_dict['errcode'], 0, '状态码返回错误')

    #单元测试函数，注意：该函数必须以test_开头
    def test_empty_username_password(self):
        """测试用户名与密码为空的情况[当参数不全的话，返回errcode=-2]"""
        response = app.test_client().post('/login', data={})
        json_data = response.data.decode()
        json_dict = json.loads(json_data)

        self.assertIn('errcode', json_dict, '数据格式返回错误')
        self.assertEqual(json_dict['errcode'], -2, '状态码返回错误')

        # TODO 测试用户名为空的情况
        # TODO 测试密码为空的情况

    def test_error_username_password(self):
        """测试用户名和密码错误的情况[当登录名和密码错误的时候，返回 errcode = -1]"""
        response = app.test_client().post('/login', data={"username": "aaaaa", "password": "12343"})
        json_data = response.data.decode()
        json_dict = json.loads(json_data)
        self.assertIn('errcode', json_dict, '数据格式返回错误')
        self.assertEqual(json_dict['errcode'], -1, '状态码返回错误')

        # TODO 测试用户名错误的情况
        # TODO 测试密码错误的情况

if __name__ == '__main__':
    # 运行单元测试
    unittest.main()