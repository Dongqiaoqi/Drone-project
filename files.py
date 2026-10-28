# -*- coding: utf-8 -*-
"""
后台上传与删除路由：图片上传、PDF 上传、内容删除
"""

import os
from datetime import datetime

from flask import abort, current_app, flash, redirect, request, url_for

from core.extensions import db
from core.labels import GALLERY_PAGES, IMAGE_SLOTS, PDF_SLOTS
from core.models import Content
from core.security import login_required, save_uploaded_file
from core.utils import VALID_PAGES, set_content
from routes.blueprints import admin_bp


def _get_uploaded_file(page):
    """从请求中取出文件，返回 (file, 错误提示)"""
    if 'file' not in request.files:
        return None, '未选择文件。'
    file = request.files['file']
    if file.filename == '':
        return None, '未选择文件。'
    return file, None


@admin_bp.route('/upload/image/<page>', methods=['POST'])
@login_required
def upload_image(page):
    """上传图片：案例页面图片可选，其他页面必须选择图片"""
    if page not in VALID_PAGES:
        abort(404)

    file = request.files.get('file')
    has_file = bool(file and file.filename)

    if page in GALLERY_PAGES:
        # 案例：标题、描述必填，图片可选
        title = request.form.get('title', '').strip()
        text = request.form.get('text', '').strip()
        if not title or not text:
            flash('案例标题和案例描述必须填写。', 'warning')
            return redirect(url_for('admin.edit', page=page))

        content_key = f'photo_{datetime.now().strftime("%Y%m%d%H%M%S%f")}'
        filename = ''
        if has_file:
            try:
                filename = save_uploaded_file(file, file_type='image')
            except ValueError as e:
                flash(str(e), 'danger')
                return redirect(url_for('admin.edit', page=page))

        set_content(page, content_key, filename, content_type='image')
        set_content(page, f'{content_key}_title', title, content_type='text')
        set_content(page, f'{content_key}_text', text, content_type='text')
        flash('案例已新增，前台已同步展示。', 'success')
        return redirect(url_for('admin.edit', page=page))

    # 其他页面（如首页轮播）：必须选择图片并指定位置
    if not has_file:
        flash('未选择文件。', 'warning')
        return redirect(url_for('admin.edit', page=page))

    content_key = request.form.get('content_key', '').strip()
    if content_key not in IMAGE_SLOTS.get(page, {}):
        flash('请选择要上传的图片位置。', 'warning')
        return redirect(url_for('admin.edit', page=page))

    try:
        filename = save_uploaded_file(file, file_type='image')
        set_content(page, content_key, filename, content_type='image')
        flash('图片上传成功。', 'success')
    except ValueError as e:
        flash(str(e), 'danger')

    return redirect(url_for('admin.edit', page=page))


@admin_bp.route('/upload/pdf/<page>', methods=['POST'])
@login_required
def upload_pdf(page):
    """上传 PDF 到指定页面"""
    if page not in VALID_PAGES:
        abort(404)

    file, error = _get_uploaded_file(page)
    if error:
        flash(error, 'warning')
        return redirect(url_for('admin.edit', page=page))

    content_key = request.form.get('content_key', '').strip()
    if content_key not in PDF_SLOTS.get(page, {}):
        flash('请选择要上传的文档位置。', 'warning')
        return redirect(url_for('admin.edit', page=page))

    try:
        filename = save_uploaded_file(file, file_type='pdf')
        set_content(page, content_key, filename, content_type='pdf')
        flash('PDF 上传成功。', 'success')
    except ValueError as e:
        flash(str(e), 'danger')

    return redirect(url_for('admin.edit', page=page))


@admin_bp.route('/case/<int:content_id>', methods=['POST'])
@login_required
def update_case(content_id):
    """保存某条案例的标题与描述文字"""
    item = Content.query.get_or_404(content_id)
    if item.content_type != 'image' or item.page not in GALLERY_PAGES:
        abort(404)

    title = request.form.get('title', '').strip()
    text = request.form.get('text', '').strip()
    if not title or not text:
        flash('案例标题和案例描述必须填写。', 'warning')
        return redirect(url_for('admin.edit', page=item.page))

    set_content(item.page, f'{item.content_key}_title', title, content_type='text')
    set_content(item.page, f'{item.content_key}_text', text, content_type='text')
    flash('案例已保存。', 'success')
    return redirect(url_for('admin.edit', page=item.page))


@admin_bp.route('/delete/content/<int:content_id>', methods=['POST'])
@login_required
def delete_content(content_id):
    """删除内容记录（图片 / PDF 同时删除磁盘文件）"""
    item = Content.query.get_or_404(content_id)
    page = item.page

    if item.content_type == 'image':
        filepath = os.path.join(current_app.config['UPLOAD_IMG_FOLDER'], item.value)
    elif item.content_type == 'pdf':
        filepath = os.path.join(current_app.config['UPLOAD_PDF_FOLDER'], item.value)
    else:
        filepath = None

    if filepath and os.path.exists(filepath):
        try:
            os.remove(filepath)
        except OSError:
            pass  # 磁盘文件删除失败不影响记录删除

    db.session.delete(item)

    # 案例图片：同时删除它对应的标题与描述文字
    if item.content_type == 'image' and item.content_key.startswith('photo_'):
        Content.query.filter(
            Content.page == page,
            Content.content_key.in_([
                f'{item.content_key}_title',
                f'{item.content_key}_text',
            ])
        ).delete(synchronize_session=False)

    db.session.commit()
    flash('内容已删除。', 'success')
    return redirect(url_for('admin.edit', page=page))
