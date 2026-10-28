# -*- coding: utf-8 -*-
"""
全局配置文件
集中管理 Flask 应用的所有可调参数，方便部署时统一修改。
"""

import os

# ============================================================
# 基础路径配置
# ============================================================
# 项目根目录（本文件位于 core/ 目录，上一级即项目根目录）
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 上传文件存放目录（图片、PDF 等静态资源独立存放，方便管理与备份）
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
# 进一步按类型分子目录，便于维护
UPLOAD_IMG_FOLDER = os.path.join(UPLOAD_FOLDER, 'images')
UPLOAD_PDF_FOLDER = os.path.join(UPLOAD_FOLDER, 'pdfs')

# 数据库文件所在目录（SQLite 文件需要父目录存在）
INSTANCE_FOLDER = os.path.join(BASE_DIR, 'instance')

# 确保上传目录与数据库目录存在
for _d in (UPLOAD_FOLDER, UPLOAD_IMG_FOLDER, UPLOAD_PDF_FOLDER, INSTANCE_FOLDER):
    os.makedirs(_d, exist_ok=True)


class Config:
    """Flask 应用配置类"""

    # ---------- 安全相关 ----------
    # 会话密钥：生产环境务必修改为随机长字符串！
    # 可通过 python -c "import secrets; print(secrets.token_hex(32))" 生成
    SECRET_KEY = os.environ.get('SECRET_KEY', 'drone-site-change-me-in-production-please')

    # ---------- 数据库 ----------
    # SQLite 数据库文件路径
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'instance', 'site.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 关闭信号追踪，节省资源

    # ---------- 文件上传 ----------
    # 允许上传的文件类型（白名单机制，拦截危险格式）
    ALLOWED_IMAGE_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp', 'bmp'}
    ALLOWED_PDF_EXTENSIONS = {'pdf'}
    ALLOWED_EXTENSIONS = ALLOWED_IMAGE_EXTENSIONS | ALLOWED_PDF_EXTENSIONS

    # 单个文件最大 16MB
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024

    # ---------- 上传目录 ----------
    UPLOAD_FOLDER = UPLOAD_FOLDER
    UPLOAD_IMG_FOLDER = UPLOAD_IMG_FOLDER
    UPLOAD_PDF_FOLDER = UPLOAD_PDF_FOLDER

    # ---------- 默认管理员账号（首次启动时自动创建）----------
    # 生产环境建议登录后立即修改密码
    DEFAULT_ADMIN_USERNAME = 'admin'
    DEFAULT_ADMIN_PASSWORD = 'admin123'
