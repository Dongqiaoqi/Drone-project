# -*- coding: utf-8 -*-
"""
蓝图定义集中放这里，供各路由模块导入，避免互相引用造成循环导入。
"""

from flask import Blueprint

# 前台：访客浏览（无任何提交交互）
front_bp = Blueprint('front', __name__)

# 后台：统一挂在 /admin 前缀下，所有路由都需登录
admin_bp = Blueprint('admin', __name__, url_prefix='/admin')
