# -*- coding: utf-8 -*-
"""
环境配置管理模块
"""
import os
from common.utils import read_config
from common.logger import logger


class EnvConfig:
    """环境配置管理类"""

    def __init__(self):
        config_file = "config/env.yaml"

        if not os.path.exists(config_file):
            logger.warning(f"⚠️ 配置文件 {config_file} 不存在")
            logger.warning("请复制 config/env.yaml.example 为 config/env.yaml 并填写")
            raise FileNotFoundError(f"请先配置 env.yaml")

        self.config = read_config(config_file)

    @property
    def base_url(self):
        return self.config.get("base_url")

    @property
    def headers(self):
        return {
            "Cookie": self.config.get("cookie", ""),
            "Content-Type": "application/json"
        }

    @property
    def timeout(self):
        return self.config.get("timeout", 10)


def get_env_config():
    return EnvConfig()