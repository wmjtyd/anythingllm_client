"""
测试导入 AnythingLLMClient
"""

try:
    from anythingllm_client import AnythingLLMClient
    print("成功导入 AnythingLLMClient")
    print(f"AnythingLLMClient 类型: {type(AnythingLLMClient)}")
except ImportError as e:
    print(f"导入错误: {e}")
    
    # 尝试直接导入
    try:
        from anythingllm_client.client import AnythingLLMClient
        print("成功从 client.py 直接导入 AnythingLLMClient")
    except ImportError as e2:
        print(f"直接导入错误: {e2}")
        
    # 检查 sys.path
    import sys
    print("\nPython 路径:")
    for path in sys.path:
        print(f"  - {path}")
        
    # 检查模块结构
    import pkgutil
    print("\n可用的模块:")
    for module in pkgutil.iter_modules():
        if "anythingllm" in module.name:
            print(f"  - {module.name}")
