# -*- coding: utf-8 -*-
"""
Pytest全局配置
作用：定义全局fixture，给测试用例提供配置信息
"""

import pytest
from common.utils import read_config
from common.logger import logger

# 读取环境配置
env_config = read_config("config/env.yaml")
logger.info("✅ 环境配置加载成功")


@pytest.fixture(scope="session")
def api_config():
    """
    全局配置fixture

    说明：
    - scope="session"表示整个测试过程只执行一次
    - 所有测试用例共享这个配置
    - 测试用例在参数里写 api_config 就能直接使用
    """
    return {
        "base_url": env_config["base_url"],
        "headers": {
            "Cookie": env_config["cookie"],
            "Content-Type": "application/json"
        }
    }


def pytest_configure(config):
    """测试开始前执行"""
    logger.info("=" * 50)
    logger.info("🚀 开始执行测试")
    logger.info("=" * 50)


def pytest_unconfigure(config):
    """测试结束后执行"""
    logger.info("=" * 50)
    logger.info("🏁 测试执行完毕")
    logger.info("=" * 50)