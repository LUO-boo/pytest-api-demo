# -*- coding: utf-8 -*-
"""
断言工具
作用：检查接口返回是否符合预期
"""

from common.logger import logger


def check_status_code(response, expected_code=200):
    """检查状态码"""
    actual_code = response.status_code
    if actual_code == expected_code:
        logger.info(f"✅ 状态码: {actual_code}")
        return True
    else:
        logger.error(f"❌ 状态码错误: 期望{expected_code}, 实际{actual_code}")
        raise AssertionError(f"状态码错误")


def check_success(response_json):
    """检查success字段"""
    success = response_json.get("success")
    if success == True:
        logger.info("✅ success=True")
        return True
    else:
        logger.error(f"❌ success={success}")
        raise AssertionError("接口返回失败")


def check_not_empty(response_json, key):
    """检查字段不为空"""
    value = response_json.get(key)
    if value:
        logger.info(f"✅ {key}不为空")
        return True
    else:
        logger.error(f"❌ {key}为空")
        raise AssertionError(f"{key}为空")


def check_complete_success(response):
    """
    完整检查：状态码200 + success=True + data不为空
    最常用的断言，一步到位
    """
    check_status_code(response, 200)
    check_success(response.json())
    check_not_empty(response.json(), "data")
    logger.info("✅ 断言通过")
    return True


def check_title_length(response_json, max_length=60):
    """检查标题长度（业务要求不能超过60字符）"""
    title = response_json["data"]["list"][0]["generatedTitle"]

    if len(title) <= max_length:
        logger.info(f"✅ 标题长度: {len(title)}")
        return True
    else:
        logger.error(f"❌ 标题超长: {len(title)}")
        raise AssertionError("标题超长")