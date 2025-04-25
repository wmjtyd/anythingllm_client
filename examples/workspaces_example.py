#!/usr/bin/env python3
"""
工作区管理示例
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

    print("\n=== 获取所有工作区 ===")
    workspaces = client.workspaces.list()
    print_json(workspaces)

    print("\n=== 创建新工作区 ===")
    new_workspace = client.workspaces.create(
        name="测试工作区",
        description="这是一个通过 Python 客户端创建的测试工作区"
    )
    print_json(new_workspace)

    workspace_id = new_workspace.get("id") or new_workspace.get("slug")

    print(f"\n=== 获取工作区 {workspace_id} 的详细信息 ===")
    workspace_details = client.workspaces.get(workspace_id)
    print_json(workspace_details)

    print(f"\n=== 更新工作区 {workspace_id} ===")
    updated_workspace = client.workspaces.update(
        workspace_id=workspace_id,
        name="更新后的测试工作区",
        description="这是一个已更新的测试工作区描述"
    )
    print_json(updated_workspace)

    print(f"\n=== 获取工作区 {workspace_id} 的文档 ===")
    documents = client.workspaces.get_documents(workspace_id)
    print_json(documents)

    print(f"\n=== 删除工作区 {workspace_id} ===")
    delete_result = client.workspaces.delete(workspace_id)
    print_json(delete_result)


if __name__ == "__main__":
    main()
