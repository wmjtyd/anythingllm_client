#!/usr/bin/env python3
"""
工作区线程功能示例
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
        name="线程测试工作区",
        description="用于测试线程功能的工作区"
    )
    print_json(workspace)
    
    workspace_id = workspace.get("id") or workspace.get("slug")
    
    # 获取工作区的所有线程
    print(f"\n=== 获取工作区 {workspace_id} 的所有线程 ===")
    threads = client.workspace_thread.list_threads(workspace_id)
    print_json(threads)
    
    # 创建新线程
    print(f"\n=== 在工作区 {workspace_id} 中创建新线程 ===")
    thread = client.workspace_thread.create_thread(
        workspace_id=workspace_id,
        name="测试线程",
        description="这是一个测试线程"
    )
    print_json(thread)
    
    thread_id = thread.get("id")
    
    # 获取线程详情
    print(f"\n=== 获取线程 {thread_id} 的详细信息 ===")
    thread_details = client.workspace_thread.get_thread(workspace_id, thread_id)
    print_json(thread_details)
    
    # 发送消息到线程
    print(f"\n=== 向线程 {thread_id} 发送消息 ===")
    message = client.workspace_thread.send_message(
        workspace_id=workspace_id,
        thread_id=thread_id,
        message="你好，这是一条测试消息。",
        temperature=0.7
    )
    print_json(message)
    
    # 获取线程的所有消息
    print(f"\n=== 获取线程 {thread_id} 的所有消息 ===")
    messages = client.workspace_thread.get_thread_messages(workspace_id, thread_id)
    print_json(messages)
    
    # 更新线程
    print(f"\n=== 更新线程 {thread_id} ===")
    updated_thread = client.workspace_thread.update_thread(
        workspace_id=workspace_id,
        thread_id=thread_id,
        name="更新后的测试线程",
        description="这是一个已更新的测试线程"
    )
    print_json(updated_thread)
    
    # 清除线程的所有消息
    print(f"\n=== 清除线程 {thread_id} 的所有消息 ===")
    clear_result = client.workspace_thread.clear_thread_messages(workspace_id, thread_id)
    print_json(clear_result)
    
    # 删除线程
    print(f"\n=== 删除线程 {thread_id} ===")
    delete_thread_result = client.workspace_thread.delete_thread(workspace_id, thread_id)
    print_json(delete_thread_result)
    
    # 删除测试工作区
    print(f"\n=== 删除测试工作区 {workspace_id} ===")
    delete_workspace_result = client.workspaces.delete(workspace_id)
    print_json(delete_workspace_result)


if __name__ == "__main__":
    main()
