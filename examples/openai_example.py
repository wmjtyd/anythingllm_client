#!/usr/bin/env python3
"""
OpenAI 兼容功能示例
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
    
    print("=== 获取所有模型（工作区） ===")
    models = client.openai.list_models()
    print_json(models)
    
    if models:
        model_id = models[0].get("model")
        print(f"\n=== 使用模型 {model_id} 创建聊天完成 ===")
        completion = client.openai.create_chat_completion(
            model=model_id,
            messages=[
                {"role": "system", "content": "你是一个专业的助手。"},
                {"role": "user", "content": "你好，请介绍一下 AnythingLLM。"}
            ],
            temperature=0.7
        )
        print_json(completion)
    
    print("\n=== 获取所有向量数据库集合 ===")
    vector_stores = client.openai.list_vector_stores()
    print_json(vector_stores)
    
    print("\n=== 创建嵌入向量 ===")
    embedding = client.openai.create_embedding(
        input_text="这是一个测试文本，用于获取嵌入向量。"
    )
    print_json(embedding)


if __name__ == "__main__":
    main()
