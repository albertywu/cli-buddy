from setuptools import setup, find_packages

setup(
    name="clibuddy",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "click",
        "openai",
    ],
    entry_points={
        "console_scripts": [
            "clibuddy = clibuddy.cli:main",
        ],
    },
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)