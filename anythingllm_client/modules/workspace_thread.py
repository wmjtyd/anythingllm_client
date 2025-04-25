"""
工作区线程模块
"""

from typing import Dict, Any, List, Optional, Union, cast
from .base import BaseModule
from ..types import ChatThread, ChatMessage


class WorkspaceThreadModule(BaseModule):
    """
    处理 AnythingLLM 工作区线程相关的 API
    """

    def list_threads(self, workspace_id: str) -> List[ChatThread]:
        """
        获取工作区的所有线程

        Args:
            workspace_id: 工作区 ID 或 slug

        Returns:
            线程列表
        """
        return self.http_client.get(f"/v1/workspace/{workspace_id}/threads")

    def get_thread(self, workspace_id: str, thread_id: str) -> ChatThread:
        """
        获取特定线程的详细信息

        Args:
            workspace_id: 工作区 ID 或 slug
            thread_id: 线程 ID

        Returns:
            线程详细信息
        """
        return self.http_client.get(f"/v1/workspace/{workspace_id}/thread/{thread_id}")

    def create_thread(
        self,
        workspace_id: str,
        name: str,
        description: Optional[str] = None
    ) -> ChatThread:
        """
        创建新线程

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

        return self.http_client.post(f"/v1/workspace/{workspace_id}/thread/new", json_data=data)

    def update_thread(
        self,
        workspace_id: str,
        thread_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None
    ) -> ChatThread:
        """
        更新线程

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

        return self.http_client.post(f"/v1/workspace/{workspace_id}/thread/{thread_id}", json_data=data)

    def delete_thread(self, workspace_id: str, thread_id: str) -> Dict[str, Any]:
        """
        删除线程

        Args:
            workspace_id: 工作区 ID 或 slug
            thread_id: 线程 ID

        Returns:
            删除操作结果
        """
        return self.http_client.delete(f"/v1/workspace/{workspace_id}/thread/{thread_id}")

    def get_thread_messages(self, workspace_id: str, thread_id: str) -> List[ChatMessage]:
        """
        获取线程的所有消息

        Args:
            workspace_id: 工作区 ID 或 slug
            thread_id: 线程 ID

        Returns:
            消息列表
        """
        return self.http_client.get(f"/v1/workspace/{workspace_id}/thread/{thread_id}/messages")

    def send_message(
        self,
        workspace_id: str,
        thread_id: str,
        message: str,
        system_prompt: Optional[str] = None,
        temperature: Optional[float] = None,
        include_sources: Optional[bool] = None,
    ) -> ChatMessage:
        """
        发送消息到线程

        Args:
            workspace_id: 工作区 ID 或 slug
            thread_id: 线程 ID
            message: 消息内容
            system_prompt: 系统提示
            temperature: 温度值
            include_sources: 是否包含源文档

        Returns:
            消息响应
        """
        data = {
            "message": message,
        }

        if system_prompt:
            data["systemPrompt"] = system_prompt

        if temperature is not None:
            data["temperature"] = temperature

        if include_sources is not None:
            data["includeSources"] = include_sources

        return self.http_client.post(f"/v1/workspace/{workspace_id}/thread/{thread_id}/message", json_data=data)

    def clear_thread_messages(self, workspace_id: str, thread_id: str) -> Dict[str, Any]:
        """
        清除线程的所有消息

        Args:
            workspace_id: 工作区 ID 或 slug
            thread_id: 线程 ID

        Returns:
            清除操作结果
        """
        return self.http_client.delete(f"/v1/workspace/{workspace_id}/thread/{thread_id}/messages")
