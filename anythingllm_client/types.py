"""
类型定义模块

定义 AnythingLLM API 的各种数据类型
"""

from typing import Dict, List, Any, Optional, Union, TypedDict
from datetime import datetime


class Workspace(TypedDict, total=False):
    """工作区类型"""
    id: str
    slug: str
    name: str
    description: str
    createdAt: str
    updatedAt: str
    vectorDb: str
    embeddingModel: str
    chatModel: str
    temperature: float
    includeSources: bool
    promptId: Optional[str]


class Document(TypedDict, total=False):
    """文档类型"""
    id: str
    name: str
    path: str
    url: Optional[str]
    type: str
    size: int
    tokens: int
    chunks: int
    createdAt: str
    updatedAt: str
    metadata: Dict[str, Any]
    folderId: Optional[str]
    workspaceIds: List[str]


class DocumentFolder(TypedDict, total=False):
    """文档文件夹类型"""
    id: str
    name: str
    path: str
    createdAt: str
    updatedAt: str
    documentCount: int


class ChatMessage(TypedDict, total=False):
    """聊天消息类型"""
    id: str
    role: str
    content: str
    createdAt: str
    sources: List[Dict[str, Any]]
    threadId: Optional[str]
    workspaceId: str


class ChatThread(TypedDict, total=False):
    """聊天线程类型"""
    id: str
    name: str
    description: Optional[str]
    createdAt: str
    updatedAt: str
    workspaceId: str
    messageCount: int


class User(TypedDict, total=False):
    """用户类型"""
    id: str
    username: str
    role: str
    createdAt: str
    updatedAt: str
    customization: Dict[str, Any]


class ApiKey(TypedDict, total=False):
    """API 密钥类型"""
    id: str
    name: str
    key: str
    createdAt: str
    expiresAt: Optional[str]
    lastUsed: Optional[str]


class Prompt(TypedDict, total=False):
    """提示模板类型"""
    id: str
    title: str
    content: str
    description: Optional[str]
    createdAt: str
    updatedAt: str


class LLMModel(TypedDict, total=False):
    """LLM 模型类型"""
    id: str
    name: str
    provider: str
    tokenLimit: int
    available: bool


class EmbeddingModel(TypedDict, total=False):
    """嵌入模型类型"""
    id: str
    name: str
    provider: str
    dimensions: int
    available: bool


class VectorDatabase(TypedDict, total=False):
    """向量数据库类型"""
    id: str
    name: str
    provider: str
    available: bool


class SystemSettings(TypedDict, total=False):
    """系统设置类型"""
    serverName: str
    serverDescription: str
    allowUserSignup: bool
    allowAnonymousUsers: bool
    defaultLLMProvider: str
    defaultEmbeddingProvider: str
    defaultVectorDB: str
    customSettings: Dict[str, Any]


class Invite(TypedDict, total=False):
    """邀请码类型"""
    id: str
    code: str
    status: str
    createdAt: str
    updatedAt: str
    workspaceIds: List[int]


class OpenAIModel(TypedDict, total=False):
    """OpenAI 模型类型"""
    name: str
    model: str
    llm: Dict[str, str]


class VectorStore(TypedDict, total=False):
    """向量存储类型"""
    id: str
    object: str
    name: str
    file_counts: Dict[str, int]
    provider: str
