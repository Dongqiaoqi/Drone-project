# -*- coding: utf-8 -*-
"""
内容读写工具
统一封装前台内容表（Content）的查询与写入，各页面路由只需调用这里的方法。
"""

from core.extensions import db
from core.models import Content

# ============================================================
# 页面标识与中文名称（新增页面时只改这里即可）
# ============================================================
PAGE_NAMES = {
    'index': '首页',
    'about': '公司介绍',
    'training': '无人机培训业务',
    'activities': '无人机活动服务',
    'activities_performance': '无人机表演（详情页）',
    'activities_aerial': '航拍服务（详情页）',
    'activities_science': '科普研学（详情页）',
    'cases': '项目案例',
    'downloads': '资料下载',
    'contact': '联系我们',
}

# ============================================================
# 活动服务下的三个业务（顺序即前台卡片展示顺序）
# slug -> (业务名称, activities 页介绍文字 key, 该业务案例图片所属页面)
# ============================================================
ACTIVITY_TYPES = {
    'performance': ('无人机表演', 'performance', 'activities_performance'),
    'aerial': ('航拍服务', 'aerial', 'activities_aerial'),
    'science': ('科普研学', 'science', 'activities_science'),
}

# 合法页面集合（用于后台路由的白名单校验）
VALID_PAGES = set(PAGE_NAMES.keys())


def get_content(page, content_key, default=''):
    """读取指定页面某个 key 的内容值，不存在时返回默认值"""
    item = Content.query.filter_by(page=page, content_key=content_key).first()
    return item.value if item else default


def get_page_contents(page):
    """读取某页面所有内容，返回 dict: {content_key: value}"""
    items = Content.query.filter_by(page=page).all()
    return {item.content_key: item.value for item in items}


def get_gallery_items(page):
    """
    读取某页面的案例列表：每条包含图片、标题、描述文字
    图片 key 形如 photo_xxx，其标题/描述存放在 photo_xxx_title / photo_xxx_text
    """
    texts = get_page_contents(page)
    items = []
    for img in get_contents_by_type(page, 'image'):
        items.append({
            'id': img.id,
            'image': img.value,
            'title': texts.get(f'{img.content_key}_title', ''),
            'text': texts.get(f'{img.content_key}_text', ''),
        })
    return items


def get_contents_by_type(page, content_type):
    """读取某页面指定类型的内容（如图片列表），按 sort_order 升序"""
    return Content.query.filter_by(
        page=page, content_type=content_type
    ).order_by(Content.sort_order.asc(), Content.id.asc()).all()


def set_content(page, content_key, value, content_type='text'):
    """新增或更新某页面的内容项"""
    item = Content.query.filter_by(page=page, content_key=content_key).first()
    if item:
        item.value = value
        item.content_type = content_type
    else:
        item = Content(
            page=page, content_key=content_key,
            value=value, content_type=content_type
        )
        db.session.add(item)
    db.session.commit()
    return item
