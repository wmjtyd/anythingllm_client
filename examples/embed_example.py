#!/usr/bin/env python3
"""
嵌入功能示例
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

    print("=== 获取文本嵌入向量 ===")
    text = "这是一个测试文本，用于获取嵌入向量。"
    embedding = client.embed.get_text_embedding(text)
    print(f"文本: {text}")
    print(f"嵌入向量维度: {len(embedding.get('embedding', []))}")

    print("\n=== 批量获取文本嵌入向量 ===")
    texts = [
        "这是第一个测试文本。",
        "这是第二个测试文本。",
        "这是第三个测试文本。"
    ]
    batch_embeddings = client.embed.get_batch_embeddings(texts)
    print(f"文本数量: {len(texts)}")

    embeddings = batch_embeddings.get("embeddings", [])
    for i, embedding in enumerate(embeddings):
        print(f"文本 {i+1} 嵌入向量维度: {len(embedding)}")


if __name__ == "__main__":
    main()
