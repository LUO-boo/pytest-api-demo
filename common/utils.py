# -*- coding: utf-8 -*-
"""
工具函数
作用：读取配置文件、发送HTTP请求
"""

import yaml
import requests
from common.logger import logger


def read_config(file_path):
    """读取YAML配置文件"""
    with open(file_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
        logger.info(f"✅ 读取配置: {file_path}")
        return config


def send_post_request(url, data, headers=None):
    """
    发送POST请求

    说明：
    - POST就是向服务器提交数据
    - 比如生成标题、确认标题这些操作
    """
    logger.info(f"📤 POST请求: {url}")

    response = requests.post(
        url=url,
        json=data,
        headers=headers,
        timeout=10
    )

    logger.info(f"📥 状态码: {response.status_code}")

    return response


def send_get_request(url, params=None, headers=None):
    """
    发送GET请求

    说明：
    - GET就是从服务器获取数据
    - 比如查询列表、查看详情
    """
    logger.info(f"📤 GET请求: {url}")

    response = requests.get(
        url=url,
        params=params,
        headers=headers,
        timeout=10
    )

    logger.info(f"📥 状态码: {response.status_code}")

    return response