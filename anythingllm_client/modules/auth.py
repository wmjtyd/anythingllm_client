"""
认证模块
"""

from typing import Dict, Any, Optional
from .base import BaseModule


class AuthModule(BaseModule):
    """
    处理 AnythingLLM 认证相关的 API
    """
    
    def login(self, username: str, password: str) -> Dict[str, Any]:
        """
        用户登录
        
        Args:
            username: 用户名
            password: 密码
            
        Returns:
            包含认证信息的字典，通常包含 token
        """
        return self.http_client.post(
            "/v1/auth/login",
            json_data={"username": username, "password": password}
        )
    
    def validate_token(self, token: Optional[str] = None) -> Dict[str, Any]:
        """
        验证认证令牌
        
        Args:
            token: 要验证的令牌，如果未提供则使用当前客户端的令牌
            
        Returns:
            包含验证结果的字典
        """
        return self.http_client.post("/v1/auth/validate")
    
    def check_setup(self) -> Dict[str, Any]:
        """
        检查系统设置状态
        
        Returns:
            包含系统设置状态的字典
        """
        return self.http_client.get("/v1/auth/setup-complete")
