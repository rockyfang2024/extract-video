#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extract Video - 视频提取和下载系统
项目初始化配置文件
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="extract-video",
    version="1.0.0",
    author="Rocky Fang",
    description="从网页提取、识别和下载视频的完整系统",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.8",
    packages=find_packages(),
    install_requires=[
        "flask==2.3.3",
        "flask-cors==4.0.0",
        "yt-dlp==2023.11.16",
        "requests==2.31.0",
        "beautifulsoup4==4.12.2",
        "selenium==4.13.0",
        "python-dotenv==1.0.0",
        "sqlalchemy==2.0.23",
        "flask-sqlalchemy==3.1.1",
        "werkzeug==2.3.7",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)