# AnythingLLM Python Client

一个用于与 AnythingLLM API 交互的 Python 客户端库。

## 安装

```bash
pip install -e .
```

## 使用方法

```python
from anythingllm_client import AnythingLLMClient

# 初始化客户端
client = AnythingLLMClient(
    base_url="http://localhost:3001",
    api_key="PM2XHGK-951MAPY-HJ1CC2V-V0ZKQ28"
)

# 获取所有工作区
workspaces = client.workspaces.list()
print(workspaces)

# 创建新工作区
new_workspace = client.workspaces.create(
    name="测试工作区",
    description="这是一个测试工作区"
)
print(f"创建的工作区: {new_workspace}")

# 上传文档
document = client.documents.upload(
    file_path="path/to/document.pdf",
    add_to_workspaces=["测试工作区"]
)
print(f"上传的文档: {document}")

# 发送聊天消息
response = client.chat.send_message(
    workspace_id=new_workspace["id"],
    message="你好，请总结一下我上传的文档"
)
print(f"AI 回复: {response['message']}")
```

## 功能

- 完整的 AnythingLLM API 支持
  - 认证模块（auth）
  - 工作区模块（workspaces）
  - 文档模块（documents）
  - 聊天模块（chat）
  - 系统模块（system）
  - 用户模块（users）
  - 嵌入模块（embed）
  - 管理员模块（admin）
  - OpenAI 兼容模块（openai）
  - 工作区线程模块（workspace_thread）
- 简单易用的接口
- 类型提示支持
- 详细的文档和示例

## 许可证

MIT
