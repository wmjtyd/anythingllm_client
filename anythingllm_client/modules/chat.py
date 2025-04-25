"""
聊天模块
"""

from typing import Dict, Any, List, Optional, cast
from .base import BaseModule
from ..types import ChatMessage, ChatThread


class ChatModule(BaseModule):
    """
    处理 AnythingLLM 聊天相关的 API
    """

    def send_message(
        self,
        workspace_id: str,
        message: str,
        thread_id: Optional[str] = None,
        system_prompt: Optional[str] = None,
        temperature: Optional[float] = None,
        include_sources: Optional[bool] = None,
    ) -> ChatMessage:
        """
        发送聊天消息

        Args:
            workspace_id: 工作区 ID 或 slug
            message: 消息内容
            thread_id: 对话线程 ID
            system_prompt: 系统提示
            temperature: 温度值
            include_sources: 是否包含源文档

        Returns:
            聊天响应
        """
        data = {
            "message": message,
        }

        if thread_id:
            data["threadId"] = thread_id

        if system_prompt:
            data["systemPrompt"] = system_prompt

        if temperature is not None:
            data["temperature"] = temperature

        if include_sources is not None:
            data["includeSources"] = include_sources

        return self.http_client.post(f"/v1/workspaces/{workspace_id}/chat", json_data=data)

    def get_history(
        self,
        workspace_id: str,
        thread_id: Optional[str] = None
    ) -> List[ChatMessage]:
        """
        获取聊天历史

        Args:
            workspace_id: 工作区 ID 或 slug
            thread_id: 对话线程 ID

        Returns:
            聊天历史记录
        """
        endpoint = f"/v1/workspaces/{workspace_id}/chat-history"

        if thread_id:
            endpoint = f"{endpoint}/{thread_id}"

        return self.http_client.get(endpoint)

    def clear_history(
        self,
        workspace_id: str,
        thread_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        清除聊天历史

        Args:
            workspace_id: 工作区 ID 或 slug
            thread_id: 对话线程 ID

        Returns:
            操作结果
        """
        endpoint = f"/v1/workspaces/{workspace_id}/chat-history"

        if thread_id:
            endpoint = f"{endpoint}/{thread_id}"

        return self.http_client.delete(endpoint)

    def list_threads(self, workspace_id: str) -> List[ChatThread]:
        """
        获取工作区的所有对话线程

        Args:
            workspace_id: 工作区 ID 或 slug

        Returns:
            对话线程列表
        """
        return self.http_client.get(f"/v1/workspaces/{workspace_id}/threads")

    def create_thread(
        self,
        workspace_id: str,
        name: str,
        description: Optional[str] = None
    ) -> ChatThread:
        """
        创建新的对话线程

        Args:
            workspace_id: 工作区 ID 或 slug
            name: 线程名称
            description: 线程描述

        Returns:
            创建的线程信息
        """
        data = {
            "name": name,
        }

        if description:
            data["description"] = description

        return self.http_client.post(f"/v1/workspaces/{workspace_id}/threads", json_data=data)

    def update_thread(
        self,
        workspace_id: str,
        thread_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None
    ) -> ChatThread:
        """
        更新对话线程

        Args:
            workspace_id: 工作区 ID 或 slug
            thread_id: 线程 ID
            name: 新线程名称
            description: 新线程描述

        Returns:
            更新后的线程信息
        """
        data = {}

        if name:
            data["name"] = name

        if description:
            data["description"] = description

        return self.http_client.put(
            f"/v1/workspaces/{workspace_id}/threads/{thread_id}",
            json_data=data
        )

    def delete_thread(self, workspace_id: str, thread_id: str) -> Dict[str, Any]:
        """
        删除对话线程

        Args:
            workspace_id: 工作区 ID 或 slug
            thread_id: 线程 ID

        Returns:
            删除操作结果
        """
        return self.http_client.delete(f"/v1/workspaces/{workspace_id}/threads/{thread_id}")
