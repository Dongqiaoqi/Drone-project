# -*- coding: utf-8 -*-
"""
后台编辑界面的中文名称
内部仍然使用英文 key 存储，员工在后台看到的全部是中文。
"""

# ============================================================
# 各页面文字字段的中文名称（新增字段时在这里补一行）
# ============================================================
KEY_LABELS = {
    'index': {
        'hero_title': '首页主标题',
        'hero_subtitle': '首页副标题',
        'intro_text': '公司简介',
        'about_title': '“关于我们”版块标题',
        'services_title': '“业务服务”版块标题',
        'services_subtitle': '“业务服务”版块副标题',
        'training_card_title': '“无人机培训”主卡片标题',
        'training_card_subtitle': '“无人机培训”主卡片副标题',
        'training_card_intro': '“无人机培训”主卡片介绍',
        'activities_card_title': '“无人机活动”主卡片标题',
        'activities_card_subtitle': '“无人机活动”主卡片副标题',
        'activities_card_intro': '“无人机活动”主卡片介绍',
        'banner_1': '首页轮播图一',
        'banner_2': '首页轮播图二',
        'banner_3': '首页轮播图三',
        'performance_banner': '无人机表演滚屏背景图',
        'performance_banner_title': '无人机表演滚屏标题',
        'performance_banner_subtitle': '无人机表演滚屏副标题',
        'science_banner': '科普研学滚屏背景图',
        'science_banner_title': '科普研学滚屏标题',
        'science_banner_subtitle': '科普研学滚屏副标题',
        'aerial_banner': '航拍服务滚屏背景图',
        'aerial_banner_title': '航拍服务滚屏标题',
        'aerial_banner_subtitle': '航拍服务滚屏副标题',
    },
    'about': {
        'company_name': '公司名称',
        'background_title': '“企业背景”小标题',
        'background': '企业背景',
        'qualification_title': '“公司资质”小标题',
        'qualification': '公司资质',
        'team_title': '“团队介绍”小标题',
        'team': '团队介绍',
        'company_pdf': '公司资料文档',
    },
    'training': {
        'title': '页面标题',
        'subtitle': '页面副标题',
        'courses_title': '“课程介绍”小标题',
        'courses': '课程介绍',
        'instructors_title': '“师资力量”小标题',
        'instructors': '师资团队',
        'venue_title': '“培训场地”小标题',
        'venue': '培训场地',
        'gallery_title': '案例区标题',
    },
    'activities': {
        'title': '页面标题',
        'subtitle': '页面副标题',
        'performance': '无人机表演介绍',
        'science': '科普研学介绍',
        'aerial': '航拍服务介绍',
    },
    'activities_performance': {
        'detail_title': '详情页标题',
        'detail_subtitle': '详情页副标题',
        'detail_intro': '业务介绍',
        'gallery_title': '案例区标题',
    },
    'activities_science': {
        'detail_title': '详情页标题',
        'detail_subtitle': '详情页副标题',
        'detail_intro': '业务介绍',
        'gallery_title': '案例区标题',
    },
    'activities_aerial': {
        'detail_title': '详情页标题',
        'detail_subtitle': '详情页副标题',
        'detail_intro': '业务介绍',
        'gallery_title': '案例区标题',
    },
    'cases': {
        'title': '页面标题',
        'subtitle': '页面副标题',
    },
    'downloads': {
        'title': '页面标题',
        'subtitle': '页面副标题',
        'course_manual': '课程手册文档',
        'company_profile': '企业资料文档',
    },
    'contact': {
        'title': '页面标题',
        'subtitle': '页面副标题',
        'address': '公司地址',
        'phone': '联系电话',
        'wechat': '微信号',
        'email': '电子邮箱',
    },
}

# ============================================================
# 可固定上传图片的位置（key -> 中文名称）
# ============================================================
IMAGE_SLOTS = {
    'index': {
        'banner_1': '首页轮播图一',
        'banner_2': '首页轮播图二',
        'banner_3': '首页轮播图三',
        'performance_banner': '无人机表演滚屏背景图',
        'science_banner': '科普研学滚屏背景图',
        'aerial_banner': '航拍服务滚屏背景图',
    },
}

# ============================================================
# 可固定上传 PDF 的位置（key -> 中文名称）
# ============================================================
PDF_SLOTS = {
    'about': {
        'company_pdf': '公司资料文档',
    },
    'downloads': {
        'course_manual': '课程手册文档',
        'company_profile': '企业资料文档',
    },
}

# ============================================================
# 支持“新增图片”（自动生成编号，无需填写英文标识）的页面
# ============================================================
GALLERY_PAGES = {
    'training',
    'cases',
    'activities_performance',
    'activities_science',
    'activities_aerial',
}


def label_for(page, key, content_type='text'):
    """获取字段的中文名称，未登记的字段给出中文兜底名称"""
    label = KEY_LABELS.get(page, {}).get(key)
    if label:
        return label
    if content_type == 'image':
        return '案例图片'
    if content_type == 'pdf':
        return '文档'
    return '文字内容'
