from setuptools import setup, find_packages

setup(
    name="RapidOCR_pytorch",  # 包名
    version="1.0.0",  # 版本号
    author="zekunzhang",  # 作者名
    author_email="zekunzhang46@outlook.com",  # 作者邮箱
    description="A implementation of RapidOCR using PyTorch",  # 简短描述
    long_description=open("README.md").read(),  # 长描述
    long_description_content_type="text/markdown",  # 描述格式
    url="https://github.com/zzk2021/RapidOCR_pytorch",  # 项目主页
    packages=find_packages(),  # 自动查找包
    install_requires=[  # 依赖项
        "torch>=1.8.0",
        "opencv-python>=4.5.0",
        "numpy>=1.19.0",
        "Pillow>=10.3.0",
    ],
    classifiers=[  # 分类器
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",  # 支持的 Python 版本
    entry_points={  # 可选：定义命令行工具入口点
        "console_scripts": [
            "rapidocr=your_package_name.cli:main",  # 将命令行工具绑定到函数
        ],
    },
)