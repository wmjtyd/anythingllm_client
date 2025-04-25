#!/usr/bin/env python3
"""
聊天功能示例
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

    # 创建一个测试工作区
    print("=== 创建测试工作区 ===")
    workspace = client.workspaces.create(
        name="聊天测试工作区",
        description="用于测试聊天功能的工作区"
    )
    print_json(workspace)

    workspace_id = workspace.get("id") or workspace.get("slug")

    # 创建一个对话线程
    print("\n=== 创建对话线程 ===")
    thread = client.chat.create_thread(
        workspace_id=workspace_id,
        name="测试对话",
        description="这是一个测试对话线程"
    )
    print_json(thread)

    thread_id = thread.get("id")

    # 发送消息
    print("\n=== 发送聊天消息 ===")
    chat_response = client.chat.send_message(
        workspace_id=workspace_id,
        thread_id=thread_id,
        message="你好，请介绍一下 AnythingLLM 的主要功能",
        temperature=0.7,
        include_sources=True
    )
    print_json(chat_response)

    # 获取聊天历史
    print("\n=== 获取聊天历史 ===")
    chat_history = client.chat.get_history(
        workspace_id=workspace_id,
        thread_id=thread_id
    )
    print_json(chat_history)

    # 获取所有对话线程
    print("\n=== 获取所有对话线程 ===")
    threads = client.chat.list_threads(workspace_id=workspace_id)
    print_json(threads)

    # 更新对话线程
    print("\n=== 更新对话线程 ===")
    updated_thread = client.chat.update_thread(
        workspace_id=workspace_id,
        thread_id=thread_id,
        name="更新后的测试对话",
        description="这是一个已更新的测试对话线程"
    )
    print_json(updated_thread)

    # 清除聊天历史
    print("\n=== 清除聊天历史 ===")
    clear_result = client.chat.clear_history(
        workspace_id=workspace_id,
        thread_id=thread_id
    )
    print_json(clear_result)

    # 删除对话线程
    print("\n=== 删除对话线程 ===")
    delete_thread_result = client.chat.delete_thread(
        workspace_id=workspace_id,
        thread_id=thread_id
    )
    print_json(delete_thread_result)

    # 删除测试工作区
    print("\n=== 删除测试工作区 ===")
    delete_workspace_result = client.workspaces.delete(workspace_id)
    print_json(delete_workspace_result)


if __name__ == "__main__":
    main()
