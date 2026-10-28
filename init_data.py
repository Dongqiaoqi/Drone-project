# -*- coding: utf-8 -*-
"""
应用初始化数据
建表、创建默认管理员账号、补齐默认页面内容（首次启动时调用）。
"""

from core.config import Config
from core.defaults import DEFAULT_CONTENTS
from core.extensions import db
from core.models import Content, User


def init_database(app):
    """初始化数据库：建表 + 默认管理员账号 + 默认页面内容（首次启动）"""
    with app.app_context():
        db.create_all()

        # 默认管理员账号
        if not User.query.filter_by(username=Config.DEFAULT_ADMIN_USERNAME).first():
            admin = User(
                username=Config.DEFAULT_ADMIN_USERNAME,
                is_active_flag=True
            )
            admin.set_password(Config.DEFAULT_ADMIN_PASSWORD)
            db.session.add(admin)
            db.session.commit()
            print(f'[初始化] 默认管理员账号已创建：'
                  f'{Config.DEFAULT_ADMIN_USERNAME} / {Config.DEFAULT_ADMIN_PASSWORD}')

        # 默认页面内容：逐条补齐缺失项（不覆盖已有内容，便于后续新增页面字段）
        existing = {(c.page, c.content_key) for c in Content.query.all()}
        added = 0
        for page, key, ctype, value in DEFAULT_CONTENTS:
            if (page, key) in existing:
                continue
            db.session.add(
                Content(page=page, content_key=key,
                        content_type=ctype, value=value)
            )
            added += 1
        if added:
            db.session.commit()
            print(f'[初始化] 已补齐默认页面内容 {added} 项。')
