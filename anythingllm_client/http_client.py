"""
HTTP 客户端模块，处理与 AnythingLLM API 的所有 HTTP 通信
"""

import json
import requests
from typing import Dict, Any, Optional, Union, List, BinaryIO
from urllib.parse import urljoin


class ApiError(Exception):
    """API 错误异常类"""
    
    def __init__(self, status_code: int, message: str, details: Optional[Dict[str, Any]] = None):
        self.status_code = status_code
        self.message = message
        self.details = details
        super().__init__(f"API 错误 {status_code}: {message}")


class HttpClient:
    """
    HTTP 客户端类，处理与 AnythingLLM API 的所有 HTTP 通信
    """
    
    def __init__(self, base_url: str, api_key: str, timeout: int = 60):
        """
        初始化 HTTP 客户端
        
        Args:
            base_url: API 的基础 URL
            api_key: API 密钥
            timeout: 请求超时时间（秒）
        """
        self.base_url = base_url
        self.api_key = api_key
        self.timeout = timeout
    
    def _get_headers(self, with_content_type: bool = True) -> Dict[str, str]:
        """
        获取请求头
        
        Args:
            with_content_type: 是否包含 Content-Type 头
            
        Returns:
            请求头字典
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "X-API-Key": self.api_key,
        }
        
        if with_content_type:
            headers["Content-Type"] = "application/json"
        
        return headers
    
    def _handle_response(self, response: requests.Response) -> Any:
        """
        处理 API 响应
        
        Args:
            response: 请求响应对象
            
        Returns:
            解析后的响应数据
            
        Raises:
            ApiError: 当 API 返回错误时
        """
        if not response.ok:
            try:
                error_data = response.json()
                message = error_data.get("message", response.reason)
                details = error_data
            except (ValueError, json.JSONDecodeError):
                message = response.reason
                details = {"raw_response": response.text}
            
            raise ApiError(response.status_code, message, details)
        
        # 处理空响应
        if not response.text:
            return {}
        
        try:
            return response.json()
        except (ValueError, json.JSONDecodeError):
            return {"raw_response": response.text}
    
    def get(self, path: str, params: Optional[Dict[str, Any]] = None) -> Any:
        """
        发送 GET 请求
        
        Args:
            path: API 路径
            params: 查询参数
            
        Returns:
            解析后的响应数据
        """
        url = urljoin(self.base_url, path)
        response = requests.get(
            url,
            params=params,
            headers=self._get_headers(),
            timeout=self.timeout
        )
        return self._handle_response(response)
    
    def post(
        self,
        path: str,
        data: Optional[Dict[str, Any]] = None,
        json_data: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, BinaryIO]] = None
    ) -> Any:
        """
        发送 POST 请求
        
        Args:
            path: API 路径
            data: 表单数据
            json_data: JSON 数据
            files: 文件数据
            
        Returns:
            解析后的响应数据
        """
        url = urljoin(self.base_url, path)
        headers = self._get_headers(with_content_type=files is None)
        
        response = requests.post(
            url,
            data=data,
            json=json_data,
            files=files,
            headers=headers,
            timeout=self.timeout
        )
        return self._handle_response(response)
    
    def put(self, path: str, json_data: Dict[str, Any]) -> Any:
        """
        发送 PUT 请求
        
        Args:
            path: API 路径
            json_data: JSON 数据
            
        Returns:
            解析后的响应数据
        """
        url = urljoin(self.base_url, path)
        response = requests.put(
            url,
            json=json_data,
            headers=self._get_headers(),
            timeout=self.timeout
        )
        return self._handle_response(response)
    
    def delete(self, path: str, params: Optional[Dict[str, Any]] = None) -> Any:
        """
        发送 DELETE 请求
        
        Args:
            path: API 路径
            params: 查询参数
            
        Returns:
            解析后的响应数据
        """
        url = urljoin(self.base_url, path)
        response = requests.delete(
            url,
            params=params,
            headers=self._get_headers(),
            timeout=self.timeout
        )
        return self._handle_response(response)
