# -*- coding: utf-8 -*-
"""
测试用例
作用：测试标题生成和确认的业务流程
"""

import pytest
import allure
from api.superboss_api import generate_title, confirm_title
from common.assertions import check_complete_success, check_status_code
from common.logger import logger


@allure.feature("标题优化")
@allure.story("标题生成与确认")
class TestTitleFlow:
    """标题优化流程测试"""

    @allure.title("单条商品标题生成和确认")
    @allure.severity(allure.severity_level.NORMAL)
    def test_single_product(self, api_config):
        """
        测试单条商品：生成标题 -> 确认标题
        """
        base_url = api_config["base_url"]
        headers = api_config["headers"]

        # 准备测试数据
        product_data = [
            {
                "productId": "1096424368652",
                "originalTitle": "女士优雅花朵抓夹",
                "titleLength": "60",
                "type": "1"
            }
        ]

        # 1. 调用生成标题接口
        with allure.step("生成标题"):
            response = generate_title(base_url, headers, product_data)
            check_status_code(response, 200)

            # 提取生成结果
            result = response.json()
            first_product = result["data"]["list"][0]
            new_title = first_product["generatedTitle"]
            record_id = first_product["recordId"]
            product_id = first_product["productId"]

            logger.info(f"生成的标题: {new_title}")

        # 2. 准备确认数据（注意字段映射）
        with allure.step("准备确认数据"):
            confirm_data = [
                {
                    "numIid": product_id,      # productId -> numIid
                    "title": new_title,
                    "recordId": record_id
                }
            ]

        # 3. 调用确认标题接口
        with allure.step("确认标题"):
            response = confirm_title(base_url, headers, confirm_data)
            check_complete_success(response)

        logger.info("✅ 单条商品测试通过！")

    @allure.title("批量商品标题生成和确认")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_batch_products(self, api_config):
        """
        测试批量商品：生成标题 -> 数据清洗 -> 确认标题
        """
        base_url = api_config["base_url"]
        headers = api_config["headers"]

        # 准备批量数据
        products_data = [
            {
                "productId": "1046102085606",
                "originalTitle": "可移动桌面增高架",
                "titleLength": "60",
                "type": "1"
            },
            {
                "productId": "1044401047726",
                "originalTitle": "女士亲肤针织衫",
                "titleLength": "60",
                "type": "1"
            }
        ]

        # 1. 批量生成标题
        with allure.step("批量生成标题"):
            response = generate_title(base_url, headers, products_data)
            check_status_code(response, 200)

            result_list = response.json()["data"]["list"]
            logger.info(f"成功生成 {len(result_list)} 个标题")

        # 2. 数据清洗（重要！生成接口和确认接口字段名不一样）
        with allure.step("数据清洗"):
            clean_data = []
            for product in result_list:
                clean_data.append({
                    "numIid": product["productId"],        # 字段改名
                    "title": product["generatedTitle"],    # 新标题
                    "recordId": product["recordId"]
                })

        # 3. 批量确认标题
        with allure.step("批量确认标题"):
            response = confirm_title(base_url, headers, clean_data)
            check_complete_success(response)

            # 额外检查：确保没有全部失败
            result = response.json()
            message = result.get("subMessage", "")
            if "成功0个" in message:
                logger.error("❌ 所有商品都失败了！")
                raise AssertionError("所有商品都失败了")
            else:
                logger.info(f"✅ 批量确认成功: {message}")

        logger.info("✅ 批量商品测试通过！")