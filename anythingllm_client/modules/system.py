"""
系统设置模块
"""

from typing import Dict, Any, List, Optional, cast
from .base import BaseModule
from ..types import SystemSettings, LLMModel, EmbeddingModel, VectorDatabase, Prompt


class SystemModule(BaseModule):
    """
    处理 AnythingLLM 系统相关的 API
    """

    def get_health(self) -> Dict[str, Any]:
        """
        获取系统健康状态

        Returns:
            系统健康状态信息
        """
        return self.http_client.get("/v1/system/health")

    def get_settings(self) -> SystemSettings:
        """
        获取系统设置

        Returns:
            系统设置信息
        """
        return self.http_client.get("/v1/system/settings")

    def update_settings(self, settings: Dict[str, Any]) -> SystemSettings:
        """
        更新系统设置

        Args:
            settings: 要更新的设置

        Returns:
            更新后的系统设置
        """
        return self.http_client.post("/v1/system/settings", json_data=settings)

    def get_llm_models(self) -> List[LLMModel]:
        """
        获取可用的 LLM 模型

        Returns:
            LLM 模型列表
        """
        return self.http_client.get("/v1/system/llm-models")

    def get_embedding_models(self) -> List[EmbeddingModel]:
        """
        获取可用的嵌入模型

        Returns:
            嵌入模型列表
        """
        return self.http_client.get("/v1/system/embedding-models")

    def get_vector_dbs(self) -> List[VectorDatabase]:
        """
        获取可用的向量数据库

        Returns:
            向量数据库列表
        """
        return self.http_client.get("/v1/system/vector-databases")

    def get_accepted_document_types(self) -> List[str]:
        """
        获取系统接受的文档类型

        Returns:
            接受的文档类型列表
        """
        return self.http_client.get("/v1/system/accepted-document-types")

    def get_prompts(self) -> List[Prompt]:
        """
        获取系统提示模板

        Returns:
            提示模板列表
        """
        return self.http_client.get("/v1/system/prompts")

    def create_prompt(
        self,
        title: str,
        content: str,
        description: Optional[str] = None
    ) -> Prompt:
        """
        创建系统提示模板

        Args:
            title: 提示标题
            content: 提示内容
            description: 提示描述

        Returns:
            创建的提示模板
        """
        data = {
            "title": title,
            "content": content,
        }

        if description:
            data["description"] = description

        return self.http_client.post("/v1/system/prompts", json_data=data)

    def update_prompt(
        self,
        prompt_id: str,
        title: Optional[str] = None,
        content: Optional[str] = None,
        description: Optional[str] = None
    ) -> Prompt:
        """
        更新系统提示模板

        Args:
            prompt_id: 提示模板 ID
            title: 新提示标题
            content: 新提示内容
            description: 新提示描述

        Returns:
            更新后的提示模板
        """
        data = {}

        if title:
            data["title"] = title

        if content:
            data["content"] = content

        if description:
            data["description"] = description

        return self.http_client.put(f"/v1/system/prompts/{prompt_id}", json_data=data)

    def delete_prompt(self, prompt_id: str) -> Dict[str, Any]:
        """
        删除系统提示模板

        Args:
            prompt_id: 提示模板 ID

        Returns:
            删除操作结果
        """
        return self.http_client.delete(f"/v1/system/prompts/{prompt_id}")
