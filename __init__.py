# -*- coding: utf-8 -*-
"""
路由包入口
先导入各路由子包（完成路由注册），再统一注册蓝图到应用。
"""

from routes.blueprints import admin_bp, front_bp

# 导入前台 / 后台子包以触发路由注册（顺序无关）
from routes import admin, front  # noqa: E402,F401


def register_blueprints(app):
    """把所有蓝图注册到 Flask 应用"""
    app.register_blueprint(front_bp)
    app.register_blueprint(admin_bp)
