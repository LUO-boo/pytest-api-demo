# -*- coding: utf-8 -*-
"""
日志工具
作用：记录测试过程，方便查问题
"""

import logging
import os

# 日志文件路径
log_dir = "logs"
log_file = "logs/test.log"

# 如果logs目录不存在就创建
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# 配置日志：同时打印在控制台和保存到文件
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler(),  # 控制台输出
        logging.FileHandler(log_file, encoding='utf-8')  # 保存到文件
    ]
)

logger = logging.getLogger()