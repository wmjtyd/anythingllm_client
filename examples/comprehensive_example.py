#!/usr/bin/env python3
"""
综合示例：展示如何使用 AnythingLLM 客户端的所有功能
"""

import os
import sys
import json
import time
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
    
    print("=== 系统信息 ===")
    health = client.system.get_health()
    print_json(health)
    
    # 检查多用户模式
    print("\n=== 检查多用户模式 ===")
    multi_user_mode = client.admin.is_multi_user_mode()
    print_json(multi_user_mode)
    
    # 创建工作区
    print("\n=== 创建工作区 ===")
    workspace = client.workspaces.create(
        name="综合示例工作区",
        description="用于展示所有功能的工作区"
    )
    print_json(workspace)
    
    workspace_id = workspace.get("id") or workspace.get("slug")
    
    # 创建线程
    print(f"\n=== 在工作区 {workspace_id} 中创建线程 ===")
    thread = client.workspace_thread.create_thread(
        workspace_id=workspace_id,
        name="综合示例线程",
        description="用于展示线程功能的线程"
    )
    print_json(thread)
    
    thread_id = thread.get("id")
    
    # 发送消息到线程
    print(f"\n=== 向线程 {thread_id} 发送消息 ===")
    message = client.workspace_thread.send_message(
        workspace_id=workspace_id,
        thread_id=thread_id,
        message="你好，这是一条测试消息。请介绍一下 AnythingLLM 的主要功能。",
        temperature=0.7
    )
    print_json(message)
    
    # 获取线程消息
    print(f"\n=== 获取线程 {thread_id} 的消息 ===")
    messages = client.workspace_thread.get_thread_messages(workspace_id, thread_id)
    print_json(messages)
    
    # 使用 OpenAI 兼容 API
    print("\n=== 获取 OpenAI 兼容模型列表 ===")
    models = client.openai.list_models()
    print_json(models)
    
    if models:
        model_id = models[0].get("model")
        print(f"\n=== 使用 OpenAI 兼容 API 发送聊天请求 ===")
        completion = client.openai.create_chat_completion(
            model=model_id,
            messages=[
                {"role": "system", "content": "你是一个专业的助手。"},
                {"role": "user", "content": "请简要介绍一下 AnythingLLM。"}
            ],
            temperature=0.7
        )
        print_json(completion)
    
    # 获取向量存储
    print("\n=== 获取向量存储列表 ===")
    vector_stores = client.openai.list_vector_stores()
    print_json(vector_stores)
    
    # 上传文档示例
    # 注意：请将路径替换为实际的文档路径
    document_path = "examples/sample_document.txt"
    
    # 如果示例文档不存在，创建一个
    if not os.path.exists(document_path):
        os.makedirs(os.path.dirname(document_path), exist_ok=True)
        with open(document_path, "w", encoding="utf-8") as f:
            f.write("这是一个示例文档，用于测试 AnythingLLM API。\n")
            f.write("AnythingLLM 是一个强大的本地 LLM 应用程序，支持多种语言模型和文档处理功能。\n")
            f.write("它可以帮助用户构建基于文档的问答系统，实现知识库管理和智能对话。\n")
    
    print(f"\n=== 上传文档 {document_path} ===")
    document = client.documents.upload(
        file_path=document_path,
        add_to_workspaces=[workspace_id]
    )
    print_json(document)
    
    # 获取工作区文档
    print(f"\n=== 获取工作区 {workspace_id} 的文档 ===")
    workspace_documents = client.workspaces.get_documents(workspace_id)
    print_json(workspace_documents)
    
    # 使用嵌入功能
    print("\n=== 创建文本嵌入 ===")
    embedding = client.embed.get_text_embedding("这是一个测试文本，用于获取嵌入向量。")
    print(f"嵌入向量维度: {len(embedding.get('embedding', []))}")
    
    # 清理资源
    print("\n=== 清理资源 ===")
    
    # 删除线程
    print(f"删除线程 {thread_id}...")
    client.workspace_thread.delete_thread(workspace_id, thread_id)
    
    # 删除文档
    document_id = document.get("id")
    if document_id:
        print(f"删除文档 {document_id}...")
        client.documents.delete(document_id)
    
    # 删除工作区
    print(f"删除工作区 {workspace_id}...")
    client.workspaces.delete(workspace_id)
    
    print("\n=== 完成 ===")


if __name__ == "__main__":
    main()
