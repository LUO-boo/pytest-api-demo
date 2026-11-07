# -*- coding: utf-8 -*-
"""
测试启动文件
作用：运行测试并生成Allure报告

使用方法：
python run.py
"""

import os
import sys
import subprocess
from common.logger import logger


def run_all_tests():
    """运行所有测试"""

    # 检查配置文件是否存在
    if not os.path.exists("config/env.yaml"):
        logger.error("❌ 配置文件不存在！")
        logger.error("请复制 config/env.yaml.example 为 config/env.yaml 并填写")
        return 1

    # 1. 运行测试
    logger.info("=" * 50)
    logger.info("🚀 开始执行自动化测试...")
    logger.info("=" * 50)

    result = subprocess.run([
        sys.executable, "-m", "pytest",
        "-vs",
        "--alluredir=./report/json",
        "--clean-alluredir",
        "testcases/"
    ])

    # 2. 生成报告
    logger.info("📊 生成测试报告...")

    os.makedirs("./report/html", exist_ok=True)

    subprocess.run([
        "allure", "generate",
        "./report/json",
        "-o", "./report/html",
        "--clean"
    ])

    # 3. 打开报告
    logger.info("🌐 打开报告...")
    subprocess.Popen(["allure", "open", "./report/html"])

    logger.info("✅ 测试完成！")

    return result.returncode


if __name__ == '__main__':
    exit_code = run_all_tests()
    sys.exit(exit_code)