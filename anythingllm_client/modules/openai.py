"""
OpenAI 兼容模块
"""

from typing import Dict, Any, List, Optional, Union, cast
from .base import BaseModule
from ..types import OpenAIModel, VectorStore


class OpenAIModule(BaseModule):
    """
    处理 AnythingLLM OpenAI 兼容 API
    """

    def list_models(self) -> List[OpenAIModel]:
        """
        获取所有可用的"模型"，实际上是可用于聊天的工作区

        Returns:
            模型列表
        """
        response = self.http_client.get("/v1/openai/models")
        return response.get("data", [])

    def create_chat_completion(
        self,
        model: str,
        messages: List[Dict[str, str]],
        temperature: Optional[float] = None,
        stream: bool = False,
        max_tokens: Optional[int] = None,
        top_p: Optional[float] = None,
        frequency_penalty: Optional[float] = None,
        presence_penalty: Optional[float] = None,
    ) -> Dict[str, Any]:
        """
        创建聊天完成

        Args:
            model: 模型名称（工作区 slug）
            messages: 消息列表，每个消息包含 role 和 content
            temperature: 温度值
            stream: 是否流式输出
            max_tokens: 最大令牌数
            top_p: top_p 值
            frequency_penalty: 频率惩罚
            presence_penalty: 存在惩罚

        Returns:
            聊天完成结果
        """
        data = {
            "model": model,
            "messages": messages,
            "stream": stream,
        }

        if temperature is not None:
            data["temperature"] = temperature

        if max_tokens is not None:
            data["max_tokens"] = max_tokens

        if top_p is not None:
            data["top_p"] = top_p

        if frequency_penalty is not None:
            data["frequency_penalty"] = frequency_penalty

        if presence_penalty is not None:
            data["presence_penalty"] = presence_penalty

        return self.http_client.post("/v1/openai/chat/completions", json_data=data)

    def list_vector_stores(self) -> List[VectorStore]:
        """
        获取所有向量数据库集合

        Returns:
            向量数据库集合列表
        """
        response = self.http_client.get("/v1/openai/vector_stores")
        return response.get("data", [])

    def create_embedding(self, input_text: Union[str, List[str]], model: Optional[str] = None) -> Dict[str, Any]:
        """
        创建嵌入向量

        Args:
            input_text: 输入文本或文本列表
            model: 模型名称

        Returns:
            嵌入向量结果
        """
        data = {
            "input": input_text,
        }

        if model:
            data["model"] = model

        return self.http_client.post("/v1/openai/embeddings", json_data=data)
