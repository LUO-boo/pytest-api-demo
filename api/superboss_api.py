# -*- coding: utf-8 -*-
"""
接口封装
作用：统一管理接口地址，测试用例直接调用
"""

from common.utils import send_post_request
from common.logger import logger


def generate_title(base_url, headers, product_list):
    """
    生成标题接口

    参数：
    - base_url: 系统地址（从配置读取）
    - headers: 请求头（包含Cookie）
    - product_list: 商品列表
    """
    url = f"{base_url}/title/generate"
    logger.info(f"📝 生成标题: {len(product_list)}个")
    return send_post_request(url, product_list, headers)


def confirm_title(base_url, headers, title_list):
    """
    确认标题接口

    参数：
    - base_url: 系统地址
    - headers: 请求头
    - title_list: 标题列表
    """
    url = f"{base_url}/title/updateItemTitle"
    logger.info(f"✓ 确认标题: {len(title_list)}个")
    return send_post_request(url, title_list, headers)