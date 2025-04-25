#!/usr/bin/env python3
"""
系统设置示例
"""

import os
import sys
import json
from dotenv import load_dotenv

# 添加项目根目录到 Python 路径
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 使用正确的导入路径
from anythingllm_client.anythingllm_client import AnythingLLMClient

# 加载环境变量
load_dotenv()

# 配置
API_KEY = os.getenv("ANYTHINGLLM_API_KEY", "PM2XHGK-951MAPY-HJ1CC2V-V0ZKQ28")
BASE_URL = os.getenv("ANYTHINGLLM_BASE_URL", "http://localhost:3001")


def print_json(data):
    """美化打印 JSON 数据"""
    print(json.dumps(data, ensure_ascii=False, indent=2))


def main():
    """主函数"""
    # 初始化客户端
    client = AnythingLLMClient(base_url=BASE_URL, api_key=API_KEY)

    print("=== 获取系统健康状态 ===")
    health = client.system.get_health()
    print_json(health)

    print("\n=== 获取系统设置 ===")
    settings = client.system.get_settings()
    print_json(settings)

    print("\n=== 获取可用的 LLM 模型 ===")
    llm_models = client.system.get_llm_models()
    print_json(llm_models)

    print("\n=== 获取可用的嵌入模型 ===")
    embedding_models = client.system.get_embedding_models()
    print_json(embedding_models)

    print("\n=== 获取可用的向量数据库 ===")
    vector_dbs = client.system.get_vector_dbs()
    print_json(vector_dbs)

    print("\n=== 获取系统接受的文档类型 ===")
    document_types = client.system.get_accepted_document_types()
    print_json(document_types)

    print("\n=== 获取系统提示模板 ===")
    prompts = client.system.get_prompts()
    print_json(prompts)

    print("\n=== 创建系统提示模板 ===")
    new_prompt = client.system.create_prompt(
        title="测试提示模板",
        content="你是一个专业的助手，请帮助用户解答关于 {{documents}} 的问题。",
        description="用于测试的提示模板"
    )
    print_json(new_prompt)

    prompt_id = new_prompt.get("id")
    if prompt_id:
        print(f"\n=== 更新提示模板 {prompt_id} ===")
        updated_prompt = client.system.update_prompt(
            prompt_id=prompt_id,
            title="更新后的测试提示模板",
            content="你是一个专业的助手，请根据 {{documents}} 帮助用户解答问题。",
            description="这是一个已更新的测试提示模板"
        )
        print_json(updated_prompt)

        print(f"\n=== 删除提示模板 {prompt_id} ===")
        delete_result = client.system.delete_prompt(prompt_id)
        print_json(delete_result)


if __name__ == "__main__":
    main()
