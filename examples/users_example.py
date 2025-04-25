#!/usr/bin/env python3
"""
用户管理示例
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

    print("=== 获取所有用户 ===")
    users = client.users.list()
    print_json(users)

    print("\n=== 创建新用户 ===")
    new_user = client.users.create(
        username="testuser",
        password="password123",
        role="user",
        customization={"theme": "dark"}
    )
    print_json(new_user)

    user_id = new_user.get("id")
    if user_id:
        print(f"\n=== 获取用户 {user_id} 的详细信息 ===")
        user_details = client.users.get(user_id)
        print_json(user_details)

        print(f"\n=== 更新用户 {user_id} ===")
        updated_user = client.users.update(
            user_id=user_id,
            username="updated_testuser",
            customization={"theme": "light"}
        )
        print_json(updated_user)

        print(f"\n=== 删除用户 {user_id} ===")
        delete_result = client.users.delete(user_id)
        print_json(delete_result)

    print("\n=== 获取所有 API 密钥 ===")
    api_keys = client.users.get_api_keys()
    print_json(api_keys)

    print("\n=== 创建新 API 密钥 ===")
    new_api_key = client.users.create_api_key(
        name="测试 API 密钥",
        expires_at="2025-12-31T23:59:59Z"
    )
    print_json(new_api_key)

    key_id = new_api_key.get("id")
    if key_id:
        print(f"\n=== 删除 API 密钥 {key_id} ===")
        delete_key_result = client.users.delete_api_key(key_id)
        print_json(delete_key_result)


if __name__ == "__main__":
    main()
