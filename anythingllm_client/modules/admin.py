"""
管理员模块
"""

from typing import Dict, Any, List, Optional, Union, cast
from .base import BaseModule
from ..types import User, Invite, SystemSettings


class AdminModule(BaseModule):
    """
    处理 AnythingLLM 管理员相关的 API
    """

    def is_multi_user_mode(self) -> Dict[str, bool]:
        """
        检查实例是否处于多用户模式

        Returns:
            包含多用户模式状态的字典
        """
        return self.http_client.get("/v1/admin/is-multi-user-mode")

    def create_user(
        self,
        username: str,
        password: str,
        role: str = "default"
    ) -> Dict[str, User]:
        """
        创建新用户

        Args:
            username: 用户名
            password: 密码
            role: 用户角色，默认为 "default"

        Returns:
            创建的用户信息
        """
        data = {
            "username": username,
            "password": password,
            "role": role
        }

        return self.http_client.post("/v1/admin/users/new", json_data=data)

    def update_user(
        self,
        user_id: str,
        username: Optional[str] = None,
        password: Optional[str] = None,
        role: Optional[str] = None
    ) -> Dict[str, User]:
        """
        更新用户

        Args:
            user_id: 用户 ID
            username: 新用户名
            password: 新密码
            role: 新用户角色

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

        return self.http_client.post(f"/v1/admin/users/{user_id}", json_data=data)

    def delete_user(self, user_id: str) -> Dict[str, Any]:
        """
        删除用户

        Args:
            user_id: 用户 ID

        Returns:
            删除操作结果
        """
        return self.http_client.delete(f"/v1/admin/users/{user_id}")

    def create_invite(self, workspace_ids: Optional[List[int]] = None) -> Dict[str, Invite]:
        """
        创建新的邀请码

        Args:
            workspace_ids: 工作区 ID 列表

        Returns:
            创建的邀请码信息
        """
        data = {}

        if workspace_ids:
            data["workspaceIds"] = workspace_ids

        return self.http_client.post("/v1/admin/invite/new", json_data=data)

    def get_invites(self) -> List[Invite]:
        """
        获取所有邀请码

        Returns:
            邀请码列表
        """
        return self.http_client.get("/v1/admin/invites")

    def delete_invite(self, invite_id: str) -> Dict[str, Any]:
        """
        删除邀请码

        Args:
            invite_id: 邀请码 ID

        Returns:
            删除操作结果
        """
        return self.http_client.delete(f"/v1/admin/invite/{invite_id}")

    def get_system_preferences(self) -> SystemSettings:
        """
        获取系统偏好设置

        Returns:
            系统偏好设置
        """
        return self.http_client.get("/v1/admin/system-preferences")

    def update_system_preferences(self, preferences: Dict[str, Any]) -> SystemSettings:
        """
        更新系统偏好设置

        Args:
            preferences: 新的系统偏好设置

        Returns:
            更新后的系统偏好设置
        """
        return self.http_client.post("/v1/admin/system-preferences", json_data=preferences)
