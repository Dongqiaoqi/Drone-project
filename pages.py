# -*- coding: utf-8 -*-
"""
后台页面管理路由：仪表盘、按页面编辑内容
"""

from flask import abort, flash, redirect, render_template, request, url_for

from core.labels import GALLERY_PAGES, IMAGE_SLOTS, PDF_SLOTS, label_for
from core.security import login_required
from core.utils import (
    ACTIVITY_TYPES, PAGE_NAMES, VALID_PAGES,
    get_contents_by_type, get_page_contents, set_content
)
from routes.blueprints import admin_bp


def _preview_url(page):
    """后台“预览前台”链接：普通页面直接映射，活动案例子页面映射到详情页"""
    if page.startswith('activities_'):
        slug = page.split('_', 1)[1]
        if slug in ACTIVITY_TYPES:
            return url_for('front.activity_detail', slug=slug)
    return url_for('front.' + page)


@admin_bp.route('/')
@login_required
def dashboard():
    """后台首页：页面列表与编辑入口"""
    return render_template('admin/dashboard.html', pages=PAGE_NAMES.items())


@admin_bp.route('/edit/<page>', methods=['GET', 'POST'])
@login_required
def edit(page):
    """
    可视化编辑页面内容
    GET：展示当前内容与编辑表单
    POST：保存文字内容
    """
    # 页面白名单校验，防止越权编辑不存在的页面
    if page not in VALID_PAGES:
        abort(404)

    if request.method == 'POST':
        # 只保存该页面的文字字段，避免把图片/PDF 记录改成文字
        text_keys = {item.content_key for item in get_contents_by_type(page, 'text')}
        for key, value in request.form.items():
            if key not in text_keys:
                continue
            set_content(page, key, value, content_type='text')
        flash('内容已保存，前台将自动更新。', 'success')
        return redirect(url_for('admin.edit', page=page))

    # 文字字段（带中文名称）；案例条目的标题/描述不在此处，避免重复编辑
    text_items = [
        {
            'key': item.content_key,
            'label': label_for(page, item.content_key, 'text'),
            'value': item.value,
        }
        for item in get_contents_by_type(page, 'text')
        if not item.content_key.startswith('photo_')
    ]
    # 图片 / PDF 列表（带中文名称）
    image_items = [
        (item, label_for(page, item.content_key, 'image'))
        for item in get_contents_by_type(page, 'image')
    ]
    pdf_items = [
        (item, label_for(page, item.content_key, 'pdf'))
        for item in get_contents_by_type(page, 'pdf')
    ]

    # 案例条目：图片 + 标题 + 描述（仅案例类页面）
    texts = get_page_contents(page)
    case_items = [
        {
            'id': img.id,
            'image': img.value,
            'title': texts.get(f'{img.content_key}_title', ''),
            'text': texts.get(f'{img.content_key}_text', ''),
        }
        for img in get_contents_by_type(page, 'image')
    ]

    return render_template(
        'admin/edit.html',
        page=page,
        page_names=PAGE_NAMES,
        preview_url=_preview_url(page),
        text_items=text_items,
        image_items=image_items,
        pdf_items=pdf_items,
        case_items=case_items,
        # 下拉选项中显示中文位置名称
        image_slots=IMAGE_SLOTS.get(page, {}),
        pdf_slots=PDF_SLOTS.get(page, {}),
        gallery=page in GALLERY_PAGES,
    )
