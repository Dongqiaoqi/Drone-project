# -*- coding: utf-8 -*-
"""
后台登录 / 退出路由
"""

from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user, logout_user

from core.models import User
from core.security import login_required
from routes.blueprints import admin_bp


@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    """后台登录页"""
    if current_user.is_authenticated:
        return redirect(url_for('admin.dashboard'))

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')

        user = User.query.filter_by(username=username).first()
        # 校验：账号存在 + 密码正确 + 账号启用
        if user and user.check_password(password) and user.is_active_flag:
            login_user(user)
            flash('登录成功，欢迎回来！', 'success')
            next_page = request.args.get('next') or url_for('admin.dashboard')
            return redirect(next_page)
        flash('用户名或密码错误，请重试。', 'danger')

    return render_template('admin/login.html')


@admin_bp.route('/logout')
@login_required
def logout():
    """退出登录"""
    logout_user()
    flash('已安全退出。', 'info')
    return redirect(url_for('admin.login'))
