"""
AnythingLLM 客户端主类
"""

import os
from typing import Optional, Dict, Any

from .modules.auth import AuthModule
from .modules.workspaces import WorkspacesModule
from .modules.documents import DocumentsModule
from .modules.chat import ChatModule
from .modules.system import SystemModule
from .modules.users import UsersModule
from .modules.embed import EmbedModule
from .modules.admin import AdminModule
from .modules.openai import OpenAIModule
from .modules.workspace_thread import WorkspaceThreadModule
from .http_client import HttpClient


class AnythingLLMClient:
    """
    AnythingLLM API 客户端主类

    提供对 AnythingLLM API 的所有功能的访问。
    """

    def __init__(
        self,
        base_url: str = "http://localhost:3001",
        api_key: Optional[str] = None,
        timeout: int = 60,
    ):
        """
        初始化 AnythingLLM 客户端

        Args:
            base_url: AnythingLLM API 的基础 URL
            api_key: API 密钥，如果未提供，将尝试从环境变量 ANYTHINGLLM_API_KEY 获取
            timeout: 请求超时时间（秒）
        """
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key or os.environ.get("ANYTHINGLLM_API_KEY")

        if not self.api_key:
            raise ValueError(
                "API 密钥必须提供，可以通过参数传递或设置环境变量 ANYTHINGLLM_API_KEY"
            )

        self.http_client = HttpClient(
            base_url=self.base_url,
            api_key=self.api_key,
            timeout=timeout
        )

        # 初始化各个模块
        self.auth = AuthModule(self.http_client)
        self.workspaces = WorkspacesModule(self.http_client)
        self.documents = DocumentsModule(self.http_client)
        self.chat = ChatModule(self.http_client)
        self.system = SystemModule(self.http_client)
        self.users = UsersModule(self.http_client)
        self.embed = EmbedModule(self.http_client)
        self.admin = AdminModule(self.http_client)
        self.openai = OpenAIModule(self.http_client)
        self.workspace_thread = WorkspaceThreadModule(self.http_client)

    def get_api_status(self) -> Dict[str, Any]:
        """
        获取 API 服务器状态

        Returns:
            包含 API 服务器状态信息的字典
        """
        return self.http_client.get("/v1/system/health")
