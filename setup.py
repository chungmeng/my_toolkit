from setuptools import setup, find_packages

setup(
    name='my_toolkit',
    version='1.0.0',
    description="Jerome Lim's Python Toolkit",
    author = 'jerome',
    author_email = 'chungmeng@omnilytics.co',
    packages = find_packages(exclude=['my_toolkit.tests*']),
)