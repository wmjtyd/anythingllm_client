"""
文档管理模块
"""

import os
from typing import Dict, Any, List, Optional, Union, BinaryIO, cast
from .base import BaseModule
from ..types import Document, DocumentFolder


class DocumentsModule(BaseModule):
    """
    处理 AnythingLLM 文档相关的 API
    """

    def list(self) -> List[Document]:
        """
        获取所有文档列表

        Returns:
            文档列表
        """
        return self.http_client.get("/v1/documents")

    def get(self, document_id: str) -> Document:
        """
        获取特定文档的详细信息

        Args:
            document_id: 文档 ID

        Returns:
            文档详细信息
        """
        return self.http_client.get(f"/v1/documents/{document_id}")

    def upload(
        self,
        file_path: str = None,
        file_obj: BinaryIO = None,
        add_to_workspaces: Optional[List[str]] = None,
        folder_name: Optional[str] = None
    ) -> Document:
        """
        上传文档

        Args:
            file_path: 文件路径
            file_obj: 文件对象
            add_to_workspaces: 要添加文档的工作区 slug 列表
            folder_name: 目标文件夹名称

        Returns:
            上传的文档信息
        """
        if not file_path and not file_obj:
            raise ValueError("必须提供 file_path 或 file_obj")

        if file_path and not os.path.exists(file_path):
            raise FileNotFoundError(f"文件不存在: {file_path}")

        files = {}
        data = {}

        if file_path:
            files["file"] = open(file_path, "rb")
        elif file_obj:
            files["file"] = file_obj

        if add_to_workspaces:
            data["addToWorkspaces"] = ",".join(add_to_workspaces)

        endpoint = "/v1/document/upload"
        if folder_name:
            endpoint = f"/v1/document/upload/{folder_name}"

        try:
            return self.http_client.post(endpoint, data=data, files=files)
        finally:
            # 如果我们打开了文件，确保关闭它
            if file_path and "file" in files:
                files["file"].close()

    def delete(self, document_id: str) -> Dict[str, Any]:
        """
        删除文档

        Args:
            document_id: 文档 ID

        Returns:
            删除操作结果
        """
        return self.http_client.delete(f"/v1/documents/{document_id}")

    def sync(self) -> Dict[str, Any]:
        """
        同步所有文档

        Returns:
            同步操作结果
        """
        return self.http_client.post("/v1/documents/sync")

    def get_folders(self) -> List[DocumentFolder]:
        """
        获取所有文档文件夹

        Returns:
            文件夹列表
        """
        return self.http_client.get("/v1/document-folders")

    def create_folder(self, name: str) -> DocumentFolder:
        """
        创建文档文件夹

        Args:
            name: 文件夹名称

        Returns:
            创建的文件夹信息
        """
        return self.http_client.post("/v1/document-folders", json_data={"name": name})

    def delete_folder(self, folder_id: str) -> Dict[str, Any]:
        """
        删除文档文件夹

        Args:
            folder_id: 文件夹 ID

        Returns:
            删除操作结果
        """
        return self.http_client.delete(f"/v1/document-folders/{folder_id}")
