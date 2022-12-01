from setuptools import setup, find_packages


setup(
    name="bookmark",
    version="0.0.1",
    description="CLIでBookmark操作を行うツール。",
    author="gamari",
    packages=find_packages(),
    install_requires=['fire'],
    entry_points='''
        [console_scripts]
        bookmark=src.app:main
    ''',
)
