# 专门在init文件做导入工作，视图函数的业务逻辑代码放到views.py
from flask import Blueprint

#1.创建蓝图
# url_prefix:访问所有user模块的url前缀
user_bp = Blueprint("user_bp",
                    __name__,
                    static_folder="static",
                    template_folder="templates",
                    url_prefix="/user"
                    )

#2.延迟导入 （切记一定要导入views文件，不然整个包就发现不了里面的视图函数，没法注册路由）
from .views import *

