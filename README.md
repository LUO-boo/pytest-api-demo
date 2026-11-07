# 接口自动化测试框架

> 基于 Python + Pytest + Allure 的轻量级接口自动化测试框架

---

## 📖 项目背景

在电商业务中，标题优化是高频操作，每次发版都需要回归验证。手工执行耗时久、易遗漏，因此搭建了这个轻量级接口自动化框架，用于核心业务流程的回归测试。

**解决问题：**
- 手工回归测试耗时长（约 2 小时）
- 重复执行容易遗漏
- 测试数据管理混乱

---

## 🏗️ 架构设计

采用分层设计，职责清晰：

```
┌─────────────────────────────────┐
│         testcases/              │  ← 用例层：测试步骤和业务场景
│   └── test_data/ (YAML)         │  ← 数据层：测试数据独立管理
├─────────────────────────────────┤
│           api/                  │  ← 接口层：统一封装所有接口
├─────────────────────────────────┤
│          common/                │  ← 工具层：日志、断言、请求
├─────────────────────────────────┤
│          config/                │  ← 配置层：环境配置与代码分离
└─────────────────────────────────┘
```

**分层的好处：**
- 接口变更只需改 `api/` 层
- 测试数据用 YAML 管理，改数据不改代码
- 工具函数复用，减少重复代码

---

## ✨ 框架特点

| 特点 | 说明 |
|------|------|
| 分层设计 | API层、工具层、用例层清晰分离，维护成本低 |
| 数据驱动 | 测试数据 YAML 管理，与代码分离 |
| 失败重试 | 自动重试失败用例，减少网络波动误报 |
| 可视化报告 | Allure 报告，步骤、日志、断言一目了然 |
| 日志系统 | 控制台实时显示 + 文件持久化 |
| 环境隔离 | 配置文件不提交，避免敏感信息泄露 |

---

## 🛠️ 技术栈

| 技术 | 用途 | 选型理由 |
|------|------|---------|
| Python 3.8+ | 编程语言 | 生态丰富，易上手 |
| Pytest | 测试框架 | 语法简洁，插件丰富，Fixture 灵活 |
| Requests | HTTP 请求 | 简单直观，功能完善 |
| PyYAML | 配置解析 | 格式清晰，易于维护 |
| Allure | 测试报告 | 可视化效果好，支持步骤和附件 |
| pytest-rerunfailures | 失败重试 | 减少误报，提高稳定性 |

---

## 📁 目录结构

```
├── api/                    # 接口封装层
│   └── superboss_api.py    # 业务接口（生成标题、确认标题）
├── common/                 # 工具层
│   ├── utils.py            # 基础工具（YAML读取、HTTP请求）
│   ├── logger.py           # 日志工具（控制台+文件）
│   └── assertions.py       # 断言工具（状态码、业务断言）
├── config/                 # 配置层
│   ├── env.yaml.example    # 环境配置模板
│   └── env_config.py       # 配置管理
├── testcases/              # 用例层
│   ├── test_flow.py        # 业务流程测试
│   └── test_data/          # 测试数据
│       └── title_data.yaml
├── report/                 # 测试报告（自动生成）
├── logs/                   # 日志文件（自动生成）
├── conftest.py             # Pytest 全局配置
├── pytest.ini              # Pytest 配置
├── requirements.txt        # 依赖管理
└── run.py                  # 测试入口
```

---

## 🚀 快速开始

### 1. 环境准备

- Python 3.8+
- [Allure 命令行工具](https://github.com/allure-framework/allure2/releases)

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 配置环境

```bash
# 复制配置模板
cp config/env.yaml.example config/env.yaml

# 编辑 env.yaml，填写接口地址和登录凭证
```

### 4. 运行测试

```bash
# 方式1：使用入口脚本
python run.py

# 方式2：直接使用 pytest
pytest testcases/
```

### 5. 查看报告

```bash
allure open ./report/html
```

---

## 📊 测试报告示例

Allure 报告包含：
- 测试统计（通过率、失败率）
- 用例详情（步骤、请求参数、响应数据）
- 失败原因分析
- 功能模块分类

---

## 🔧 常用命令

```bash
# 运行所有测试
pytest testcases/

# 运行指定文件
pytest testcases/test_flow.py

# 按关键字过滤
pytest -k "single"

# 跳过失败用例
pytest --lf

# 生成并查看报告
allure serve ./report/json
```

---

## 💡 使用示例

### 添加新接口

在 `api/superboss_api.py` 中添加：

```python
def new_api(base_url, headers, payload):
    """新接口"""
    url = f"{base_url}/new/endpoint"
    return send_post_request(url, payload, headers)
```

### 添加新用例

在 `testcases/` 目录下创建测试文件：

```python
import allure
from api.superboss_api import new_api
from common.assertions import check_complete_success

@allure.feature("新功能")
class TestNewFeature:
    @allure.title("测试新接口")
    def test_new_api(self, api_config):
        base_url = api_config["base_url"]
        headers = api_config["headers"]

        response = new_api(base_url, headers, {"key": "value"})
        check_complete_success(response)
```

---

## 📝 注意事项

1. `config/env.yaml` 包含敏感信息，已加入 `.gitignore`，不会提交到代码库
2. `report/` 和 `logs/` 是自动生成目录，不需要提交
3. Cookie 过期后需要手动更新 `config/env.yaml`

---

**版本**：v1.0
**更新日期**：2026-11-07