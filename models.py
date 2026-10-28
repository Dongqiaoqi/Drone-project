# -*- coding: utf-8 -*-
"""
数据库模型定义
使用 Flask-SQLAlchemy + SQLite，无需单独安装数据库服务。
"""

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

# 数据库实例统一从 core.extensions 导入（避免循环导入）
from core.extensions import db


# ============================================================
# 用户表：后台管理员账号
# ============================================================
class User(UserMixin, db.Model):
    """后台员工账号表"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False, index=True)
    # 密码哈希（不存储明文密码）
    password_hash = db.Column(db.String(256), nullable=False)
    # 账号是否启用
    is_active_flag = db.Column(db.Boolean, default=True)
    # 创建时间
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        """设置密码：自动生成哈希值存储"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """校验密码：比对哈希值，返回 True/False"""
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'


# ============================================================
# 页面内容表：存储前台所有可编辑的文字、图片、PDF
# 采用 key-value 结构，每个 content_key 对应页面上的一个可编辑区域
# ============================================================
class Content(db.Model):
    """前台页面内容表（文字 / 图片 / PDF 统一存储）"""
    __tablename__ = 'contents'

    id = db.Column(db.Integer, primary_key=True)
    # 所属页面标识，如 index / about / training / activities / cases / downloads / contact
    page = db.Column(db.String(32), nullable=False, index=True)
    # 内容区块标识，同一页面内唯一，如 banner_title / about_text
    content_key = db.Column(db.String(64), nullable=False)
    # 内容类型: text(文字) / image(图片) / pdf(PDF文件)
    content_type = db.Column(db.String(16), nullable=False, default='text')
    # 内容值：文字直接存文本；图片/PDF 存储上传后的文件名
    value = db.Column(db.Text, default='')
    # 排序号（用于轮播图等有序内容）
    sort_order = db.Column(db.Integer, default=0)
    # 更新时间
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    __table_args__ = (
        # 同一页面内 content_key 唯一
        db.UniqueConstraint('page', 'content_key', name='uq_page_key'),
    )

    def __repr__(self):
        return f'<Content {self.page}.{self.content_key}>'
