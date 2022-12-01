from setuptools import setup, find_packages


setup(
    name="bookmark-url",
    version="0.0.1",
    description="CLIでBookmark操作を行うツール。",
    author="gamari",
    packages=find_packages(where="src"),
    install_requires=['fire'],
    entry_points={
        "console_scripts": [
            "myapp = src.main:main",
        ]
    }
)
