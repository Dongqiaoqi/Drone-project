# -*- coding: utf-8 -*-
"""
安全相关工具
1. 后台登录态校验装饰器
2. 上传文件类型白名单校验与保存
"""

import os
from datetime import datetime
from functools import wraps

from flask import current_app, flash, redirect, request, url_for
from flask_login import current_user
from werkzeug.utils import secure_filename


def login_required(view_func):
    """
    登录态校验装饰器
    后台所有路由都必须经过此装饰器，未登录用户会被重定向到登录页。
    """
    @wraps(view_func)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated:
            flash('请先登录后再访问后台。', 'warning')
            return redirect(url_for('admin.login', next=request.path))
        return view_func(*args, **kwargs)
    return wrapper


def allowed_file(filename, allowed_set=None):
    """校验文件后缀是否在允许的白名单内"""
    if allowed_set is None:
        allowed_set = current_app.config['ALLOWED_EXTENSIONS']
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_set


def is_image_file(filename):
    """是否为允许的图片格式"""
    return allowed_file(filename, current_app.config['ALLOWED_IMAGE_EXTENSIONS'])


def is_pdf_file(filename):
    """是否为 PDF 格式"""
    return allowed_file(filename, current_app.config['ALLOWED_PDF_EXTENSIONS'])


def save_uploaded_file(file_storage, file_type='image'):
    """
    保存上传文件到对应目录，返回保存后的文件名
    :param file_storage: request.files 中的文件对象
    :param file_type: 'image' 或 'pdf'
    :raises ValueError: 文件类型不合法
    """
    filename = secure_filename(file_storage.filename)

    if file_type == 'image':
        if not is_image_file(filename):
            raise ValueError('仅允许上传 png/jpg/jpeg/gif/webp/bmp 格式的图片')
        save_dir = current_app.config['UPLOAD_IMG_FOLDER']
    elif file_type == 'pdf':
        if not is_pdf_file(filename):
            raise ValueError('仅允许上传 PDF 格式文件')
        save_dir = current_app.config['UPLOAD_PDF_FOLDER']
    else:
        raise ValueError('未知的文件类型')

    # 时间戳前缀，避免同名文件互相覆盖
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S%f')
    safe_name = f'{timestamp}_{filename}'

    file_storage.save(os.path.join(save_dir, safe_name))
    return safe_name
