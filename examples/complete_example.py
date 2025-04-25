#!/usr/bin/env python3
"""
完整的 AnythingLLM 客户端使用示例
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

    print("=== 检查系统健康状态 ===")
    health = client.system.get_health()
    print_json(health)

    print("\n=== 创建工作区 ===")
    workspace = client.workspaces.create(
        name="完整示例工作区",
        description="用于展示完整 API 功能的工作区"
    )
    print_json(workspace)

    workspace_id = workspace.get("id") or workspace.get("slug")

    print("\n=== 创建文档文件夹 ===")
    folder = client.documents.create_folder(name="示例文件夹")
    print_json(folder)

    # 上传示例文档
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

    document_id = document.get("id")

    print("\n=== 获取工作区文档 ===")
    workspace_documents = client.workspaces.get_documents(workspace_id)
    print_json(workspace_documents)

    print("\n=== 创建对话线程 ===")
    thread = client.chat.create_thread(
        workspace_id=workspace_id,
        name="示例对话",
        description="完整示例中的对话线程"
    )
    print_json(thread)

    thread_id = thread.get("id")

    print("\n=== 发送聊天消息 ===")
    chat_response = client.chat.send_message(
        workspace_id=workspace_id,
        thread_id=thread_id,
        message="请总结一下我上传的文档内容",
        temperature=0.7,
        include_sources=True
    )
    print_json(chat_response)

    print("\n=== 获取聊天历史 ===")
    chat_history = client.chat.get_history(
        workspace_id=workspace_id,
        thread_id=thread_id
    )
    print_json(chat_history)

    print("\n=== 发送后续问题 ===")
    follow_up_response = client.chat.send_message(
        workspace_id=workspace_id,
        thread_id=thread_id,
        message="AnythingLLM 有哪些主要功能？",
        temperature=0.7
    )
    print_json(follow_up_response)

    print("\n=== 获取更新后的聊天历史 ===")
    updated_chat_history = client.chat.get_history(
        workspace_id=workspace_id,
        thread_id=thread_id
    )
    print_json(updated_chat_history)

    # 清理资源
    print("\n=== 清理资源 ===")

    print("删除对话线程...")
    client.chat.delete_thread(workspace_id, thread_id)

    print("删除文档...")
    if document_id:
        client.documents.delete(document_id)

    print("删除工作区...")
    client.workspaces.delete(workspace_id)

    folder_id = folder.get("id")
    if folder_id:
        print("删除文件夹...")
        client.documents.delete_folder(folder_id)

    print("\n=== 完成 ===")


if __name__ == "__main__":
    main()
