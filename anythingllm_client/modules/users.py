"""
用户管理模块
"""

from typing import Dict, Any, List, Optional, cast
from .base import BaseModule
from ..types import User, ApiKey


class UsersModule(BaseModule):
    """
    处理 AnythingLLM 用户相关的 API
    """

    def list(self) -> List[User]:
        """
        获取所有用户列表

        Returns:
            用户列表
        """
        return self.http_client.get("/v1/users")

    def get(self, user_id: str) -> User:
        """
        获取特定用户的详细信息

        Args:
            user_id: 用户 ID

        Returns:
            用户详细信息
        """
        return self.http_client.get(f"/v1/users/{user_id}")

    def create(
        self,
        username: str,
        password: str,
        role: str = "user",
        customization: Optional[Dict[str, Any]] = None
    ) -> User:
        """
        创建新用户

        Args:
            username: 用户名
            password: 密码
            role: 用户角色，默认为 "user"
            customization: 用户自定义设置

        Returns:
            创建的用户信息
        """
        data = {
            "username": username,
            "password": password,
            "role": role,
        }

        if customization:
            data["customization"] = customization

        return self.http_client.post("/v1/users", json_data=data)

    def update(
        self,
        user_id: str,
        username: Optional[str] = None,
        password: Optional[str] = None,
        role: Optional[str] = None,
        customization: Optional[Dict[str, Any]] = None
    ) -> User:
        """
        更新用户

        Args:
            user_id: 用户 ID
            username: 新用户名
            password: 新密码
            role: 新用户角色
            customization: 新用户自定义设置

        Returns:
            更新后的用户信息
        """
        data = {}

        if username:
            data["username"] = username

        if password:
            data["password"] = password

        if role:
            data["role"] = role

        if customization:
            data["customization"] = customization

        return self.http_client.put(f"/v1/users/{user_id}", json_data=data)

    def delete(self, user_id: str) -> Dict[str, Any]:
        """
        删除用户

        Args:
            user_id: 用户 ID

        Returns:
            删除操作结果
        """
        return self.http_client.delete(f"/v1/users/{user_id}")

    def get_api_keys(self) -> List[ApiKey]:
        """
        获取所有 API 密钥

        Returns:
            API 密钥列表
        """
        return self.http_client.get("/v1/api-keys")

    def create_api_key(
        self,
        name: str,
        expires_at: Optional[str] = None
    ) -> ApiKey:
        """
        创建新 API 密钥

        Args:
            name: API 密钥名称
            expires_at: 过期时间，ISO 格式

        Returns:
            创建的 API 密钥信息
        """
        data = {
            "name": name,
        }

        if expires_at:
            data["expiresAt"] = expires_at

        return self.http_client.post("/v1/api-keys", json_data=data)

    def delete_api_key(self, key_id: str) -> Dict[str, Any]:
        """
        删除 API 密钥

        Args:
            key_id: API 密钥 ID

        Returns:
            删除操作结果
        """
        return self.http_client.delete(f"/v1/api-keys/{key_id}")
