from setuptools import setup, find_packages

setup(
    name="anythingllm_client",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
        "pydantic>=2.0.0",
        "python-dotenv>=0.19.0",
        "tqdm>=4.62.0",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python client for AnythingLLM API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/anythingllm-client",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
