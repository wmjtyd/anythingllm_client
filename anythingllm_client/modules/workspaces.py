"""
工作区管理模块
"""

from typing import Dict, Any, List, Optional, Union, cast
from .base import BaseModule
from ..types import Workspace, Document


class WorkspacesModule(BaseModule):
    """
    处理 AnythingLLM 工作区相关的 API
    """

    def list(self) -> List[Workspace]:
        """
        获取所有工作区列表

        Returns:
            工作区列表
        """
        return self.http_client.get("/v1/workspaces")

    def get(self, workspace_id: str) -> Workspace:
        """
        获取特定工作区的详细信息

        Args:
            workspace_id: 工作区 ID 或 slug

        Returns:
            工作区详细信息
        """
        return self.http_client.get(f"/v1/workspaces/{workspace_id}")

    def create(
        self,
        name: str,
        description: Optional[str] = None,
        vector_db: Optional[str] = None
    ) -> Workspace:
        """
        创建新工作区

        Args:
            name: 工作区名称
            description: 工作区描述
            vector_db: 向量数据库类型

        Returns:
            创建的工作区信息
        """
        data = {
            "name": name,
            "description": description or "",
        }

        if vector_db:
            data["vectorDb"] = vector_db

        return self.http_client.post("/v1/workspaces", json_data=data)

    def update(
        self,
        workspace_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        vector_db: Optional[str] = None,
        embedding_model: Optional[str] = None,
        chat_model: Optional[str] = None,
        temperature: Optional[float] = None,
        include_sources: Optional[bool] = None,
        prompt_id: Optional[str] = None,
    ) -> Workspace:
        """
        更新工作区

        Args:
            workspace_id: 工作区 ID 或 slug
            name: 新工作区名称
            description: 新工作区描述
            vector_db: 新向量数据库类型
            embedding_model: 新嵌入模型
            chat_model: 新聊天模型
            temperature: 新温度值
            include_sources: 是否包含源文档
            prompt_id: 提示模板 ID

        Returns:
            更新后的工作区信息
        """
        data = {}

        if name is not None:
            data["name"] = name

        if description is not None:
            data["description"] = description

        if vector_db is not None:
            data["vectorDb"] = vector_db

        if embedding_model is not None:
            data["embeddingModel"] = embedding_model

        if chat_model is not None:
            data["chatModel"] = chat_model

        if temperature is not None:
            data["temperature"] = temperature

        if include_sources is not None:
            data["includeSources"] = include_sources

        if prompt_id is not None:
            data["promptId"] = prompt_id

        return self.http_client.put(f"/v1/workspaces/{workspace_id}", json_data=data)

    def delete(self, workspace_id: str) -> Dict[str, Any]:
        """
        删除工作区

        Args:
            workspace_id: 工作区 ID 或 slug

        Returns:
            删除操作结果
        """
        return self.http_client.delete(f"/v1/workspaces/{workspace_id}")

    def get_documents(self, workspace_id: str) -> List[Document]:
        """
        获取工作区中的文档

        Args:
            workspace_id: 工作区 ID 或 slug

        Returns:
            文档列表
        """
        return self.http_client.get(f"/v1/workspaces/{workspace_id}/documents")

    def add_documents(self, workspace_id: str, document_ids: List[str]) -> Dict[str, Any]:
        """
        向工作区添加文档

        Args:
            workspace_id: 工作区 ID 或 slug
            document_ids: 要添加的文档 ID 列表

        Returns:
            操作结果
        """
        return self.http_client.post(
            f"/v1/workspaces/{workspace_id}/documents",
            json_data={"documents": document_ids}
        )

    def remove_document(self, workspace_id: str, document_id: str) -> Dict[str, Any]:
        """
        从工作区移除文档

        Args:
            workspace_id: 工作区 ID 或 slug
            document_id: 要移除的文档 ID

        Returns:
            操作结果
        """
        return self.http_client.delete(
            f"/v1/workspaces/{workspace_id}/documents/{document_id}"
        )
