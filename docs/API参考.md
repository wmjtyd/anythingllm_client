# AnythingLLM Python 客户端 API 参考

这个文档提供了 AnythingLLM Python 客户端库的详细 API 参考。

## 目录

- [主客户端](#主客户端)
- [HTTP 客户端](#http-客户端)
- [认证模块](#认证模块)
- [工作区模块](#工作区模块)
- [文档模块](#文档模块)
- [聊天模块](#聊天模块)
- [系统模块](#系统模块)
- [用户模块](#用户模块)
- [嵌入模块](#嵌入模块)
- [管理员模块](#管理员模块)
- [OpenAI 兼容模块](#openai-兼容模块)
- [工作区线程模块](#工作区线程模块)
- [类型定义](#类型定义)

## 主客户端

### `AnythingLLMClient`

主客户端类，提供对所有 API 功能的访问。

#### 初始化

```python
def __init__(
    self,
    base_url: str = "http://localhost:3001",
    api_key: Optional[str] = None,
    timeout: int = 60,
)
```

**参数**:
- `base_url`: AnythingLLM API 的基础 URL
- `api_key`: API 密钥，如果未提供，将尝试从环境变量 `ANYTHINGLLM_API_KEY` 获取
- `timeout`: 请求超时时间（秒）

#### 方法

```python
def get_api_status(self) -> Dict[str, Any]
```

获取 API 服务器状态。

**返回值**:
- 包含 API 服务器状态信息的字典

#### 属性

- `auth`: 认证模块实例
- `workspaces`: 工作区模块实例
- `documents`: 文档模块实例
- `chat`: 聊天模块实例
- `system`: 系统模块实例
- `users`: 用户模块实例
- `embed`: 嵌入模块实例
- `http_client`: HTTP 客户端实例
- `admin`: 管理员模块实例
- `openai`: OpenAI 兼容模块实例
- `workspace_thread`: 工作区线程模块实例

## HTTP 客户端

### `HttpClient`

处理与 AnythingLLM API 的所有 HTTP 通信。

#### 初始化

```python
def __init__(self, base_url: str, api_key: str, timeout: int = 60)
```

**参数**:
- `base_url`: API 的基础 URL
- `api_key`: API 密钥
- `timeout`: 请求超时时间（秒）

#### 方法

```python
def get(self, path: str, params: Optional[Dict[str, Any]] = None) -> Any
```

发送 GET 请求。

**参数**:
- `path`: API 路径
- `params`: 查询参数

**返回值**:
- 解析后的响应数据

```python
def post(
    self,
    path: str,
    data: Optional[Dict[str, Any]] = None,
    json_data: Optional[Dict[str, Any]] = None,
    files: Optional[Dict[str, BinaryIO]] = None
) -> Any
```

发送 POST 请求。

**参数**:
- `path`: API 路径
- `data`: 表单数据
- `json_data`: JSON 数据
- `files`: 文件数据

**返回值**:
- 解析后的响应数据

```python
def put(self, path: str, json_data: Dict[str, Any]) -> Any
```

发送 PUT 请求。

**参数**:
- `path`: API 路径
- `json_data`: JSON 数据

**返回值**:
- 解析后的响应数据

```python
def delete(self, path: str, params: Optional[Dict[str, Any]] = None) -> Any
```

发送 DELETE 请求。

**参数**:
- `path`: API 路径
- `params`: 查询参数

**返回值**:
- 解析后的响应数据

### `ApiError`

API 错误异常类。

#### 初始化

```python
def __init__(self, status_code: int, message: str, details: Optional[Dict[str, Any]] = None)
```

**参数**:
- `status_code`: HTTP 状态码
- `message`: 错误消息
- `details`: 错误详情

## 认证模块

### `AuthModule`

处理 AnythingLLM 认证相关的 API。

#### 方法

```python
def login(self, username: str, password: str) -> Dict[str, Any]
```

用户登录。

**参数**:
- `username`: 用户名
- `password`: 密码

**返回值**:
- 包含认证信息的字典，通常包含 token

```python
def validate_token(self, token: Optional[str] = None) -> Dict[str, Any]
```

验证认证令牌。

**参数**:
- `token`: 要验证的令牌，如果未提供则使用当前客户端的令牌

**返回值**:
- 包含验证结果的字典

```python
def check_setup(self) -> Dict[str, Any]
```

检查系统设置状态。

**返回值**:
- 包含系统设置状态的字典

## 工作区模块

### `WorkspacesModule`

处理 AnythingLLM 工作区相关的 API。

#### 方法

```python
def list(self) -> List[Workspace]
```

获取所有工作区列表。

**返回值**:
- 工作区列表

```python
def get(self, workspace_id: str) -> Workspace
```

获取特定工作区的详细信息。

**参数**:
- `workspace_id`: 工作区 ID 或 slug

**返回值**:
- 工作区详细信息

```python
def create(
    self,
    name: str,
    description: Optional[str] = None,
    vector_db: Optional[str] = None
) -> Workspace
```

创建新工作区。

**参数**:
- `name`: 工作区名称
- `description`: 工作区描述
- `vector_db`: 向量数据库类型

**返回值**:
- 创建的工作区信息

```python
def update(
    self,
    workspace_id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    vector_db: Optional[str] = None,
    embedding_model: Optional[str] = None,
    chat_model: Optional[str] = None,
    temperature: Optional[float] = None,
    include_sources: Optional[bool] = None,
    prompt_id: Optional[str] = None,
) -> Workspace
```

更新工作区。

**参数**:
- `workspace_id`: 工作区 ID 或 slug
- `name`: 新工作区名称
- `description`: 新工作区描述
- `vector_db`: 新向量数据库类型
- `embedding_model`: 新嵌入模型
- `chat_model`: 新聊天模型
- `temperature`: 新温度值
- `include_sources`: 是否包含源文档
- `prompt_id`: 提示模板 ID

**返回值**:
- 更新后的工作区信息

```python
def delete(self, workspace_id: str) -> Dict[str, Any]
```

删除工作区。

**参数**:
- `workspace_id`: 工作区 ID 或 slug

**返回值**:
- 删除操作结果

```python
def get_documents(self, workspace_id: str) -> List[Document]
```

获取工作区中的文档。

**参数**:
- `workspace_id`: 工作区 ID 或 slug

**返回值**:
- 文档列表

```python
def add_documents(self, workspace_id: str, document_ids: List[str]) -> Dict[str, Any]
```

向工作区添加文档。

**参数**:
- `workspace_id`: 工作区 ID 或 slug
- `document_ids`: 要添加的文档 ID 列表

**返回值**:
- 操作结果

```python
def remove_document(self, workspace_id: str, document_id: str) -> Dict[str, Any]
```

从工作区移除文档。

**参数**:
- `workspace_id`: 工作区 ID 或 slug
- `document_id`: 要移除的文档 ID

**返回值**:
- 操作结果

## 文档模块

### `DocumentsModule`

处理 AnythingLLM 文档相关的 API。

#### 方法

```python
def list(self) -> List[Document]
```

获取所有文档列表。

**返回值**:
- 文档列表

```python
def get(self, document_id: str) -> Document
```

获取特定文档的详细信息。

**参数**:
- `document_id`: 文档 ID

**返回值**:
- 文档详细信息

```python
def upload(
    self,
    file_path: str = None,
    file_obj: BinaryIO = None,
    add_to_workspaces: Optional[List[str]] = None,
    folder_name: Optional[str] = None
) -> Document
```

上传文档。

**参数**:
- `file_path`: 文件路径
- `file_obj`: 文件对象
- `add_to_workspaces`: 要添加文档的工作区 slug 列表
- `folder_name`: 目标文件夹名称

**返回值**:
- 上传的文档信息

```python
def delete(self, document_id: str) -> Dict[str, Any]
```

删除文档。

**参数**:
- `document_id`: 文档 ID

**返回值**:
- 删除操作结果

```python
def sync(self) -> Dict[str, Any]
```

同步所有文档。

**返回值**:
- 同步操作结果

```python
def get_folders(self) -> List[DocumentFolder]
```

获取所有文档文件夹。

**返回值**:
- 文件夹列表

```python
def create_folder(self, name: str) -> DocumentFolder
```

创建文档文件夹。

**参数**:
- `name`: 文件夹名称

**返回值**:
- 创建的文件夹信息

```python
def delete_folder(self, folder_id: str) -> Dict[str, Any]
```

删除文档文件夹。

**参数**:
- `folder_id`: 文件夹 ID

**返回值**:
- 删除操作结果

## 聊天模块

### `ChatModule`

处理 AnythingLLM 聊天相关的 API。

#### 方法

```python
def send_message(
    self,
    workspace_id: str,
    message: str,
    thread_id: Optional[str] = None,
    system_prompt: Optional[str] = None,
    temperature: Optional[float] = None,
    include_sources: Optional[bool] = None,
) -> ChatMessage
```

发送聊天消息。

**参数**:
- `workspace_id`: 工作区 ID 或 slug
- `message`: 消息内容
- `thread_id`: 对话线程 ID
- `system_prompt`: 系统提示
- `temperature`: 温度值
- `include_sources`: 是否包含源文档

**返回值**:
- 聊天响应

```python
def get_history(
    self,
    workspace_id: str,
    thread_id: Optional[str] = None
) -> List[ChatMessage]
```

获取聊天历史。

**参数**:
- `workspace_id`: 工作区 ID 或 slug
- `thread_id`: 对话线程 ID

**返回值**:
- 聊天历史记录

```python
def clear_history(
    self,
    workspace_id: str,
    thread_id: Optional[str] = None
) -> Dict[str, Any]
```

清除聊天历史。

**参数**:
- `workspace_id`: 工作区 ID 或 slug
- `thread_id`: 对话线程 ID

**返回值**:
- 操作结果

```python
def list_threads(self, workspace_id: str) -> List[ChatThread]
```

获取工作区的所有对话线程。

**参数**:
- `workspace_id`: 工作区 ID 或 slug

**返回值**:
- 对话线程列表

```python
def create_thread(
    self,
    workspace_id: str,
    name: str,
    description: Optional[str] = None
) -> ChatThread
```

创建新的对话线程。

**参数**:
- `workspace_id`: 工作区 ID 或 slug
- `name`: 线程名称
- `description`: 线程描述

**返回值**:
- 创建的线程信息

```python
def update_thread(
    self,
    workspace_id: str,
    thread_id: str,
    name: Optional[str] = None,
    description: Optional[str] = None
) -> ChatThread
```

更新对话线程。

**参数**:
- `workspace_id`: 工作区 ID 或 slug
- `thread_id`: 线程 ID
- `name`: 新线程名称
- `description`: 新线程描述

**返回值**:
- 更新后的线程信息

```python
def delete_thread(self, workspace_id: str, thread_id: str) -> Dict[str, Any]
```

删除对话线程。

**参数**:
- `workspace_id`: 工作区 ID 或 slug
- `thread_id`: 线程 ID

**返回值**:
- 删除操作结果

## 系统模块

### `SystemModule`

处理 AnythingLLM 系统相关的 API。

#### 方法

```python
def get_health(self) -> Dict[str, Any]
```

获取系统健康状态。

**返回值**:
- 系统健康状态信息

```python
def get_settings(self) -> SystemSettings
```

获取系统设置。

**返回值**:
- 系统设置信息

```python
def update_settings(self, settings: Dict[str, Any]) -> SystemSettings
```

更新系统设置。

**参数**:
- `settings`: 要更新的设置

**返回值**:
- 更新后的系统设置

```python
def get_llm_models(self) -> List[LLMModel]
```

获取可用的 LLM 模型。

**返回值**:
- LLM 模型列表

```python
def get_embedding_models(self) -> List[EmbeddingModel]
```

获取可用的嵌入模型。

**返回值**:
- 嵌入模型列表

```python
def get_vector_dbs(self) -> List[VectorDatabase]
```

获取可用的向量数据库。

**返回值**:
- 向量数据库列表

```python
def get_accepted_document_types(self) -> List[str]
```

获取系统接受的文档类型。

**返回值**:
- 接受的文档类型列表

```python
def get_prompts(self) -> List[Prompt]
```

获取系统提示模板。

**返回值**:
- 提示模板列表

```python
def create_prompt(
    self,
    title: str,
    content: str,
    description: Optional[str] = None
) -> Prompt
```

创建系统提示模板。

**参数**:
- `title`: 提示标题
- `content`: 提示内容
- `description`: 提示描述

**返回值**:
- 创建的提示模板

```python
def update_prompt(
    self,
    prompt_id: str,
    title: Optional[str] = None,
    content: Optional[str] = None,
    description: Optional[str] = None
) -> Prompt
```

更新系统提示模板。

**参数**:
- `prompt_id`: 提示模板 ID
- `title`: 新提示标题
- `content`: 新提示内容
- `description`: 新提示描述

**返回值**:
- 更新后的提示模板

```python
def delete_prompt(self, prompt_id: str) -> Dict[str, Any]
```

删除系统提示模板。

**参数**:
- `prompt_id`: 提示模板 ID

**返回值**:
- 删除操作结果

## 用户模块

### `UsersModule`

处理 AnythingLLM 用户相关的 API。

#### 方法

```python
def list(self) -> List[User]
```

获取所有用户列表。

**返回值**:
- 用户列表

```python
def get(self, user_id: str) -> User
```

获取特定用户的详细信息。

**参数**:
- `user_id`: 用户 ID

**返回值**:
- 用户详细信息

```python
def create(
    self,
    username: str,
    password: str,
    role: str = "user",
    customization: Optional[Dict[str, Any]] = None
) -> User
```

创建新用户。

**参数**:
- `username`: 用户名
- `password`: 密码
- `role`: 用户角色，默认为 "user"
- `customization`: 用户自定义设置

**返回值**:
- 创建的用户信息

```python
def update(
    self,
    user_id: str,
    username: Optional[str] = None,
    password: Optional[str] = None,
    role: Optional[str] = None,
    customization: Optional[Dict[str, Any]] = None
) -> User
```

更新用户。

**参数**:
- `user_id`: 用户 ID
- `username`: 新用户名
- `password`: 新密码
- `role`: 新用户角色
- `customization`: 新用户自定义设置

**返回值**:
- 更新后的用户信息

```python
def delete(self, user_id: str) -> Dict[str, Any]
```

删除用户。

**参数**:
- `user_id`: 用户 ID

**返回值**:
- 删除操作结果

```python
def get_api_keys(self) -> List[ApiKey]
```

获取所有 API 密钥。

**返回值**:
- API 密钥列表

```python
def create_api_key(
    self,
    name: str,
    expires_at: Optional[str] = None
) -> ApiKey
```

创建新 API 密钥。

**参数**:
- `name`: API 密钥名称
- `expires_at`: 过期时间，ISO 格式

**返回值**:
- 创建的 API 密钥信息

```python
def delete_api_key(self, key_id: str) -> Dict[str, Any]
```

删除 API 密钥。

**参数**:
- `key_id`: API 密钥 ID

**返回值**:
- 删除操作结果

## 嵌入模块

### `EmbedModule`

处理 AnythingLLM 嵌入相关的 API。

#### 方法

```python
def get_text_embedding(self, text: str) -> Dict[str, Any]
```

获取文本嵌入向量。

**参数**:
- `text`: 要嵌入的文本

**返回值**:
- 嵌入向量结果

```python
def get_batch_embeddings(self, texts: List[str]) -> Dict[str, Any]
```

批量获取文本嵌入向量。

**参数**:
- `texts`: 要嵌入的文本列表

**返回值**:
- 嵌入向量结果

## 管理员模块

### `AdminModule`

处理 AnythingLLM 管理员相关的 API。

#### 方法

```python
def is_multi_user_mode(self) -> Dict[str, bool]
```

检查实例是否处于多用户模式。

**返回值**:
- 包含多用户模式状态的字典

```python
def create_user(
    self,
    username: str,
    password: str,
    role: str = "default"
) -> Dict[str, User]
```

创建新用户。

**参数**:
- `username`: 用户名
- `password`: 密码
- `role`: 用户角色，默认为 "default"

**返回值**:
- 创建的用户信息

```python
def update_user(
    self,
    user_id: str,
    username: Optional[str] = None,
    password: Optional[str] = None,
    role: Optional[str] = None
) -> Dict[str, User]
```

更新用户。

**参数**:
- `user_id`: 用户 ID
- `username`: 新用户名
- `password`: 新密码
- `role`: 新用户角色

**返回值**:
- 更新后的用户信息

```python
def delete_user(self, user_id: str) -> Dict[str, Any]
```

删除用户。

**参数**:
- `user_id`: 用户 ID

**返回值**:
- 删除操作结果

```python
def create_invite(self, workspace_ids: Optional[List[int]] = None) -> Dict[str, Invite]
```

创建新的邀请码。

**参数**:
- `workspace_ids`: 工作区 ID 列表

**返回值**:
- 创建的邀请码信息

```python
def get_invites(self) -> List[Invite]
```

获取所有邀请码。

**返回值**:
- 邀请码列表

```python
def delete_invite(self, invite_id: str) -> Dict[str, Any]
```

删除邀请码。

**参数**:
- `invite_id`: 邀请码 ID

**返回值**:
- 删除操作结果

```python
def get_system_preferences(self) -> SystemSettings
```

获取系统偏好设置。

**返回值**:
- 系统偏好设置

```python
def update_system_preferences(self, preferences: Dict[str, Any]) -> SystemSettings
```

更新系统偏好设置。

**参数**:
- `preferences`: 新的系统偏好设置

**返回值**:
- 更新后的系统偏好设置

## OpenAI 兼容模块

### `OpenAIModule`

处理 AnythingLLM OpenAI 兼容 API。

#### 方法

```python
def list_models(self) -> List[OpenAIModel]
```

获取所有可用的“模型”，实际上是可用于聊天的工作区。

**返回值**:
- 模型列表

```python
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
) -> Dict[str, Any]
```

创建聊天完成。

**参数**:
- `model`: 模型名称（工作区 slug）
- `messages`: 消息列表，每个消息包含 role 和 content
- `temperature`: 温度值
- `stream`: 是否流式输出
- `max_tokens`: 最大令牌数
- `top_p`: top_p 值
- `frequency_penalty`: 频率惩罚
- `presence_penalty`: 存在惩罚

**返回值**:
- 聊天完成结果

```python
def list_vector_stores(self) -> List[VectorStore]
```

获取所有向量数据库集合。

**返回值**:
- 向量数据库集合列表

```python
def create_embedding(self, input_text: Union[str, List[str]], model: Optional[str] = None) -> Dict[str, Any]
```

创建嵌入向量。

**参数**:
- `input_text`: 输入文本或文本列表
- `model`: 模型名称

**返回值**:
- 嵌入向量结果

## 工作区线程模块

### `WorkspaceThreadModule`

处理 AnythingLLM 工作区线程相关的 API。

#### 方法

```python
def list_threads(self, workspace_id: str) -> List[ChatThread]
```

获取工作区的所有线程。

**参数**:
- `workspace_id`: 工作区 ID 或 slug

**返回值**:
- 线程列表

```python
def get_thread(self, workspace_id: str, thread_id: str) -> ChatThread
```

获取特定线程的详细信息。

**参数**:
- `workspace_id`: 工作区 ID 或 slug
- `thread_id`: 线程 ID

**返回值**:
- 线程详细信息

```python
def create_thread(
    self,
    workspace_id: str,
    name: str,
    description: Optional[str] = None
) -> ChatThread
```

创建新线程。

**参数**:
- `workspace_id`: 工作区 ID 或 slug
- `name`: 线程名称
- `description`: 线程描述

**返回值**:
- 创建的线程信息

```python
def update_thread(
    self,
    workspace_id: str,
    thread_id: str,
    name: Optional[str] = None,
    description: Optional[str] = None
) -> ChatThread
```

更新线程。

**参数**:
- `workspace_id`: 工作区 ID 或 slug
- `thread_id`: 线程 ID
- `name`: 新线程名称
- `description`: 新线程描述

**返回值**:
- 更新后的线程信息

```python
def delete_thread(self, workspace_id: str, thread_id: str) -> Dict[str, Any]
```

删除线程。

**参数**:
- `workspace_id`: 工作区 ID 或 slug
- `thread_id`: 线程 ID

**返回值**:
- 删除操作结果

```python
def get_thread_messages(self, workspace_id: str, thread_id: str) -> List[ChatMessage]
```

获取线程的所有消息。

**参数**:
- `workspace_id`: 工作区 ID 或 slug
- `thread_id`: 线程 ID

**返回值**:
- 消息列表

```python
def send_message(
    self,
    workspace_id: str,
    thread_id: str,
    message: str,
    system_prompt: Optional[str] = None,
    temperature: Optional[float] = None,
    include_sources: Optional[bool] = None,
) -> ChatMessage
```

发送消息到线程。

**参数**:
- `workspace_id`: 工作区 ID 或 slug
- `thread_id`: 线程 ID
- `message`: 消息内容
- `system_prompt`: 系统提示
- `temperature`: 温度值
- `include_sources`: 是否包含源文档

**返回值**:
- 消息响应

```python
def clear_thread_messages(self, workspace_id: str, thread_id: str) -> Dict[str, Any]
```

清除线程的所有消息。

**参数**:
- `workspace_id`: 工作区 ID 或 slug
- `thread_id`: 线程 ID

**返回值**:
- 清除操作结果

## 类型定义

### `Workspace`

工作区类型。

```python
class Workspace(TypedDict, total=False):
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
```

### `Document`

文档类型。

```python
class Document(TypedDict, total=False):
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
```

### `DocumentFolder`

文档文件夹类型。

```python
class DocumentFolder(TypedDict, total=False):
    id: str
    name: str
    path: str
    createdAt: str
    updatedAt: str
    documentCount: int
```

### `ChatMessage`

聊天消息类型。

```python
class ChatMessage(TypedDict, total=False):
    id: str
    role: str
    content: str
    createdAt: str
    sources: List[Dict[str, Any]]
    threadId: Optional[str]
    workspaceId: str
```

### `ChatThread`

聊天线程类型。

```python
class ChatThread(TypedDict, total=False):
    id: str
    name: str
    description: Optional[str]
    createdAt: str
    updatedAt: str
    workspaceId: str
    messageCount: int
```

### `User`

用户类型。

```python
class User(TypedDict, total=False):
    id: str
    username: str
    role: str
    createdAt: str
    updatedAt: str
    customization: Dict[str, Any]
```

### `ApiKey`

API 密钥类型。

```python
class ApiKey(TypedDict, total=False):
    id: str
    name: str
    key: str
    createdAt: str
    expiresAt: Optional[str]
    lastUsed: Optional[str]
```

### `Prompt`

提示模板类型。

```python
class Prompt(TypedDict, total=False):
    id: str
    title: str
    content: str
    description: Optional[str]
    createdAt: str
    updatedAt: str
```

### `LLMModel`

LLM 模型类型。

```python
class LLMModel(TypedDict, total=False):
    id: str
    name: str
    provider: str
    tokenLimit: int
    available: bool
```

### `EmbeddingModel`

嵌入模型类型。

```python
class EmbeddingModel(TypedDict, total=False):
    id: str
    name: str
    provider: str
    dimensions: int
    available: bool
```

### `VectorDatabase`

向量数据库类型。

```python
class VectorDatabase(TypedDict, total=False):
    id: str
    name: str
    provider: str
    available: bool
```

### `SystemSettings`

系统设置类型。

```python
class SystemSettings(TypedDict, total=False):
    serverName: str
    serverDescription: str
    allowUserSignup: bool
    allowAnonymousUsers: bool
    defaultLLMProvider: str
    defaultEmbeddingProvider: str
    defaultVectorDB: str
    customSettings: Dict[str, Any]
```
