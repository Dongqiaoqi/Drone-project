# -*- coding: utf-8 -*-
"""
无人机公司网站 - 应用入口
只负责：创建应用、注册蓝图、初始化数据库、启动服务。
具体路由见 routes/ 目录，公共核心代码见 core/ 目录。
"""

from flask import Flask

from core.config import Config
from core.extensions import db, login_manager
from core.init_data import init_database
from core.models import User
from routes import register_blueprints


def create_app():
    """应用工厂：创建并配置 Flask 应用"""
    app = Flask(__name__)
    app.config.from_object(Config)

    # 绑定扩展
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'admin.login'
    login_manager.login_message = '请先登录后再访问后台。'

    # 注册前台 / 后台蓝图
    register_blueprints(app)
    return app


app = create_app()


@login_manager.user_loader
def load_user(user_id):
    """Flask-Login 回调：根据 user_id 加载用户"""
    return User.query.get(int(user_id))


if __name__ == '__main__':
    init_database(app)
    # 生产环境请改用 gunicorn 等 WSGI 服务器，例如：
    # gunicorn -w 4 -b 0.0.0.0:5000 app:app
    app.run(host='0.0.0.0', port=5000, debug=True)
