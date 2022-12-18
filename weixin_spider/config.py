'''
Author: CalmCapK
Date: 2022-09-26 03:18:24
LastEditors: Please set LastEditors
LastEditTime: 2022-11-14 01:33:27
'''
cihui = [
    'yolo', 'MLP', 'Transformer', 'ViT', 'GAN', 'LLVM', 'DALL', 'CLIP', 'prompt', 'dert', 'MAE', 'gpt', 'VGG', 'FPN', 'VAE', 'ResNet', 'ImageNet', 'SSD', 'diffusion',
    'Attention', '注意力', '全局', '局部',
    '多模态', '跨模态', '跨域', 'Domain','自适应', '多任务',
    '大规模', '预训练', '迁移学习', 'representation', '表征', '特征', '大模型',
    'contrastive', '对比', '度量', '相似', 
    '泛化', '鲁棒','distribution', 'overconfidence', 
    'Few-shot','少样本', '小样本', '负样本', '零样本', '长尾', 
    '无监督', '自监督','半监督','全监督', '文本监督', '弱监督',
    
    '分割', 'segmentation', '检测','detection','识别', '分类','标签', '细粒度', 'Anchor','回归','图像处理',
    '人脸', '文档','手写', 'SLAM','光流','双流', 'mask',
    '视频', '时序预测', '时间序列预测','运动预测','跟踪',
    '深度估计', '传感器', '动态环境', '3D', '三维', '姿态', '估计', '重建','纹理',
    'synthesis', '合成',  '生成', '扩散', '风格', '迁移', '作画',
    '恢复', '修复', '补全', '去噪', '超分', '分辨率', 
    'Adversarial', '对抗', '攻击', '可解释',
    '开集识别', 'Closed-Set', 
    '自动驾驶','感知',
    '医学图像', '医疗',
    '语言模型','多语言','问答', 
    '数据挖掘','爬取','抽取',
    '图神经',  
    '推荐', 
    '检索', '搜索',
    '相机', '摄像', '摄影', '影像', '白平衡', 'ISP', '3A', 'HDR', '非视线成像',
    '理解', 
    '安全',
    '蛋白', 

    'IoU', '损失', 'ROC','距离',
    '马尔可夫', '分布','梯度', '熵','先验',
    '正则化','卷积','池化', 'batch', 'ReLU', '激活函数','Sigmoid', '超参', '优化器', 'optim',
    '基线', 'backbone','sota',
    
    '蒸馏', '压缩', '剪枝', '量化', '轻量级','GPU', '显卡','速度', '加速', '快','A100',
    '框架', '架构', '部署','分布式',
    
    '增强','交互', '抠图', '机器人','增量', '联邦', '范式',
    
    '顶会', '综述','Oral', 
    'CVPR', 'ICML', 'OSDI', 'ICLR', 'IJCAI', 'TPAMI', 'ECCV', 'NeurIPS', 'PRCV', 'Nature', 'NIPS', 'TIP', 'IEEE','ILSVRC', 'AAAI', 'COLING', 'CIKM', 'VLDB',
    '谷歌', '何恺明', '华为', '英伟达', 'MSRA', '亚马逊', 'Meta', '微软', '苹果','nvidia',
    
    'github','开源', 'kaggle','leetcode',
    '配置','代码', '手把手', '数据',
    '云计算',  'AI', 'pytorch', 'opencv','Matplotlib',
    '每日', '回顾', '解读','经典', '讲座', '大赛','大会', '进展', '实验室', '研究院',
    '抄袭', '裁员', '毕业', '国企', '排名', '面试', '编制', '单位', '人才', '公务员', '研究员', '招聘', '岗位', '内推', '实习', '算法岗', '课题组', '招收', '基金', '项目', '招生', '上岸',
]
global_cnt = 50
global_token = '228422115'
globel_cookie = 'appmsglist_action_3879859384=card; RK=C/2NjrxBMh; ptcz=30c453d3718f08a4550ef4a9815730bfab570de6b0dfd2c0dc27e62e02cedebe; ua_id=k6yXDooqC7mt04RBAAAAABgqWq_ng68Z62M-zF-tJIM=; wxuin=64115639033196; mm_lang=zh_CN; pgv_pvid=3335243978; ptui_loginuin=1557519267@qq.com; open_id=A815483F0EF019E4E52BBD1A59692D38; tvfe_boss_uuid=3f41a80f6f2d2ef6; _clck=3879859384|1|f6i|0; uuid=1e5498847c3393407284df6bf6f9e729; rand_info=CAESICGpzoBIC7z7myghF5/35pG+NYcJco7a3TznTZLC8955; slave_bizuin=3879859384; data_bizuin=3879859384; bizuin=3879859384; data_ticket=/lNR6cZyJmivzGQP989mIc2GheXriEfa5b4MlVyWgCyii88qT44lBJK/htQ1CKln; slave_sid=S3ZaWG1tRURtVGtXaV9qZnRrRzBwOWphQnBhN3NXRGxzU0dTSjUwT2ZnNVhoWUtNNldtS3FkTXFvX2pScm9UaDFsamplVlE0cG9mWldMYVowVk5uQ28xSWNtalo0VUFEcGhvRzM0V3NkR3VXVlVKc2VOSktWd3N6WFk0bmVFYmd4OU9VNFJ0cVEzNWZiUU52; slave_user=gh_e5c22d354bac; xid=9f37f67a0e269f35dc4cc59b346fcaac' 
gongzhonghao_list = [
    {"name": 'AI算法与图像处理',"fakeid": "MzU4NTY4Mzg1Mw==","cnt": 64,"begin": "4"},
    {"name": 'GiantPandaCV',"fakeid": "MzA4MjY4NTk0NQ==","cnt": 51,"begin": "11"},
    {"name": 'VALSE',"fakeid": "MzA3Mjk0OTgyMg==","cnt": 51,"begin": "9"},
    {"name": 'arXiv每日学术速递',"fakeid": "Mzg4OTEwNjMzMA==","cnt": 67,"begin": "3"},
    {"name": '晓飞的算法工程笔记',"fakeid": "MzI3MzU5NjQyMQ==","cnt": 55,"begin": "11"},
    {"name": 'Smarter',"fakeid": "Mzg4MjQ1NzI0NA==","cnt": 50,"begin": "10"},

    {"name": '我爱计算机视觉',"fakeid": "MzIwMTE1NjQxMQ==","cnt": 55,"begin": "6"},
    {"name": '微软研究院AI头条',"fakeid": "MzAwMTA3MzM4Nw==","cnt": 53,"begin": "9"},
    {"name": '计算机视觉life',"fakeid": "MzIxOTczOTM4NA==","cnt": 58,"begin": "3"},
    {"name": '小白学视觉',"fakeid": "MzU0NjgzMDIxMQ==","cnt": 70,"begin": "3"},
    {"name": '计算机视觉研究院',"fakeid": "MzU0NTAyNTQ1OQ==","cnt": 58,"begin": "7"},
    {"name": 'AIWalker',"fakeid": "MzIyMjIxNDk3OA==","cnt": 55,"begin": "8"},
    
    {"name": 'CVer',"fakeid": "MzUxNjcxMjQxNg==","cnt": 68,"begin": "4"},
    {"name": '人工智能前沿讲习',"fakeid": "MzIzNjc0MTMwMA==","cnt": 55,"begin": "5"},
    {"name": '机器学习算法与自然语言处理',"fakeid": "MzI4MDYzNzg4Mw==","cnt": 71,"begin": "4"},
    {"name": '深度学习与NLP',"fakeid": "MzIxNDgzNDg3NQ==","cnt": 42,"begin": "2"},

    {"name": '医学图像计算青年研讨会',"fakeid": "MzU1ODc4Mjg1Mw==","cnt": 52,"begin": "10"},
    {"name": '深度学习与图网络',"fakeid": "MzUyNzcyNzE0Mg==","cnt": 56,"begin": "5"},
    {"name": 'AI有道',"fakeid": "MzIwOTc2MTUyMg==","cnt": 58,"begin": "4"},
    {"name": 'OpenCV学堂',"fakeid": "MzA4MDExMDEyMw==","cnt": 53,"begin": "6"},
    {"name": '3D视觉工坊',"fakeid": "MzU1MjY4MTA1MQ==","cnt": 59,"begin": "3"},
    {"name": '极市平台',"fakeid": "MzI5MDUyMDIxNA==","cnt": 62,"begin": "3"},
    {"name": '虎嗅APP',"fakeid": "MTQzMjE1NjQwMQ==","cnt": 53,"begin": "3"},
    {"name": '36氪',"fakeid": "MzI2NDk5NzA0Mw==","cnt": 58,"begin": "3"},
    {"name": '量子位',"fakeid": "MzIzNjc1NzUzMw==","cnt": 58,"begin": "2"},
    {"name": '新智元',"fakeid": "MzI3MTA0MTk1MA==","cnt": 65,"begin": "3"},
    {"name": '机器之心',"fakeid": "MzA3MzI4MjgzMw==","cnt": 74,"begin": "3"},
    {"name": '手机技术资讯',"fakeid": "MzA5MjI1OTAwMQ==","cnt": 56,"begin": "3"},
    {"name": '爱可可爱生活',"fakeid": "MzI2MTMxNzg1OA==","cnt": 60,"begin": "4"},
   
    {"name": '计算摄影学',"fakeid": "MzU4Njc4MzY4NQ==","cnt": 51,"begin": "10"},
    {"name": '自动驾驶之心',"fakeid": "Mzg2NzUxNTU1OA==","cnt": 65,"begin": "3"},
    {"name": 'FightingCV',"fakeid": "MzIzNzU4OTAxMQ==","cnt": 61,"begin": "2"},
    {"name": '深度学习爱好者',"fakeid": "MzU1OTYzNjg5OQ==","cnt": 58,"begin": "3"},
    {"name": '夕小瑶的卖萌屋',"fakeid": "MzIwNzc2NTk0NQ==","cnt": 56,"begin": "6"},
    {"name": '集智书童',"fakeid": "MzU5OTA2Mjk5Mw==","cnt": 53,"begin": "4"},

    {"name": '模板',"fakeid": "","cnt": 0,"begin": "0"},
]

ok_list = ["模板", "AI算法与图像处理", "GiantPandaCV", 'VALSE', 'arXiv每日学术速递', '晓飞的算法工程笔记', 'Smarter',
            '我爱计算机视觉','微软研究院AI头条','计算机视觉life','小白学视觉','计算机视觉研究院','AIWalker',
            'CVer','人工智能前沿讲习','机器学习算法与自然语言处理','深度学习与NLP',
            '医学图像计算青年研讨会','深度学习与图网络','AI有道','OpenCV学堂','3D视觉工坊','极市平台',
            '虎嗅APP','36氪','量子位','新智元','机器之心','手机技术资讯','爱可可爱生活',
]