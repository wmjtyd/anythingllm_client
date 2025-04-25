"""
模块基类
"""

from typing import Any
from ..http_client import HttpClient


class BaseModule:
    """
    所有 API 模块的基类
    """
    
    def __init__(self, http_client: HttpClient):
        """
        初始化模块
        
        Args:
            http_client: HTTP 客户端实例
        """
        self.http_client = http_client
