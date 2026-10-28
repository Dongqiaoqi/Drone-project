# -*- coding: utf-8 -*-
"""
扩展实例集中定义
避免 app.py 与各业务模块之间产生循环导入。
"""

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# 数据库实例（在 app.py 的 create_app 中绑定应用）
db = SQLAlchemy()

# 登录管理器
login_manager = LoginManager()
