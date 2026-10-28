# -*- coding: utf-8 -*-
"""
前台页面路由（访客仅浏览：看内容、看图片、下载 PDF）
每个页面一个视图函数，一一对应 templates/front/ 下的模板。
"""

from flask import abort, current_app, render_template, send_from_directory, url_for

from routes.blueprints import front_bp
from core.utils import ACTIVITY_TYPES, get_contents_by_type, get_gallery_items, get_page_contents


@front_bp.route('/')
def index():
    """首页：banner 轮播 + 业务快速入口"""
    texts = get_page_contents('index')

    # ---- 滚屏一：首页通用 banner（只展示已上传的图片，没有则保留一张默认渐变）----
    banner_images = [texts.get(f'banner_{i}', '') for i in (1, 2, 3)]
    banner_images = [img for img in banner_images if img] or ['']
    slides = [
        {
            'image': img,
            'title': texts.get('hero_title', '专业无人机综合服务商'),
            'subtitle': texts.get('hero_subtitle', '无人机培训 · 活动表演 · 航拍服务 · 科普研学'),
            'link': url_for('front.about'),
            'link_text': '了解更多',
            'variant': '',
        }
        for img in banner_images
    ]

    # ---- 滚屏二：无人机表演 / 科普研学 / 航拍服务（各自图片、文案，点击进入业务详情）----
    for slug, (name, _intro_key, _page) in ACTIVITY_TYPES.items():
        slides.append({
            'image': texts.get(f'{slug}_banner', ''),
            'title': texts.get(f'{slug}_banner_title', name),
            'subtitle': texts.get(f'{slug}_banner_subtitle', ''),
            'link': url_for('front.activity_detail', slug=slug),
            'link_text': '查看项目案例',
            'variant': slug,
        })

    return render_template('front/index.html', slides=slides, texts=texts)


@front_bp.route('/about')
def about():
    """公司介绍：企业背景、资质、团队 + PDF 下载"""
    return render_template('front/about.html', contents=get_page_contents('about'))


@front_bp.route('/training')
def training():
    """无人机培训业务：课程、师资、场地、培训案例"""
    return render_template(
        'front/training.html',
        contents=get_page_contents('training'),
        cases=get_gallery_items('training'),
    )


@front_bp.route('/activities')
def activities():
    """无人机活动服务：表演、科普研学、航拍"""
    # 三张业务卡片的标题、副标题与各自详情页保持一致，改一处即可同步
    titles = {}
    subtitles = {}
    for slug, (name, _intro_key, page) in ACTIVITY_TYPES.items():
        detail = get_page_contents(page)
        titles[slug] = detail.get('detail_title') or name
        subtitles[slug] = detail.get('detail_subtitle', '')
    return render_template(
        'front/activities.html',
        contents=get_page_contents('activities'),
        titles=titles,
        subtitles=subtitles,
    )


@front_bp.route('/activities/<slug>')
def activity_detail(slug):
    """
    单个活动业务详情：业务介绍 + 该业务的项目案例相册
    slug: performance / science / aerial
    """
    if slug not in ACTIVITY_TYPES:
        abort(404)

    name, intro_key, page = ACTIVITY_TYPES[slug]
    detail = get_page_contents(page)
    return render_template(
        'front/activity_detail.html',
        slug=slug,
        name=detail.get('detail_title') or name,
        subtitle=detail.get('detail_subtitle', '业务介绍与项目案例'),
        # 详情页介绍优先取本业务页面的内容，未填写时回退到活动服务列表页的摘要
        intro=detail.get('detail_intro') or get_page_contents('activities').get(intro_key, ''),
        gallery_title=detail.get('gallery_title') or '项目案例',
        cases=get_gallery_items(page),
    )


@front_bp.route('/cases')
def cases():
    """项目案例：多条案例（图片 + 标题 + 描述）"""
    return render_template(
        'front/cases.html',
        contents=get_page_contents('cases'),
        cases=get_gallery_items('cases'),
    )


@front_bp.route('/downloads')
def downloads():
    """资料下载：PDF 文档列表"""
    return render_template(
        'front/downloads.html',
        contents=get_page_contents('downloads'),
        pdfs=get_contents_by_type('downloads', 'pdf'),
    )


@front_bp.route('/contact')
def contact():
    """联系我们"""
    return render_template('front/contact.html', contents=get_page_contents('contact'))


@front_bp.route('/uploads/<file_type>/<filename>')
def uploaded_file(file_type, filename):
    """访问后台上传的图片 / PDF"""
    if file_type == 'images':
        directory = current_app.config['UPLOAD_IMG_FOLDER']
    elif file_type == 'pdfs':
        directory = current_app.config['UPLOAD_PDF_FOLDER']
    else:
        abort(404)
    return send_from_directory(directory, filename)
