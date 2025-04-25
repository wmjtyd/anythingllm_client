#!/usr/bin/env python3
"""
文档管理示例
"""

import os
import sys
import json
from dotenv import load_dotenv

# 添加项目根目录到 Python 路径
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 使用正确的导入路径
from anythingllm_client.anythingllm_client import AnythingLLMClient

# 加载环境变量
load_dotenv()

# 配置
API_KEY = os.getenv("ANYTHINGLLM_API_KEY", "PM2XHGK-951MAPY-HJ1CC2V-V0ZKQ28")
BASE_URL = os.getenv("ANYTHINGLLM_BASE_URL", "http://localhost:3001")


def print_json(data):
    """美化打印 JSON 数据"""
    print(json.dumps(data, ensure_ascii=False, indent=2))


def main():
    """主函数"""
    # 初始化客户端
    client = AnythingLLMClient(base_url=BASE_URL, api_key=API_KEY)

    print("=== 获取所有文档 ===")
    documents = client.documents.list()
    print_json(documents)

    print("\n=== 获取所有文档文件夹 ===")
    folders = client.documents.get_folders()
    print_json(folders)

    print("\n=== 创建新文档文件夹 ===")
    new_folder = client.documents.create_folder(name="测试文件夹")
    print_json(new_folder)

    # 上传文档示例
    # 注意：请将路径替换为实际的文档路径
    document_path = "examples/sample_document.pdf"
    if os.path.exists(document_path):
        print(f"\n=== 上传文档 {document_path} ===")
        uploaded_document = client.documents.upload(
            file_path=document_path,
            folder_name="测试文件夹"
        )
        print_json(uploaded_document)

        document_id = uploaded_document.get("id")
        if document_id:
            print(f"\n=== 获取文档 {document_id} 的详细信息 ===")
            document_details = client.documents.get(document_id)
            print_json(document_details)

            print(f"\n=== 删除文档 {document_id} ===")
            delete_result = client.documents.delete(document_id)
            print_json(delete_result)
    else:
        print(f"文档 {document_path} 不存在，跳过上传示例")

    # 获取文件夹 ID
    folder_id = new_folder.get("id")
    if folder_id:
        print(f"\n=== 删除文件夹 {folder_id} ===")
        delete_folder_result = client.documents.delete_folder(folder_id)
        print_json(delete_folder_result)


if __name__ == "__main__":
    main()
