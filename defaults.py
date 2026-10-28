# -*- coding: utf-8 -*-
"""
各页面默认内容
仅在数据库内容表为空（首次启动）时写入。
每个页面单独一块，方便按页面增删字段。
"""

# 结构：(页面标识, 内容key, 类型, 默认值)
DEFAULT_CONTENTS = [
    # ==================== 首页 ====================
    ('index', 'hero_title', 'text', '专业无人机综合服务商'),
    ('index', 'hero_subtitle', 'text', '无人机培训 · 活动表演 · 航拍服务 · 科普研学'),
    ('index', 'intro_text', 'text', '我们致力于为政府、企业及教育机构提供专业的无人机一站式解决方案，拥有资深飞手团队与完善的培训体系。'),
    ('index', 'about_title', 'text', '关于我们'),
    ('index', 'services_title', 'text', '业务服务'),
    ('index', 'services_subtitle', 'text', '专业的无人机综合服务，覆盖培训、表演、航拍与科普'),
    ('index', 'training_card_title', 'text', '无人机培训'),
    ('index', 'training_card_subtitle', 'text', 'AOPA认证 · 驾驶员/机长培训'),
    ('index', 'training_card_intro', 'text', '从零基础到持证飞手，完善课程体系与实操场地。'),
    ('index', 'activities_card_title', 'text', '无人机活动'),
    ('index', 'activities_card_subtitle', 'text', '表演 · 航拍 · 科普研学'),
    ('index', 'activities_card_intro', 'text', '灯光秀、影视航拍与青少年研学，一站式活动服务。'),
    ('index', 'banner_1', 'image', ''),
    ('index', 'banner_2', 'image', ''),
    ('index', 'banner_3', 'image', ''),
    # 三个业务滚屏（图片可选，标题与副标题可在后台修改）
    ('index', 'performance_banner', 'image', ''),
    ('index', 'performance_banner_title', 'text', '无人机表演'),
    ('index', 'performance_banner_subtitle', 'text', '数百至数千架无人机编队，点亮夜空'),
    ('index', 'science_banner', 'image', ''),
    ('index', 'science_banner_title', 'text', '科普研学'),
    ('index', 'science_banner_subtitle', 'text', '无人机科普课堂 · 飞行体验 · 研学营'),
    ('index', 'aerial_banner', 'image', ''),
    ('index', 'aerial_banner_title', 'text', '航拍服务'),
    ('index', 'aerial_banner_subtitle', 'text', '影视航拍 · 活动跟拍 · 测绘航测'),

    # ==================== 公司介绍 ====================
    ('about', 'title', 'text', '公司介绍'),
    ('about', 'subtitle', 'text', '企业背景 · 公司资质 · 团队介绍'),
    ('about', 'company_name', 'text', '某某无人机科技有限公司'),
    ('about', 'background_title', 'text', '企业背景'),
    ('about', 'background', 'text', '公司成立于2018年，专注于无人机行业应用与人才培养，是一家集研发、培训、服务于一体的高新技术企业。'),
    ('about', 'qualification_title', 'text', '公司资质'),
    ('about', 'qualification', 'text', '中国AOPA认证培训机构 · 民用无人机驾驶员考试点 · 高新技术企业 · ISO9001质量体系认证'),
    ('about', 'team_title', 'text', '团队介绍'),
    ('about', 'team', 'text', '核心团队由资深无人机飞手、航空航天专业工程师及教育专家组成，平均行业经验超过8年。'),
    ('about', 'company_pdf', 'pdf', ''),

    # ==================== 无人机培训业务 ====================
    ('training', 'title', 'text', '无人机培训业务'),
    ('training', 'subtitle', 'text', '中国AOPA认证培训机构，专业无人机驾驶员/机长培养'),
    ('training', 'courses_title', 'text', '课程介绍'),
    ('training', 'courses', 'text',
     '• 多旋翼驾驶员视距内（驾驶员）合格证培训\n'
     '• 多旋翼驾驶员超视距（机长）合格证培训\n'
     '• 植保无人机应用培训\n'
     '• 航拍与航测专项培训\n'
     '• 青少年无人机科普课程'),
    ('training', 'instructors_title', 'text', '师资力量'),
    ('training', 'instructors', 'text', '师资团队均持有中国AOPA颁发的教员合格证，拥有丰富的飞行与教学经验，累计培养学员2000+。'),
    ('training', 'venue_title', 'text', '培训场地'),
    ('training', 'venue', 'text', '培训基地占地50亩，配备室内理论教室、模拟飞行室、室外飞行训练场，可同时容纳100名学员训练。'),
    ('training', 'gallery_title', 'text', '培训案例'),

    # ==================== 无人机活动服务 ====================
    ('activities', 'title', 'text', '无人机活动服务'),
    ('activities', 'subtitle', 'text', '无人机表演 · 航拍服务 · 科普研学'),
    ('activities', 'performance', 'text', '无人机灯光表演：数百至数千架无人机编队，打造震撼夜空秀，适用于大型活动、庆典、品牌发布。'),
    ('activities', 'science', 'text', '科普研学：面向中小学及高校的无人机科普课堂、飞行体验、研学营，激发科技兴趣。'),
    ('activities', 'aerial', 'text', '航拍服务：专业航拍团队，提供活动跟拍、影视航拍、测绘航测等高质量影像服务。'),

    # ==================== 三个业务详情页（对应前台“活动案例”详情） ====================
    ('activities_performance', 'detail_title', 'text', '无人机表演'),
    ('activities_performance', 'detail_subtitle', 'text', '夜空编队灯光秀'),
    ('activities_performance', 'detail_intro', 'text',
     '数百至数千架无人机编队升空，配合音乐与灯光编程，呈现震撼的夜空视觉盛宴。'
     '适用于大型庆典、品牌发布、文旅活动等场景，可按需求定制图案与文字方案。'),
    ('activities_performance', 'gallery_title', 'text', '表演案例'),

    ('activities_science', 'detail_title', 'text', '科普研学'),
    ('activities_science', 'detail_subtitle', 'text', '无人机科普课堂与研学体验'),
    ('activities_science', 'detail_intro', 'text',
     '面向中小学及高校的无人机科普课程、飞行体验与研学营。'
     '通过理论讲解与动手实操，让青少年了解无人机原理与行业应用，激发科技兴趣。'),
    ('activities_science', 'gallery_title', 'text', '研学案例'),

    ('activities_aerial', 'detail_title', 'text', '航拍服务'),
    ('activities_aerial', 'detail_subtitle', 'text', '专业航拍与影视跟拍'),
    ('activities_aerial', 'detail_intro', 'text',
     '专业飞手团队提供活动跟拍、影视航拍、测绘航测等服务，'
     '配备高清航拍与测绘设备，输出高质量影像作品与数据成果。'),
    ('activities_aerial', 'gallery_title', 'text', '航拍案例'),

    # ==================== 项目案例 ====================
    ('cases', 'title', 'text', '项目案例'),
    ('cases', 'subtitle', 'text', '无人机活动与培训实拍记录'),

    # ==================== 资料下载 ====================
    ('downloads', 'title', 'text', '资料下载'),
    ('downloads', 'subtitle', 'text', '课程手册、企业资料等 PDF 文档，点击即可下载'),
    ('downloads', 'course_manual', 'pdf', ''),
    ('downloads', 'company_profile', 'pdf', ''),

    # ==================== 联系我们 ====================
    ('contact', 'title', 'text', '联系我们'),
    ('contact', 'subtitle', 'text', '欢迎通过以下方式与我们取得联系'),
    ('contact', 'address', 'text', '北京市海淀区中关村科技园XX路XX号'),
    ('contact', 'phone', 'text', '400-888-8888'),
    ('contact', 'wechat', 'text', 'DroneService2024'),
    ('contact', 'email', 'text', 'contact@drone-company.com'),
]
