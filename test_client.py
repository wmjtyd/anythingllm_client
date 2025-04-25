"""
测试 AnythingLLMClient 的基本功能
"""

from anythingllm_client import AnythingLLMClient

# 初始化客户端
client = AnythingLLMClient(
    base_url="http://localhost:3001",
    api_key="PM2XHGK-951MAPY-HJ1CC2V-V0ZKQ28"
)

# 测试获取系统健康状态
try:
    health = client.system.get_health()
    print(f"系统健康状态: {health}")
except Exception as e:
    print(f"获取系统健康状态时出错: {e}")

# 测试获取所有工作区
try:
    workspaces = client.workspaces.list()
    print(f"找到 {len(workspaces)} 个工作区")
    for workspace in workspaces:
        print(f"  - {workspace.get('name', 'Unknown')}")
except Exception as e:
    print(f"获取工作区列表时出错: {e}")
