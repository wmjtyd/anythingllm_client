"""
嵌入模块
"""

from typing import Dict, Any, List, Optional, cast
from .base import BaseModule


class EmbedModule(BaseModule):
    """
    处理 AnythingLLM 嵌入相关的 API
    """

    def get_text_embedding(self, text: str) -> Dict[str, Any]:
        """
        获取文本嵌入向量

        Args:
            text: 要嵌入的文本

        Returns:
            嵌入向量结果
        """
        return self.http_client.post("/v1/embed", json_data={"text": text})

    def get_batch_embeddings(self, texts: List[str]) -> Dict[str, Any]:
        """
        批量获取文本嵌入向量

        Args:
            texts: 要嵌入的文本列表

        Returns:
            嵌入向量结果
        """
        return self.http_client.post("/v1/embed/batch", json_data={"texts": texts})
