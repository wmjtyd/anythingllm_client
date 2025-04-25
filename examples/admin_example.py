#!/usr/bin/env python3
"""
管理员功能示例
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
    
    print("=== 检查多用户模式 ===")
    multi_user_mode = client.admin.is_multi_user_mode()
    print_json(multi_user_mode)
    
    # 如果不在多用户模式下，大多数管理员功能将不可用
    if not multi_user_mode.get("isMultiUser", False):
        print("\n系统不在多用户模式下，大多数管理员功能不可用。")
        return
    
    print("\n=== 获取系统偏好设置 ===")
    preferences = client.admin.get_system_preferences()
    print_json(preferences)
    
    print("\n=== 获取所有邀请码 ===")
    invites = client.admin.get_invites()
    print_json(invites)
    
    print("\n=== 创建新邀请码 ===")
    new_invite = client.admin.create_invite()
    print_json(new_invite)
    
    invite_id = new_invite.get("invite", {}).get("id")
    if invite_id:
        print(f"\n=== 删除邀请码 {invite_id} ===")
        delete_result = client.admin.delete_invite(invite_id)
        print_json(delete_result)
    
    print("\n=== 创建新用户 ===")
    new_user = client.admin.create_user(
        username="testadmin",
        password="password123",
        role="admin"
    )
    print_json(new_user)
    
    user_id = new_user.get("user", {}).get("id")
    if user_id:
        print(f"\n=== 更新用户 {user_id} ===")
        updated_user = client.admin.update_user(
            user_id=user_id,
            username="updated_testadmin",
            role="default"
        )
        print_json(updated_user)
        
        print(f"\n=== 删除用户 {user_id} ===")
        delete_result = client.admin.delete_user(user_id)
        print_json(delete_result)


if __name__ == "__main__":
    main()
